# Networking

## VPC with a single public subnet

![publicVPC](https://docs.aws.amazon.com/vpc/latest/userguide/images/case-1_updated.png)

The configuration for this network includes the following:
+ A virtual private cloud \(VPC\) with a size /16 IPv4 CIDR block: `10.0.0.0/16`. This provides 65,536 private IPv4 addresses\.
+ A subnet with a size /24 IPv4 CIDR block: `10.0.0.0/24`. This provides 256 private IPv4 addresses\.
+ An internet gateway\. This connects the VPC to the internet and to other AWS services\.
+ An instance with a private IPv4 address in the subnet range, which enables the instance to communicate with other instances in the VPC, and a public IPv4 address which enables the instance to connect to the internet and to be reached from the internet\.
+ A custom route table associated with the subnet\. The route table entries enable instances in the subnet to use IPv4 to communicate with other instances in the VPC, and to communicate directly over the internet\. A subnet that's associated with a route table that has a route to an internet gateway is known as a *public subnet*\.


### Create a VPC

1. Open the Amazon VPC console at [https://console\.aws\.amazon\.com/vpc/](https://console.aws.amazon.com/vpc).

2. In the navigation pane, choose **Your VPCs**, **Create VPC**\.

3. Under **Resources to create**, choose **VPC only**\.

4. Specify the following VPC details\.
   + **Name tag**: Provide a name for your VPC\. Doing so creates a tag with a key of `Name` and the value that you specify\.
   + **IPv4 CIDR block**: Specify an IPv4 CIDR block of `10.0.0.0/16` for your VPC\. The CIDR block size must have a size between /16 and /28\. More information can be found in [RFC 1918](http://www.faqs.org/rfcs/rfc1918.html).

   + **Tenancy**: Choose the default tenancy option for this VPC\.
      + **Default** ensures that EC2 instances launched in this VPC use the EC2 instance tenancy attribute specified when the EC2 instance is launched\.
      + **Dedicated** ensures that EC2 instances launched in this VPC are run on dedicated tenancy instances regardless of the tenancy attribute specified at launch\.

5. Choose **Create VPC**\.


### Create a subnet in your VPC

To add a new subnet to your VPC, you must specify an IPv4 CIDR block for the subnet from the range of your VPC\. You can specify the Availability Zone in which you want the subnet to reside\. You can have multiple subnets in the same Availability Zone\.

1. In the navigation pane, choose **Subnets**\.

2. Choose **Create subnet**\.

3. For **VPC ID**: Choose the VPC for the subnet\.

4. For **Subnet name**, enter a name for your subnet\. Doing so creates a tag with a key of `Name` and the value that you specify\.

5. For **Availability Zone**, you can choose a Zone for your subnet, or leave the default **No Preference** to let AWS choose one for you\.

6. For **IPv4 CIDR block**, enter an IPv4 CIDR block for your subnet\: `10.0.0.0/24`\. 

7. Choose **Create subnet**\.

### Create a custom route table

1. In the navigation pane, choose **Route Tables**\.

2. Choose **Create route table**\.

3. For **Name tag**, enter a name for your route table\.

4. For **VPC**, choose your VPC\.

5. Choose **Create**\.


### Create and attach an internet gateway

After you create an internet gateway, attach it to your VPC\.

**To create an internet gateway and attach it to your VPC**

1. In the navigation pane, choose **Internet Gateways**, and then choose **Create internet gateway**\.

2. Name your internet gateway\.

3. Choose **Create internet gateway**\.

4. Select the internet gateway that you just created, and then choose **Actions, Attach to VPC**\.

5. Select your VPC from the list, and then choose **Attach internet gateway**\.


### Add Internet Gateway as a target in a custom route table

When you create a subnet, we automatically associate it with the main route table for the VPC\. By default, the main route table doesn't contain a route to an internet gateway\. The following procedure uses your custom route table and creates a route that sends traffic destined outside the VPC to the internet gateway, and then associates it with your subnet\.

1. Select the custom route table that you just created\. The details pane displays tabs for working with its routes, associations, and route propagation\.

2. On the **Routes** tab, choose **Edit routes**, **Add route**, and add the following routes as necessary\. Choose **Save changes** when you're done\.
   + For IPv4 traffic, specify `0.0.0.0/0` in the **Destination** box, and select the internet gateway ID in the **Target** list\.

3. On the **Subnet associations** tab, choose **Edit subnet associations**, select the check box for the subnet, and then choose **Save associations**\.


### Test you VPC

Create an EC2 instance within you VPC, connect to it and access the internet. 
