# The Elastic Stack (Elasticsearch, Logstash, Kibana)

Let's get yourself familiar with the ELK stack:

https://www.elastic.co/what-is/elk-stack

## Elasticsearch on K8S

**Note:** this chart should be released once per k8s cluster (the same server will be shared by all students).

https://bitnami.com/stack/elasticsearch/helm

Deploy with the following values:

```yaml
coordinating:
   replicaCount: 0 

ingest:
   enabled: false
   
global:
   kibanaEnabled: true
```

## Kibana setup

Visit Kibana by port-forwarding the service:

```shell
kubectl port-forward svc/<kibana-service> 5601:5601
```

Then go to `https://localhost:5601`.

Open the **Spaces** tooltip, and create your own namespace in which you will practice:

![](../docs/img/elastic-spaces.png)

### Add the sample data

Sample data sets come with sample visualizations, dashboards, and more to help you explore before you ingest or add your own data.

1. On the home page, click *Try sample data*.
2. Click *Other sample data sets*.
3. On the *Sample web logs* card, click *Add data*.

## Kibana Query Language (KQL)

Before we are experimenting with KQL, read the following [important concepts of Kibana](https://www.elastic.co/guide/en/kibana/current/kibana-concepts-analysts.html).

Then, read [the KQL short tutorial](https://www.elastic.co/guide/en/kibana/current/kuery-query.html) from Elastic's official docs.

#### Try it yourself

- Query all response code 200 and 404.
- All successful requests from last day, referred from `twitter.com` 
- All non-successful requests (both by client or server side).


- Create a [Filter](https://www.elastic.co/guide/en/kibana/current/kibana-concepts-analysts.html#autocomplete-suggestions) that displays data when `hour_of_day` value is between the working days (`9-17`). 




