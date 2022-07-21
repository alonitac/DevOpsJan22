# Questions

## EC2

1. You know that you need 24 CPUs for your production server. You also know
   that your compute capacity is going to remain fixed until next year, so you need
   to keep the production server up and running during that time. What pricing
   option would you go with?
    1. Choose the spot instance
    2. Choose the on-demand instance
    3. Choose the three-year reserved instance
    4. Choose the one-year reserved instance
    

2. You are planning to run a database on an EC2 instance. You know that the database
   is pretty heavy on I/O. The DBA told you that you would need a minimum of
   8,000 IOPS. What is the storage option you should choose?
    1. EBS volume with magnetic hard drive
    2. Store all the data files in the ephemeral storage of the server
    3. EBS volume with provisioned IOPS
    4. EBS volume with general-purpose SSD


3. You are running your application on a bunch of on-demand servers. On weekends
   you have to kick off a large batch job, and you are planning to add capacity. The
   batch job you are going to run over the weekend can be restarted if it fails. What is
   the best way to secure additional compute resources?
    1. Use the spot instance to add compute for the weekend
    2. Use the on-demand instance to add compute for the weekend
    3. Use the on-demand instance plus PIOPS storage for the weekend resource
    4. Use the on-demand instance plus a general-purpose EBS volume for the weekend resource


4. You have a compliance requirement that you should own the entire physical
   hardware and no other customer should run any other instance on the physical
   hardware. What option should you choose?
    1. Put the hardware inside the VPC so that no other customer can use it
    2. Use a dedicated instance
    3. Reserve the EC2 for one year
    4. Reserve the EC2 for three years


5. You have created an instance in EC2, and you want to connect to it. What should
   you do to log in to the system for the first time?
    1. Use the username/password combination to log in to the server
    2. Use the key-pair combination (private and public keys)
    3. Use your cell phone to get a text message for secure login
    4. Log in via the root user


6. What are the characteristics of AMI that are backed up by the instance store?
   (Choose two.)
    1. The data persists even after the instance reboot.
    2. The data is lost when the instance is shut down.
    3. The data persists when the instance is shut down.
    4. The data persists when the instance is terminated.


7. How can you make a cluster of an EC2 instance?
    1. By creating all the instances within a VPC
    2. By creating all the instances in a public subnet
    3. By creating all the instances in a private subnet
    4. By creating a placement group


8. You need to take a snapshot of the EBS volume. How long will the EBS remain
   unavailable?
    1. The volume will be available immediately.
    2. EBS magnetic drive will take more time than SSD volumes.
    3. It depends on the size of the EBS volume.
    4. It depends on the actual data stored in the EBS volume.


9. What are the different ways of making an EC2 server available to the public?
    1. Create it inside a public subnet
    2. Create it inside a private subnet and assign a NAT device
    3. Attach an IPv6 IP address
    4. Allocate that with a load balancer and expose the load balancer to the public


10. The application workload changes constantly, and to meet that, you keep on
    changing the hardware type for the application server. Because of this, you
    constantly need to update the web server with the new IP address. How can
    you fix this problem?
    1. Add a load balancer
    2. Add an IPv6 IP address
    3. Add an EIP to it
    4. Use a reserved EC2 instance


11. Your web application needs four instances to support steady traffic nearly all of the time. On the last
    day of each month, the traffic triples. What is a cost-effective way to handle this traffic pattern?
    1. Run 12 Reserved Instances all of the time.
    2. Run four On-Demand Instances constantly, then add eight more On-Demand Instances on the last day of each month.
    3. Run four Reserved Instances constantly, then add eight On-Demand Instances on the last day of each month.
    4. Run four On-Demand Instances constantly, then add eight Reserved Instances on the last day of each month.


12. Your order-processing application processes orders extracted from a queue with two Reserved
    Instances processing 10 orders/minute. If an order fails during processing, then it is returned to the
    queue without penalty. Due to a weekend sale, the queues have several hundred orders backed up.
    While the backup is not catastrophic, you would like to drain it so that customers get their
    confirmation emails faster. What is a cost-effective way to drain the queue for orders?
    1. Create more queues.
    2. Deploy additional Spot Instances to assist in processing the orders.
    3. Deploy additional Reserved Instances to assist in processing the orders.
    4. Deploy additional On-Demand Instances to assist in processing the orders.


