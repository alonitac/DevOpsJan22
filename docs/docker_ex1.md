# Docker network performance analysis

# Background

Docker's networking subsystem is pluggable, using drivers. Several drivers
exist by default, and provide core networking functionality:

- `bridge`: The default network driver. If you don't specify a driver, this is
  the type of network you are creating. **Bridge networks are usually used when
  your applications run in standalone containers that need to communicate.** See
  [bridge networks](https://docs.docker.com/network/bridge/).

- `host`: For standalone containers, remove network isolation between the
  container and the Docker host, and use the host's networking directly. See
  [use the host network](https://docs.docker.com/network/host/).

Your goal in this exercise is to measure the network performance of each network driver, and compare results.

## Preliminaries

1. Checkout a new Git branch `docker_ex1/<alias>` (change `<alias>` to your name). At the end, commit and push your results in this branch.
2. Create an **Ubuntu AMI** ec2 instance. Connect to your instance.
3. [Install docker](https://docs.docker.com/engine/install/ubuntu/).
4. Install [qperf](https://linux.die.net/man/1/qperf) networking tool:
   ```shell
   sudo apt-get update -y 
   sudo apt-get install qperf -y 
   ```

## Test network bandwidth and latency 

We will utilize qperf tool to measure bandwidth and latency. The test is fairly simple. You start
a server by `qperf` and invoke a client which will talk with the server and record the results: `qperf <server-ip> tcp_bw tcp_lat`

### Test Server and Client on the same physical machine. 

#### Test performance without Docker

4. Start the qperf server by simply: 
```shell
qpref
````
5. Open another ssh session to the same instance where the server is running, perform:
```shell
qperf 127.0.0.1 tcp_bw tcp_lat conf
```
This command will perform a single network test, and will print results to stdout. 

6. Use the following bash script template to perform the test multiple times and average results.
   ```shell
   AVG=0
   ITERATIONS=20
   for i in $( seq 0 $ITERATIONS ); do 
      CURRENT_TEST_RES=$(qperf 127.0.0.1 tcp_lat | tail -n 1 | awk '{ print $3 }')
      AVG=$(awk "BEGIN{ print $AVG + $CURRENT_TEST_RES }")
   done
   awk "BEGIN{ print $AVG / $ITERATIONS }"
   ```
   The above script perform only the latency test. Change `tcp_lat` (latency test) to `tcp_bw` (bandwidth) to perform the bandwidth test.


#### Test performance with Docker Bridge network

Now the Server will reside in a docker container using the **default Bridge network**, while the client will stay on the host machine. 

1. [pedroperezmsft/qperf](https://hub.docker.com/r/pedroperezmsft/qperf/) is pre-built docker image with qperf tool installed. Run it by:
   ```shell
   docker run --rm --name qp_server -p 19765:19765 pedroperezmsft/qperf 
   ```
   Note that the default port of the qperf server is 19765.
2. Use `docker inspect` command to get the IPAddress of the running container. 
3. Repeat the same test as described above. Don't forget to change the server ip from `127.0.0.1` to your container ip. 

#### Test performance with Docker Host network

Repeat the same test while the server will reside in a Docker container using **Host network**.


Summarize your results in the appropriate table in `12_docker_network_analysis_ex/README.md` file.

### Test Server and Client on different machines

Repeat the above experiment, but now the client and server will reside in a different physical machines, on the **same AWS region**, but in **different AZ**. In order to do that, you need to create another Ubuntu EC2 instance, and run the client from it (open relevant ports in the instance's security group).
Summarize your results in the appropriate table in the README file. 


## Conclusions

According to your experiment results, conclude the % overhead of Docker Bridge and Host networks comparing the network performance of the original machine. 
Write your conclusions separately for client-server communication on the same physical machine, and for client-server in different machines. 



# Good Luck

Don't hesitate to ask any questions