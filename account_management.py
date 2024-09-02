from datetime import datetime, timedelta, timezone
import re
import sys, traceback
import subprocess

subprocess.call('pip install boto3>=1.24,<2.0 --target /tmp/ --no-cache-dir'.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
sys.path.insert(0, '/tmp/')

import boto3

UNATTACHED_EBS_LIFESPAN = 7
LOAD_BALANCER_LIFESPAN = 30
STOPPED_EC2_LIFESPAN = 30
DB_LIFESPAN = 30

# UNATTACHED_EBS_LIFESPAN = ${UnattachedVolumesLifespan}
# LOAD_BALANCER_LIFESPAN = ${LoadBalancerLifespan}
# STOPPED_EC2_LIFESPAN = ${StoppedEC2InstanceLifespan}
# DB_LIFESPAN = ${DatabaseRDSLifespan}


def delete_non_attached_old_ebs(region):
    ec2 = boto3.client('ec2', region_name=region['RegionName'])

    unattached_vols = ec2.describe_volumes(
        Filters=[
            {
                'Name': 'status',
                'Values': ['available']
            }
        ]
    )

    cloud_trail = boto3.client('cloudtrail', region_name=region['RegionName'])

    volume_detachments = cloud_trail.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'EventName',
                'AttributeValue': 'DetachVolume'
            }
        ],
        StartTime=datetime.now(timezone.utc) - timedelta(days=UNATTACHED_EBS_LIFESPAN)
    )

    detached_vol_ids = []
    for event in volume_detachments['Events']:
        for resource in event.get('Resources', []):
            if 'volume' in resource['ResourceType'].lower():
                detached_vol_ids.append(resource['ResourceName'])

    for volume in unattached_vols['Volumes']:
        if volume['VolumeId'] not in detached_vol_ids:
            print(f'Deleting old unattached EBS: {volume}')
            response = ec2.delete_volume(VolumeId=volume['VolumeId'])


def delete_old_load_balancers(region):
    elb = boto3.client('elbv2', region_name=region['RegionName'])
    lbs = elb.describe_load_balancers()
    for lb in lbs['LoadBalancers']:
        lb_lifetime = datetime.now(timezone.utc) - lb['CreatedTime']
        lb_lifespan = timedelta(days=LOAD_BALANCER_LIFESPAN)
        tags = elb.describe_tags(ResourceArns=[lb['LoadBalancerArn']])
        for tag in tags['TagDescriptions']:
            for t in tag.get('Tags', []):
                if t['Key'].lower().strip() == 'lifespan':
                    try:
                        lb_lifespan = timedelta(days=max(int(t['Value']), LOAD_BALANCER_LIFESPAN))
                    except:
                        pass

        if lb_lifetime > lb_lifespan:
            print(f'Deleting old LB: {lb}')
            response = elb.delete_load_balancer(LoadBalancerArn=lb['LoadBalancerArn'])


def stop_and_terminate_ec2(region):
    ec2 = boto3.client('ec2', region_name=region['RegionName'])

    instances_to_stop = []
    instances_to_terminate = []
    next_token = ''
    while next_token is not None:
        descriptions = ec2.describe_instances(
            # Filters=[
            #     {
            #         'Name': 'instance-lifecycle',
            #         'Values': ['scheduled']  # TODO exclude stop instances
            #     }
            # ],
            NextToken=next_token
        )

        for description in descriptions['Reservations']:
            for instance in description['Instances']:
                ec2_lifespan = timedelta(days=STOPPED_EC2_LIFESPAN)

                # valid state values: 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                if instance['State']['Name'] in ['running']:

                    res = ec2.modify_instance_attribute(
                        InstanceId=instance['InstanceId'],
                        DisableApiStop={'Value': False}
                    )
                    instances_to_stop.append(instance['InstanceId'])

                elif instance['State']['Name'] in ['stopped']:
                    stopped_reason = instance['StateTransitionReason']
                    stopped_time = re.findall('.*\((.*)\)', stopped_reason)
                    if stopped_time:
                        stopped_time = datetime.strptime(stopped_time[0].split(' ')[0], '%Y-%m-%d')

                        for tag in instance.get('Tags', []):
                            if tag['Key'].lower().strip() == 'lifespan':
                                try:
                                    ec2_lifespan = timedelta(days=max(int(tag['Value']), STOPPED_EC2_LIFESPAN))
                                except:
                                    pass

                        if datetime.now() - stopped_time > ec2_lifespan:
                            res = ec2.modify_instance_attribute(
                                InstanceId=instance['InstanceId'],
                                DisableApiTermination={'Value': False}
                            )
                            instances_to_terminate.append(instance['InstanceId'])

        next_token = descriptions.get('NextToken')

    if instances_to_stop:
        print(f'Instances to stop: {instances_to_stop}')
        response = ec2.stop_instances(InstanceIds=instances_to_stop)

    if instances_to_terminate:
        print(f'Instances to terminate: {instances_to_terminate}')
        # response = ec2.terminate_instances(InstanceIds=instances_to_terminate)


def delete_old_rds_db_instances(region):
    rds = boto3.client('rds', region_name=region['RegionName'])
    dbs = rds.describe_db_instances()

    for db in dbs['DBInstances']:
        db_lifespan = timedelta(days=DB_LIFESPAN)

        tags = rds.list_tags_for_resource(
            ResourceName=db['DBInstanceArn']
        )
        for tag in tags.get('TagList', []):
            if tag['Key'].lower().strip() == 'lifespan':
                try:
                    db_lifespan = timedelta(days=max(int(tag['Value']), DB_LIFESPAN))
                except:
                    pass

        if db['DBInstanceStatus'] != 'deleting' and datetime.now(timezone.utc) - db['InstanceCreateTime'] > db_lifespan:
            print(f'Deleting RDS DB: {db}')
            response = rds.delete_db_instance(
                DBInstanceIdentifier=db['DBInstanceIdentifier'],
                SkipFinalSnapshot=True
            )


def handler(event, context):

    client = boto3.client('ec2')
    regions = client.describe_regions()

    for region in regions['Regions']:

        if not (region['RegionName'].startswith('eu') or region['RegionName'].startswith('us')):
            continue

        print(f'Working on region {region["RegionName"]}')

        try:
            stop_and_terminate_ec2(region)
            delete_non_attached_old_ebs(region)
            delete_old_load_balancers(region)
            delete_old_rds_db_instances(region)
        except:
            print(f'Error occured during maintenance job')
            traceback.print_exc(file=sys.stdout)
            


# handler(None, None)