13. Which of the following must be specified when launching a new Amazon Elastic Compute Cloud
    (Amazon EC2) Windows instance? (Choose 2 answers)
    1. The Amazon EC2 instance ID
    2. Password for the administrator account
    3. Amazon EC2 instance type
    4. Amazon Machine Image (AMI)


14. You have purchased an m3.xlarge Linux Reserved instance in us-east-1a. In which ways can you
    modify this reservation? (Choose 2 answers)
    1. Change it into two m3.large instances.
    2. Change it to a Windows instance.
    3. Move it to us-east-1b.
    4. Change it to an m4.xlarge.


15. Your instance is associated with two security groups. The first allows Remote Desktop Protocol
    (RDP) access over port 3389 from Classless Inter-Domain Routing (CIDR) block 72.14.0.0/16. The
    second allows HTTP access over port 80 from CIDR block 0.0.0.0/0. What traffic can reach your
    instance?
    1. RDP and HTTP access from CIDR block 0.0.0.0/0
    2. No traffic is allowed.
    3. RDP and HTTP traffic from 72.14.0.0/16
    4. RDP traffic over port 3389 from 72.14.0.0/16 and HTTP traffic over port 80 from 0.0.00/0


16. Which of the following are features of enhanced networking? (Choose 3 answers)
    1. More Packets Per Second (PPS)
    2. Lower latency
    3. Multiple network interfaces
    4. Border Gateway Protocol (BGP) routing
    5. Less jitter


17. You are creating a High-Performance Computing (HPC) cluster and need very low latency and high
    bandwidth between instances. What combination of the following will allow this? (Choose 3
    answers)
    1. Use an instance type with 10 Gbps network performance.
    2. Put the instances in a placement group.
    3. Use Dedicated Instances.
    4. Enable enhanced networking on the instances.
    5. Use Reserved Instances.


18. Which Amazon Elastic Compute Cloud (Amazon EC2) feature ensures that your instances will not
    share a physical host with instances from any other AWS customer?
    1. Amazon Virtual Private Cloud (VPC)
    2. Placement groups
    3. Dedicated Instances
    4. Reserved Instances


19. Which of the following are true of instance stores? (Choose 2 answers)
    1. Automatic backups
    2. Data is lost when the instance stops.
    3. Very high IOPS
    4. Charge is based on the total amount of storage provisioned.


20. Which of the following are features of Amazon Elastic Block Store (Amazon EBS)? (Choose 2
    answers)
    1. Data stored on Amazon EBS is automatically replicated within an Availability Zone.
    2. Amazon EBS data is automatically backed up to tape.
    3. Amazon EBS volumes can be encrypted transparently to workloads on the attached instance.
    4. Data on an Amazon EBS volume is lost when the attached instance is stopped.


21. You are restoring an Amazon Elastic Block Store (Amazon EBS) volume from a snapshot. How long
    will it be before the data is available?
    1. It depends on the provisioned size of the volume.
    2. The data will be available immediately.
    3. It depends on the amount of data stored on the volume.
    4. It depends on whether the attached instance is an Amazon EBS-optimized instance.


22. You have a workload that requires 15,000 consistent IOPS for data that must be durable. What
    combination of the following steps do you need? (Choose 2 answers)
    1. Use an Amazon Elastic Block Store (Amazon EBS)-optimized instance.
    2. Use an instance store.
    3. Use a Provisioned IOPS SSD volume.
    4. Use a magnetic volume.


23. Which of the following can be accomplished through bootstrapping?
    1. Install the most current security updates.
    2. Install the current version of the application.
    3. Configure Operating System (OS) services.
    4. All of the above.


24. How can you connect to a new Linux instance using SSH?
    1. Decrypt the root password.
    2. Using a certificate
    3. Using the private half of the instance’s key pair
    4. Using Multi-Factor Authentication (MFA)


