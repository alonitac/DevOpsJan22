# AWS demos

## Create a Bucket

### TL;DR

1. Create SSE-S3 encrypted bucket in the same region of your EC2 instance.
2. Connect to your instance over SSH, use [aws s3api put-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-object.html) command to upload an object to your bucket.
3. Repeat the same with SSE-KMS encrypted bucket.
4. Follow [this](https://aws.amazon.com/premiumsupport/knowledge-center/s3-console-access-certain-bucket/) aws blog to allow your instance to access a certain bucket only. 
5. Update you IAM policy to access only a certain "folder" in your bucket. 

--- 

### Create a Bucket

1. In S3, Choose **Create bucket**.

   The **Create bucket** wizard opens.

2. In **Bucket name**, enter a DNS-compliant name for your bucket.

   The bucket name must:
    + Be unique across all of Amazon S3.
    + Be between 3 and 63 characters long.
    + Not contain uppercase characters.
    + Start with a lowercase letter or number.

3. In **Region**, choose the AWS Region where you want the bucket to reside.

   Choose the Region where you provisioned your EC2 instance.

4. Under **Object Ownership**, leave ACLs disabled.

5. Enable Default encryption with SSE-S3 encryption type.

6. Choose **Create bucket**.

You've created a bucket in Amazon S3.

### Upload an object to S3 bucket from an EC2 instance

Disclaimer: This is not going to work. Your EC2 instance has to have permissions to operate in S3.

1. Connect to your instance over SSH.
2. Read the [examples](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-object.html#examples) in AWS code and write a command to upload (put-object) in your S3 bucket.
3. Got `Unable to locate credentials.` or `Access Denied`? follow the next section...

### Attach IAM role to your EC2 Instance with permissions over S3

You must create an IAM role before you can launch an instance with that role or attach it to an instance\.

**To create an IAM role using the IAM console**

1. Open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. In the navigation pane, choose **Roles**, **Create role**\.

1. On the **Trusted entity type** page, choose **AWS service** and the **EC2** use case\. Choose **Next: Permissions**\.

1. On the **Attach permissions policy** page, search for **AmazonS3FullAccess** AWS managed policy\.

1. On the **Review** page, enter a name for the role and choose **Create role**\.


**To replace an IAM role for an instance**

1. In EC2 navigation pane, choose **Instances**.

1. Select the instance, choose **Actions**, **Security**, **Modify IAM role**.

1. Choose your created IAM role, click **Save**.


### Create a policy to access a certain bucket only and attach it to your IAM role.

1. Open the [IAM console](https://console.aws.amazon.com/iam/).
2. From the console, open the IAM user or role that should have access to only a certain bucket.
3. In the **Permissions** tab, copy the JSON view of **AmazonS3FullAccess** policy and then **remove** it . 
4. Click **Add permissions** and **Create inline policy**
5. Paste your copies json in the JSON view of your new policy.
6. Change `"Resource": "*"` line to `"Resource": "arn:aws:s3:::<bucket name>/*"` while `<bucket name>` is you bucket you want your instance to have permissions on. 
7. Save your policy. Validate that your changes. 