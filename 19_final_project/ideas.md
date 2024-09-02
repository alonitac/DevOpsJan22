# Final Project Extension Ideas

### New functionality to the PolyBot (Python extension)

Implement some python module for the app. 

- Get photos from users and store them.
- Allow users to ask `my videos` and send them all their YouTube videos link.
- Compress the videos before the upload to S3.
- Develop some async component (`async/await` form) using [asyncio](https://docs.python.org/3/library/asyncio-task.html).


### DevSecOps 

Embed DevSecOps tool to the CI/CD pipeline:

- [safety](https://pyup.io/safety/) to scan vulnerabilities in Python packages.
- [Bandit](https://bandit.readthedocs.io/en/latest/) to find security issues in your Python code.
- [Pre-commit](https://pre-commit.com/) to enforce some policy before committing a new code.
- [Black](https://github.com/psf/black) as a linting tool.
- [Chef InSpec](https://docs.chef.io/inspec/) to apply security and compliance policies.


### Jenkins

- Implement load testing code for the Bot and run it in the PR testing pipeline.
- Create a [Jenkins shared library](https://www.jenkins.io/blog/2017/02/15/declarative-notifications/#moving-notifications-to-shared-library).
- Send email notifications to users

### AWS

- Expose some API using [API gateway](https://aws.amazon.com/api-gateway/)
- Implement basic user auth with [Cognito](https://aws.amazon.com/cognito/)
- Protect your service using [WAF](https://aws.amazon.com/waf/) or [Shield](https://aws.amazon.com/shield/).
- Any other shiny service that interesting you...

### K8S

- Deploy some interesting Helm Chart in the cluster (Jenkins, RabbitMQ - as an alternative to SQS, OpenVPN client/server).
- Write your app YAMLs as Helm Chart.
- Run some [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) in the cluster.
- Use [ArgoCD](https://argo-cd.readthedocs.io/en/stable/) to deploy your app.
- Implement some interesting [ArgoWF](https://argoproj.github.io/argo-workflows/).
- Experimenting with [Calico](https://projectcalico.docs.tigera.io/about/about-calico) to implement network security in the cluster.
- Experimenting with [Istio](https://istio.io/) to implement a service mesh. 
- Expose your app through a secured HTTPS.
- Implement Pod identity in EKS instead using the EC2 IAM role. 

### Terraform

- Provision the app infrastructure as a code.
- Built a dedicated "IaaC" pipeline in Jenkins 

### Ansible

- Use some [devsec.hardening Ansible](https://github.com/dev-sec/ansible-collection-hardening) collection to harden the system 

### Monitoring 

- Deploy [Prometheus](https://prometheus.io/) in K8S.
- Enable backup/restore to from [ElasticSearch to S3](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-restore.html). 
- Build some Kibana dashboard 
- Improve the logs stream from the k8s cluster to Elasticsearch
- Create some [alerts in Grafana](https://grafana.com/docs/grafana/latest/alerting/) (e.g. high CPU rate, container restarts many times etc...)