25. VM Import/Export can import existing virtual machines as:
    1. Amazon Elastic Block Store (Amazon EBS) volumes
    2. Amazon Elastic Compute Cloud (Amazon EC2) instances
    3. Amazon Machine Images (AMIs)
    4. Security groups


26. Which of the following can be used to address an Amazon Elastic Compute Cloud (Amazon EC2)
    instance over the web? (Choose 2 answers)
    1. Windows machine name
    2. Public DNS name
    3. Amazon EC2 instance ID
    4. Elastic IP address


27. Using the correctly decrypted Administrator password and RDP, you cannot log in to a Windows
    instance you just launched. Which of the following is a possible reason?
    1. There is no security group rule that allows RDP access over port 3389 from your IP address.
    2. The instance is a Reserved Instance.
    3. The instance is not using enhanced networking.
    4. The instance is not an Amazon EBS-optimized instance.


28. You have a workload that requires 1 TB of durable block storage at 1,500 IOPS during normal use.
    Every night there is an Extract, Transform, Load (ETL) task that requires 3,000 IOPS for 15 minutes.
    What is the most appropriate volume type for this workload?
    1. Use a Provisioned IOPS SSD volume at 3,000 IOPS.
    2. Use an instance store.
    3. Use a general-purpose SSD volume.
    4. Use a magnetic volume.


29. How are you billed for elastic IP addresses?
    1. Hourly when they are associated with an instance
    2. Hourly when they are not associated with an instance
    3. Based on the data that flows through them
    4. Based on the instance type to which they are attached


## S3


1. In what ways does Amazon Simple Storage Service (Amazon S3) object storage differ from block
   and file storage? (Choose 2 answers)
   A. Amazon S3 stores data in fixed size blocks.
   B. Objects are identified by a numbered address.
   C. Objects can be any size.
   D. Objects contain both data and metadata.
   E. Objects are stored in buckets.

   
2. Which of the following are not appropriates use cases for Amazon Simple Storage Service (Amazon
   S3)? (Choose 2 answers)
   A. Storing web content
   B. Storing a file system mounted to an Amazon Elastic Compute Cloud (Amazon EC2) instance
   C. Storing backups for a relational database
   D. Primary storage for a database
   E. Storing logs for analytics


3. What are some of the key characteristics of Amazon Simple Storage Service (Amazon S3)? (Choose
   3 answers)
   A. All objects have a URL.
   B. Amazon S3 can store unlimited amounts of data.
   C. Objects are world-readable by default.
   D. Amazon S3 uses a REST (Representational State Transfer) Application Program Interface (API).
   E. You must pre-allocate the storage in a bucket.


4. Which features can be used to restrict access to Amazon Simple Storage Service (Amazon S3) data?
   (Choose 3 answers)
   A. Enable static website hosting on the bucket.
   B. Create a pre-signed URL for an object.
   C. Use an Amazon S3 Access Control List (ACL) on a bucket or object.
   D. Use a lifecycle policy.
   E. Use an Amazon S3 bucket policy.


5. Your application stores critical data in Amazon Simple Storage Service (Amazon S3), which must
   be protected against inadvertent or intentional deletion. How can this data be protected? (Choose 2
   answers)
   A. Use cross-region replication to copy data to another bucket automatically.
   B. Set a vault lock.
   C. Enable versioning on the bucket.
   D. Use a lifecycle policy to migrate data to Amazon Glacier.
   E. Enable MFA Delete on the bucket.


6. Your company stores documents in Amazon Simple Storage Service (Amazon S3), but it wants to
   minimize cost. Most documents are used actively for only about a month, then much less frequently.
   However, all data needs to be available within minutes when requested. How can you meet these
   requirements?
   A. Migrate the data to Amazon S3 Reduced Redundancy Storage (RRS) after 30 days.
   B. Migrate the data to Amazon Glacier after 30 days.
   C. Migrate the data to Amazon S3 Standard – Infrequent Access (IA) after 30 days.
   D. Turn on versioning, then migrate the older version to Amazon Glacier.


