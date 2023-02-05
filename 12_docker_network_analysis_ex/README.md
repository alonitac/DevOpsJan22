
# Results summary for server and client on the same physical instance

| Network       | Latency avg | Bandwidth avg |
|---|-------------|---------------|
| Original      | 8.6925      | 2.365 GB/s    |
| Docker Bridge | 9.904       | 2.575 GB/s    |
| Docker Host   | 8.9885      | 2.243 GB/s    |


# Results summary for server and client on different physical instance

| Network       | Latency avg | Bandwidth avg |
|---|-------------|---------------|
| Original      | 434.3       | 121.6  MB/s   |
| Docker Bridge | 431.9       | 116.65 MB/s   |
| Docker Host   | 430.45      | 127.9  MB/s   |



# Conclusions

while the averages between running the test on docker or without are not significant, running the test on a different machine(instance) will always cause network bottleneck and 
increased latency, even for machines within the same region.

tested with the following instance as main instance with docker:
https://eu-central-1.console.aws.amazon.com/ec2/v2/home?region=eu-central-1#InstanceDetails:instanceId=i-0c0d10257ed4c588c
"client" instance:
https://eu-central-1.console.aws.amazon.com/ec2/v2/home?region=eu-central-1#InstanceDetails:instanceId=i-04eaefd0b60a4e33e