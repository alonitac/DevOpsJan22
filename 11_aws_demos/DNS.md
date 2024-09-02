# Route 53

## Resolving google.com

We will resolve google.com step by step using the `nslookup` command.

1. First, get the list of the root-level DNS servers by `nslookup -type=NS .`.
2. Pick one of the root-level domain names. We will query this server to get the hostname of the *.com* top-level domain by:
   `nslookup -type=NS com <your-chosen-root-level-hostname>`
3. Now that we have a list of *.com* TLD servers, pick on of them to query the hostname of the authoritative DNS of *google.com*:
   `nslookup -type=NS google.com <your-chosen-TLD-hostname>`
4. Finally, as we know the hostname of the authoritative DNS servers of *google.com*, we can query one of them to retrieve the IP address of *google.com*:
   `nslookup -type=A google.com <your-chosen-authoritative-hostname>`

## Creating a public hosted zone

1. Open the Route 53 console at [https://console\.aws\.amazon\.com/route53/](https://console.aws.amazon.com/route53/).

2. If you're new to Route 53, choose **Get started** under **DNS management**\.

   If you're already using Route 53, choose **Hosted zones** in the navigation pane\.

3. Choose **Create hosted zone**\.

4. In the **Create Hosted Zone** pane, enter the name of the domain that you want to route traffic for\.

5. For **Type**, accept the default value of **Public Hosted Zone**\.

6. Choose **Create**\.

7. Inspired by the above usage of `nslookup` try to query one of the authoritative DNS server created in the hosted zone. 

## Add records to registered domain


1. In the navigation pane, choose **Hosted zones**\.

2. Choose `devops-int-college.com` as the name of the hosted zone that you want to create records in\.

3. Choose **Create record**\.

4. Define an A record for a custom subdomain of yours (e.g. `my-name.devops-int-college.com`), the record value is an IP address on a running EC2 instance. 

5. Choose **Create records**\.
   **Note**  
   Your new records take time to propagate to the Route 53 DNS servers