7. How is data stored in Amazon Simple Storage Service (Amazon S3) for high durability?
   A. Data is automatically replicated to other regions.
   B. Data is automatically replicated within a region.
   C. Data is replicated only if versioning is enabled on the bucket.
   D. Data is automatically backed up on tape and restored if needed.


8. Based on the following Amazon Simple Storage Service (Amazon S3) URL, which one of the
   following statements is correct? https://bucket1.abc.com.s3.amazonaws.com/folderx/myfile.doc
   A. The object “myfile.doc” is stored in the folder “folderx” in the bucket “bucket1.abc.com.”
   B. The object “myfile.doc” is stored in the bucket “bucket1.abc.com.”
   C. The object “folderx/myfile.doc” is stored in the bucket “bucket1.abc.com.”
   D. The object “myfile.doc” is stored in the bucket “bucket1.”


9. To have a record of who accessed your Amazon Simple Storage Service (Amazon S3) data and from
    where, you should do what?
    A. Enable versioning on the bucket.
    B. Enable website hosting on the bucket.
    C. Enable server access logs on the bucket.
    D. Create an AWS Identity and Access Management (IAM) bucket policy.
    E. Enable Amazon CloudWatch logs.


10. What are some reasons to enable cross-region replication on an Amazon Simple Storage Service
    (Amazon S3) bucket? (Choose 2 answers)
    A. You want a backup of your data in case of accidental deletion.
    B. You have a set of users or customers who can access the second bucket with lower latency.
    C. For compliance reasons, you need to store data in a location at least 300 miles away from the first region.
    D. Your data needs at least five nines of durability.


11. Your company requires that all data sent to external storage be encrypted before being sent. Which
    Amazon Simple Storage Service (Amazon S3) encryption solution will meet this requirement?
    A. Server-Side Encryption (SSE) with AWS-managed keys (SSE-S3)
    B. SSE with customer-provided keys (SSE-C)
    C. Client-side encryption with customer-managed keys
    D. Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS)


12. What is needed before you can enable cross-region replication on an Amazon Simple Storage
    Service (Amazon S3) bucket? (Choose 2 answers)
    A. Enable versioning on the bucket.
    B. Enable a lifecycle rule to migrate data to the second region.
    C. Enable static website hosting.
    D. Create an AWS Identity and Access Management (IAM) policy to allow Amazon S3 to replicate objects on your behalf.


13. Your company has 100TB of financial records that need to be stored for seven years by law.
    Experience has shown that any record more than one-year old is unlikely to be accessed. Which of
    the following storage plans meets these needs in the most cost efficient manner?
    A. Store the data on Amazon Elastic Block Store (Amazon EBS) volumes attached to t2.micro instances.
    B. Store the data on Amazon Simple Storage Service (Amazon S3) with lifecycle policies that change the storage class to Amazon Glacier after one year and delete the object after seven years.
    C. Store the data in Amazon DynamoDB and run daily script to delete data older than seven years.
    D. Store the data in Amazon Elastic MapReduce (Amazon EMR).


14. Amazon Simple Storage Service (S3) bucket policies can restrict access to an Amazon S3 bucket
    and objects by which of the following? (Choose 3 answers)
    A. Company name
    B. IP address range
    C. AWS account
    D. Country of origin
    E. Objects with a specific prefix


15. What must be done to host a static website in an Amazon Simple Storage Service (Amazon S3)
    bucket? (Choose 3 answers)
    A. Configure the bucket for static hosting and specify an index and error document.
    B. Create a bucket with the same name as the website.
    C. Enable File Transfer Protocol (FTP) on the bucket.
    D. Make the objects in the bucket world-readable.
    E. Enable HTTP on the bucket.


16. You have valuable media files hosted on AWS and want them to be served only to authenticated
    users of your web application. You are concerned that your content could be stolen and distributed
    for free. How can you protect your content?
    A. Use static web hosting.
    B. Generate pre-signed URLs for content in the web application.
    C. Use AWS Identity and Access Management (IAM) policies to restrict access.
    D. Use logging to track your content.


17. Amazon Glacier is well-suited to data that is which of the following? (Choose 2 answers)
    A. Is infrequently or rarely accessed
    B. Must be immediately available when needed
    C. Is available after a three- to five-hour restore period
    D. Is frequently erased within 30 days


