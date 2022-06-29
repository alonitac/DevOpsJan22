# IAM demos

## IAM policies on S3

### Create IAM role with permissions over S3 and attach it to an EC2 instance


1. Open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

2. In the navigation pane, choose **Roles**, **Create role**\.

3. On the **Trusted entity type** page, choose **AWS service** and the **EC2** use case\. Choose **Next: Permissions**\.

4. On the **Attach permissions policy** page, search for **AmazonS3FullAccess** AWS managed policy\.

5. On the **Review** page, enter a name for the role and choose **Create role**\.
6. Attach the role to your EC2 instance. 


### Create a policy to access a certain bucket only and attach it to your IAM role.

1. Open the [IAM console](https://console.aws.amazon.com/iam/).
2. From the console, open the IAM user or role that should have access to only a certain bucket.
3. In the **Permissions** tab, copy the JSON view of **AmazonS3FullAccess** policy and then **remove** it .
4. Click **Add permissions** and **Create inline policy**
5. Paste your copies json in the JSON view of your new policy.
6. Inspired by [policies examples](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html) in AWS IAM docs, try to change the given policy JSON such that it allows the user to list, read, and write objects with a prefix `images/`
7. Save your policy. Remove the **AmazonS3FullAccess** policy from your role.
8. Validate your changes.

### Extend your policy

9. Explore [S3 policy condition key elements](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html).
10. Try to add a condition to your above policy such that only objects in `STANDARD_IA` storage-class can be accessed. 
11. Validate your changes.

### Extend more...

12. In IAM roles console, choose your role.
13. In **Tags** tab, add a tag with the key `BucketPrefix` and some value according to your choice.
14. Instead of allow operation on prefix `images/`, try to allow access on a dynamic prefix according to the principal tag:
```text
"Resource": ["arn:aws:s3:::<your-bucket-name>/${aws:PrincipalTag/BucketPrefix}/*"]
```
