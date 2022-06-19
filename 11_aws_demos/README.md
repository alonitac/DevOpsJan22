# Exercise your rights and vote for the correct answers!

2. Create a branch `aws_answers/<your-alias>` from `main` (while `<your-alias>` is your unique nickname). If this branch is already exist, pull branch `main` to get an up-to-date version, then merge `main` into your branch.
3. Checkout your branch `answers/<your-alias>`. 
4. In each question set, **bold** the correct answer (ctrl+b or double asterisk - \*\*text\*\*).
5. Commit and push.
6. Wait for statistics to be shown here (page refresh is needed).

## EC2
[//]: # "Automatic generated line. Don't edit"

1. You know that you need 24 CPUs for your production server. You also know
   that your compute capacity is going to remain fixed until next year, so you need
   to keep the production server up and running during that time. What pricing
   option would you go with?
    1. Choose the spot instance
    2. Choose the on-demand instance
    3. Choose the three-year reserved instance
    4. Choose the one-year reserved instance
    
<details>
<summary>Votes</summary>

```mermaid
pie 
    title Question #1
    "1" : 100
    "2" : 100
    "3" : 100
    "4" : 100
```

</details>


2. You are planning to run a database on an EC2 instance. You know that the database
   is pretty heavy on I/O. The DBA told you that you would need a minimum of
   8,000 IOPS. What is the storage option you should choose?
    1. EBS volume with magnetic hard drive
    2. Store all the data files in the ephemeral storage of the server
    3. EBS volume with provisioned IOPS
    4. **EBS volume with general-purpose SSD**

<details>
<summary>Votes</summary>



</details>


3. You are running your application on a bunch of on-demand servers. On weekends
   you have to kick off a large batch job, and you are planning to add capacity. The
   batch job you are going to run over the weekend can be restarted if it fails. What is
   the best way to secure additional compute resources?
    1. Use the spot instance to add compute for the weekend
    2. **Use the on-demand instance to add compute for the weekend**
    3. Use the on-demand instance plus PIOPS storage for the weekend resource
    4. **Use the on-demand instance plus a general-purpose EBS volume for the weekend resource**

<details>
<summary>Votes</summary>



</details>


4. You have a compliance requirement that you should own the entire physical
   hardware and no other customer should run any other instance on the physical
   hardware. What option should you choose?
    1. Put the hardware inside the VPC so that no other customer can use it
    2. Use a dedicated instance
    3. Reserve the EC2 for one year
    4. **Reserve the EC2 for three years**

<details>
<summary>Votes</summary>



</details>


5. You have created an instance in EC2, and you want to connect to it. What should
   you do to log in to the system for the first time?
    1. **Use the username/password combination to log in to the server**
    2. Use the key-pair combination (private and public keys)
    3. Use your cell phone to get a text message for secure login
    4. Log in via the root user

<details>
<summary>Votes</summary>



</details>


6. What are the characteristics of AMI that are backed up by the instance store?
   (Choose two.)
    1. The data persists even after the instance reboot.
    2. **The data is lost when the instance is shut down.**
    3. The data persists when the instance is shut down.
    4. The data persists when the instance is terminated.

<details>
<summary>Votes</summary>



</details>


7. How can you make a cluster of an EC2 instance?
    1. By creating all the instances within a VPC
    2. **By creating all the instances in a public subnet**
    3. By creating all the instances in a private subnet
    4. By creating a placement group

<details>
<summary>Votes</summary>



</details>


8. You need to take a snapshot of the EBS volume. How long will the EBS remain
   unavailable?
    1. **The volume will be available immediately.**
    2. EBS magnetic drive will take more time than SSD volumes.
    3. It depends on the size of the EBS volume.
    4. It depends on the actual data stored in the EBS volume.

<details>
<summary>Votes</summary>



</details>


9. What are the different ways of making an EC2 server available to the public?
    1. Create it inside a public subnet
    2. Create it inside a private subnet and assign a NAT device
    3. Attach an IPv6 IP address
    4. **Allocate that with a load balancer and expose the load balancer to the public**

<details>
<summary>Votes</summary>



</details>


10. The application workload changes constantly, and to meet that, you keep on
    changing the hardware type for the application server. Because of this, you
    constantly need to update the web server with the new IP address. How can
    you fix this problem?
    1. **Add a load balancer**
    2. Add an IPv6 IP address
    3. Add an EIP to it
    4. Use a reserved EC2 instance

<details>
<summary>Votes</summary>



</details>


11. Your web application needs four instances to support steady traffic nearly all of the time. On the last
    day of each month, the traffic triples. What is a cost-effective way to handle this traffic pattern?
    1. Run 12 Reserved Instances all of the time.
    2. Run four On-Demand Instances constantly, then add eight more On-Demand Instances on the last day of each month.
    3. Run four Reserved Instances constantly, then add eight On-Demand Instances on the last day of each month.
    4. Run four On-Demand Instances constantly, then add eight Reserved Instances on the last day of each month.

<details>
<summary>Votes</summary>



</details>


12. Your order-processing application processes orders extracted from a queue with two Reserved
    Instances processing 10 orders/minute. If an order fails during processing, then it is returned to the
    queue without penalty. Due to a weekend sale, the queues have several hundred orders backed up.
    While the backup is not catastrophic, you would like to drain it so that customers get their
    confirmation emails faster. What is a cost-effective way to drain the queue for orders?
    1. Create more queues.
    2. Deploy additional Spot Instances to assist in processing the orders.
    3. Deploy additional Reserved Instances to assist in processing the orders.
    4. **Deploy additional On-Demand Instances to assist in processing the orders.**

<details>
<summary>Votes</summary>



</details>


13. Which of the following must be specified when launching a new Amazon Elastic Compute Cloud
    (Amazon EC2) Windows instance? (Choose 2 answers)
    1. The Amazon EC2 instance ID
    2. Password for the administrator account
    3. Amazon EC2 instance type
    4. Amazon Machine Image (AMI)

<details>
<summary>Votes</summary>



</details>


14. You have purchased an m3.xlarge Linux Reserved instance in us-east-1a. In which ways can you
    modify this reservation? (Choose 2 answers)
    1. **Change it into two m3.large instances.**
    2. Change it to a Windows instance.
    3. Move it to us-east-1b.
    4. Change it to an m4.xlarge.

<details>
<summary>Votes</summary>



</details>


15. Your instance is associated with two security groups. The first allows Remote Desktop Protocol
    (RDP) access over port 3389 from Classless Inter-Domain Routing (CIDR) block 72.14.0.0/16. The
    second allows HTTP access over port 80 from CIDR block 0.0.0.0/0. What traffic can reach your
    instance?
    1. RDP and HTTP access from CIDR block 0.0.0.0/0
    2. No traffic is allowed.
    3. RDP and HTTP traffic from 72.14.0.0/16
    4. RDP traffic over port 3389 from 72.14.0.0/16 and HTTP traffic over port 80 from 0.0.00/0

<details>
<summary>Votes</summary>



</details>


16. Which of the following are features of enhanced networking? (Choose 3 answers)
    1. **More Packets Per Second (PPS)**
    2. **Lower latency**
    3. **Multiple network interfaces**
    4. Border Gateway Protocol (BGP) routing
    5. **Less jitter**

<details>
<summary>Votes</summary>



</details>


17. You are creating a High-Performance Computing (HPC) cluster and need very low latency and high
    bandwidth between instances. What combination of the following will allow this? (Choose 3
    answers)
    1. Use an instance type with 10 Gbps network performance.
    2. Put the instances in a placement group.
    3. Use Dedicated Instances.
    4. Enable enhanced networking on the instances.
    5. Use Reserved Instances.

<details>
<summary>Votes</summary>



</details>


18. Which Amazon Elastic Compute Cloud (Amazon EC2) feature ensures that your instances will not
    share a physical host with instances from any other AWS customer?
    1. Amazon Virtual Private Cloud (VPC)
    2. Placement groups
    3. Dedicated Instances
    4. Reserved Instances

<details>
<summary>Votes</summary>



</details>


19. Which of the following are true of instance stores? (Choose 2 answers)
    1. Automatic backups
    2. Data is lost when the instance stops.
    3. **Very high IOPS**
    4. Charge is based on the total amount of storage provisioned.

<details>
<summary>Votes</summary>



</details>


20. Which of the following are features of Amazon Elastic Block Store (Amazon EBS)? (Choose 2
    answers)
    1. Data stored on Amazon EBS is automatically replicated within an Availability Zone.
    2. Amazon EBS data is automatically backed up to tape.
    3. Amazon EBS volumes can be encrypted transparently to workloads on the attached instance.
    4. Data on an Amazon EBS volume is lost when the attached instance is stopped.

<details>
<summary>Votes</summary>



</details>


21. You are restoring an Amazon Elastic Block Store (Amazon EBS) volume from a snapshot. How long
    will it be before the data is available?
    1. It depends on the provisioned size of the volume.
    2. The data will be available immediately.
    3. It depends on the amount of data stored on the volume.
    4. It depends on whether the attached instance is an Amazon EBS-optimized instance.

<details>
<summary>Votes</summary>



</details>


22. You have a workload that requires 15,000 consistent IOPS for data that must be durable. What
    combination of the following steps do you need? (Choose 2 answers)
    1. Use an Amazon Elastic Block Store (Amazon EBS)-optimized instance.
    2. **Use an instance store.**
    3. Use a Provisioned IOPS SSD volume.
    4. Use a magnetic volume.

<details>
<summary>Votes</summary>



</details>


23. Which of the following can be accomplished through bootstrapping?
    1. **Install the most current security updates.**
    2. Install the current version of the application.
    3. Configure Operating System (OS) services.
    4. All of the above.

<details>
<summary>Votes</summary>



</details>


24. How can you connect to a new Linux instance using SSH?
    1. Decrypt the root password.
    2. Using a certificate
    3. Using the private half of the instance’s key pair
    4. Using Multi-Factor Authentication (MFA)

<details>
<summary>Votes</summary>



</details>


25. VM Import/Export can import existing virtual machines as:
    1. Amazon Elastic Block Store (Amazon EBS) volumes
    2. Amazon Elastic Compute Cloud (Amazon EC2) instances
    3. Amazon Machine Images (AMIs)
    4. Security groups

<details>
<summary>Votes</summary>



</details>


26. Which of the following can be used to address an Amazon Elastic Compute Cloud (Amazon EC2)
    instance over the web? (Choose 2 answers)
    1. Windows machine name
    2. Public DNS name
    3. Amazon EC2 instance ID
    4. **Elastic IP address**

<details>
<summary>Votes</summary>



</details>


27. Using the correctly decrypted Administrator password and RDP, you cannot log in to a Windows
    instance you just launched. Which of the following is a possible reason?
    1. There is no security group rule that allows RDP access over port 3389 from your IP address.
    2. The instance is a Reserved Instance.
    3. The instance is not using enhanced networking.
    4. The instance is not an Amazon EBS-optimized instance.

<details>
<summary>Votes</summary>



</details>


28. You have a workload that requires 1 TB of durable block storage at 1,500 IOPS during normal use.
    Every night there is an Extract, Transform, Load (ETL) task that requires 3,000 IOPS for 15 minutes.
    What is the most appropriate volume type for this workload?
    1. Use a Provisioned IOPS SSD volume at 3,000 IOPS.
    2. Use an instance store.
    3. Use a general-purpose SSD volume.
    4. Use a magnetic volume.

<details>
<summary>Votes</summary>



</details>


29. How are you billed for elastic IP addresses?
    1. Hourly when they are associated with an instance
    2. Hourly when they are not associated with an instance
    3. Based on the data that flows through them
    4. Based on the instance type to which they are attached

<details>
<summary>Votes</summary>



</details>

[//]: # "Automatic generated line"