18. What is the best way to protect a file in Amazon S3 against accidental delete?
    A. Upload the files in multiple buckets so that you can restore from another when a file is deleted
    B. Back up the files regularly to a different bucket or in a different region
    C. Enable versioning on the S3 bucket
    D. Use MFA for deletion
    E. Use cross-region replication


19. Amazon S3 provides 99.999999999 percent durability. Which of the following
   are true statements? (Choose all that apply.)
   A. The data is mirrored across multiple AZs within a region.
   B. The data is mirrored across multiple regions to provide the durability SLA.
   C. The data in Amazon S3 Standard is designed to handle the concurrent loss of two facilities.
   D. The data is regularly backed up to AWS Snowball to provide the durability SLA.
   E. The data is automatically mirrored to Amazon Glacier to achieve high availability.


20. To set up a cross-region replication, what statements are true? (Choose all
   that apply.)
   A. The source and target bucket should be in a same region.
   B. The source and target bucket should be in different region.
   C. You must choose different storage classes across different regions.
   D. You need to enable versioning and must have an IAM policy in place to replicate.
   E. You must have at least ten files in a bucket.


21. You want to move all the files older than a month to S3 IA. What is the best way
   of doing this?
   A. Copy all the files using the S3 copy command
   B. Set up a lifecycle rule to move all the files to S3 IA after a month
   C. Download the files after a month and re-upload them to another S3 bucket with IA
   D. Copy all the files to Amazon Glacier and from Amazon Glacier copy them to S3 IA


22. What are the various way you can control access to the data stored in S3?
   (Choose all that apply.)
   A. By using IAM policy
   B. By creating ACLs
   C. By encrypting the files in a bucket
   D. By making all the files public
   E. By creating a separate folder for the secure files


23. How much data can you store on S3?
   A. 1 petabyte per account
   B. 1 exabyte per account
   C. 1 petabyte per region
   D. 1 exabyte per region
   E. Unlimited


24. What is the best way to delete multiple objects from S3?
   A. Delete the files manually using a console
   B. Use multi-object delete
   C. Create a policy to delete multiple files
   D. Delete all the S3 buckets to delete the files


25. I shut down my EC2 instance, and when I started it, I lost all my data. What
    could be the reason for this?
    A. The data was stored in the local instance store.
    B. The data was stored in EBS but was not backed up to S3.
    C. I used an HDD-backed EBS volume instead of an SSD-backed EBS volume.
    D. I forgot to take a snapshot of the instance store.


26. I am running an Oracle database that is very I/O intense. My database administrator
    needs a minimum of 3,600 IOPS. If my system is not able to meet that number, my
    application won’t perform optimally. How can I make sure my application always
    performs optimally?
    A. Use Elastic File System since it automatically handles the performance
    B. Use Provisioned IOPS SSD to meet the IOPS number
    C. Use your database files in an SSD-based EBS volume and your other files in an HDD-based EBS volume
    D. Use a general-purpose SSD under a terabyte that has a burst capability


27. Your application needs a shared file system that can be accessed from multiple
    EC2 instances across different AZs. How would you provision it?
    A. Mount the EBS volume across multiple EC2 instances
    B. Use an EFS instance and mount the EFS across multiple EC2 instances across
    multiple AZs
    C. Access S3 from multiple EC2 instances
    D. Use EBS with Provisioned IOPS


28. You want to run a mapreduce job (a part of the big data workload) for a noncritical
    task. Your main goal is to process it in the most cost-effective way. The task is
    throughput sensitive but not at all mission critical and can take a longer time.
    Which type of storage would you choose?
    A. Throughput Optimized HDD (st1)
    B. Cold HDD (sc1)
    C. General-Purpose SSD (gp2)
    D. Provisioned IOPS (io1)



## IAM 



1. Which of the following methods will allow an application using an AWS SDK to be authenticated as
   a principal to access AWS Cloud services? (Choose 2 answers)
    1. Create an IAM user and store the username and password for the user in the application’s configuration.
    2. Create an IAM user and store both parts of the access key for the user in the application’s configuration.
    3. Run the application on an Amazon EC2 instance with an assigned IAM role.
    4. Make all the API calls over an SSL connection.


