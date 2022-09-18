import json


def get_instance_name(tags):
    for tag in tags:
        if tag['Key'] == 'Name':
            return tag['Value']

    raise RuntimeError('Name was not found')


def prepare_ansible_inventory():
    with open('hosts.json') as f:
        instances = json.load(f)

    hosts = []
    for instance in instances:
        instance_name = get_instance_name(instance['Tags'])
        instance_ip = instance['PublicIpAddress']

        hosts.append(
            f"{instance_name} ansible_host={instance_ip}\n"
        )

    with open('hosts', 'w') as f:
        f.write('[bot]\n')
        f.writelines(hosts)


if __name__ == '__main__':

    prepare_ansible_inventory()