2. Which of the following are found in an IAM policy? (Choose 2 answers)
    1. Service Name
    2. Region
    3. Action
    4. Password


3. Your AWS account administrator left your company today. The administrator had access to the root
   user and a personal IAM administrator account. With these accounts, he generated other IAM
   accounts and keys. Which of the following should you do today to protect your AWS infrastructure?
   (Choose 3 answers)
    1. Change the password and add MFA to the root user.
    2. Put an IP restriction on the root user.
    3. Rotate keys and change passwords for IAM accounts.
    4. Delete all IAM accounts.
    5. Delete the administrator’s personal IAM account.
    6. Relaunch all Amazon EC2 instances with new roles.


4. Which of the following actions can be authorized by IAM? (Choose 2 answers)
    1. Installing ASP.NET on a Windows Server
    2. Launching an Amazon Linux EC2 instance
    3. Querying an Oracle database
    4. Adding a message to an Amazon Simple Queue Service (Amazon SQS) queue


5. Which of the following are IAM security features? (Choose 2 answers)
    1. Password policies
    2. Amazon DynamoDB global secondary indexes
    3. MFA
    4. Consolidated Billing


6. Which of the following are benefits of using Amazon EC2 roles? (Choose 2 answers)
    1. No policies are required.
    2. Credentials do not need to be stored on the Amazon EC2 instance.
    3. Key rotation is not necessary.
    4. Integration with Active Directory is automatic.


7. Which of the following are based on temporary security tokens? (Choose 2 answers)
    1. Amazon EC2 roles
    2. MFA
    3. Root user
    4. Federation


8. Your security team is very concerned about the vulnerability of the IAM administrator user accounts
   (the accounts used to configure all IAM features and accounts). What steps can be taken to lock
   down these accounts? (Choose 3 answers)
    1. Add multi-factor authentication (MFA) to the accounts.
    2. Limit logins to a particular U.S. state.
    3. Implement a password policy on the AWS account.
    4. Apply a source IP address condition to the policy that only grants permissions when the user is on the corporate network.
    5. Add a CAPTCHA test to the accounts.


9. You want to grant the individuals on your network team the ability to fully manipulate Amazon EC2
   instances. Which of the following accomplish this goal? (Choose 2 answers)
    1. Create a new policy allowing EC2:* actions, and name the policy NetworkTeam.
    2. Assign the managed policy, EC2FullAccess, to a group named NetworkTeam, and assign all the team members’ IAM user accounts to that group.
    3. Create a new policy that grants EC2:* actions on all resources, and assign that policy to each individual’s IAM user account on the network team.
    4. Create a NetworkTeam IAM group, and have each team member log in to the AWS Management Console using the user name/password for the group.



10. What is the format of an IAM policy?
    1. XML
    2. Key/value pairs
    3. JSON
    4. Tab-delimited text


11. Can you add an IAM role to an IAM group?
    1. Yes
    2. No
    3. Yes, if there are ten members in the group
    4. Yes, if the group allows adding a role

12. What happens if you delete an IAM role that is associated with a running EC2
    instance?
    1. Any application running on the instance that is using the role will be denied access immediately.
    2. The application continues to use that role until the EC2 server is shut down.
    3. The application will have the access until the session is alive.
    4. The application will continue to have access.


15. For implementing security features, which of the following would you choose?
    1. Username/password
    2. MFA
    3. Using multiple S3 buckets
    4. Login using the root user


16. You want EC2 instances to give access without any username or password to S3
    buckets. What is the easiest way of doing this?
    1. By using a VPC S3 endpoint
    2. By using a signed URL
    3. By using roles
    4. By sharing the keys between S3 and EC2


17. Using the shared security model, the customer is responsible for which of the
    following? (Choose two.)
    1. The security of the data running inside the database hosted in EC2
    2. Maintaining the physical security of the data center
    3. Making sure the hypervisor is patched correctly
    4. Making sure the operating system is patched correctly

