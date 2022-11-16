# Kubernetes Tutorials

## Install Minikube

[Minikube](https://kubernetes.io/docs/tasks/tools/#minikube) is a tool that lets you run Kubernetes locally.

Installation as well as starting a cluster instructions can be found here: https://minikube.sigs.k8s.io/docs/start/


## Install `kubectl`

1. Download the `kubectl` binary from [Kubernetes](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/#install-kubectl-binary-with-curl-on-windows) official site.

2. Put the `kubectl.exe` binary in a directory accessible in your PATH environment variable.

## Start K8S dashboard

Kubernetes Dashboard allows you to get easily acclimated to your new cluster.

1. Execute
```shell
minikube dashboard
```

2. To access the dashboard endpoint, open the printed link with a web browser.

# Kubernetes Tasks

The Kubernetes documentation contains pages that show how to do individual tasks.
During this module we will walk through core tasks. 

https://kubernetes.io/docs/tasks/

## Run a Stateless Application Using a Deployment

Follow:  
https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/

### Further reading and doing

#### Understanding [Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)

Almost every Kubernetes object includes a nested object that govern the object's configuration: the object `spec`.
The `spec` provides a description of the characteristics you want the resource to have: its **desired state**.

In the .yaml file for the Kubernetes object you want to create, you'll need to set values for the following fields:

- `apiVersion` - Which version of the Kubernetes API you're using to create this object.
- `kind` - What kind of object you want to create.
- `metadata` - Data that helps uniquely identify the object, including a name string, UID, and optional namespace.
- `spec` - What state you desire for the object.

**Labels** are key/value pairs that are attached to objects, such as Deployment.
Labels are intended to be used to specify identifying attributes of objects that are meaningful and relevant to users. E.g.:

- `"release" : "stable"`
- `"environment" : "dev"`
- `"tier" : "backend"`

Via a **Label Selector**, the client/user can identify a set of objects. 

#### Deploy your own app

1. Build a simple Flask webserver in a Docker container (can be found in `05_simple_webserver`).
2. Push the image to a **public** container registry (e.g. ERC).
3. Change the `deployment.yaml` manifest according to your image. 
4. Apply your changes.
5. You can use [`kubectl port-forward`](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) command to forward specific pod and port to your local machine, so you can visit the app under the `localhost:<port>` address. This type of connection can be useful for pod debugging and obviously should not be used outside the borders of the development team.
   To do so, perform:

```shell
kubectl port-forward <pod-name> <local-port>:<pod-port> 
```

## Use Port Forwarding to Access Applications in a Cluster

Follow:  
https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/

## Use a Service to Access an Application in the Cluster

Follow:   
https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/

Notes: 

- _Using a service configuration file_ section (use YAML file instead `kubectl expose` command).
- Use `minikube ip` to get the IP of Minikube "node" and visit the app in `http://<NodeIP>:<NodePort>`

![](../docs/img/service-k8s.png)


### Further reading and doing

Services can be exposed in different ways by specifying a `type` in the ServiceSpec. We will review two types:

- `ClusterIP` (default) - Exposes the Service on an internal IP in the cluster. This type makes the Service only reachable from within the cluster.
- `NodePort` - Exposes the Service on some port of each **Node** in the cluster. Makes a Service accessible from outside the cluster using `<NodeIP>:<NodePort>`.

## Assign Memory Resources to Containers and Pods

Follow:  
https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/


## Assign CPU Resources to Containers and Pods

Follow: 
https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/


## Configure Liveness, Readiness and Startup Probes

Follow:  
https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

> The following sections can be skipped:  
> - Define a TCP liveness probe
> - Define a gRPC liveness probe
> - Use a named port
> - Protect slow starting containers with startup probes

## Configure a Pod to Use a Volume for Storage

Follow:  
https://kubernetes.io/docs/tasks/configure-pod-container/configure-volume-storage/

### Further reading and doing

- Familiarize yourself with the material in [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
- [Communicate Between Containers in the Same Pod Using a Shared Volume](https://kubernetes.io/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/)


## Configure a Pod to Use a PersistentVolume for Storage

Follow:  
https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/

## ConfigMap

TBD

## Distribute Credentials Securely Using Secrets

Follow:  
https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#create-a-pod-that-has-access-to-the-secret-data-through-a-volume


## HorizontalPodAutoscaler Walkthrough

Follow:  
https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/

## Run a Single-Instance Stateful Application

Follow:  
https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/

## Running Automated Tasks with a CronJob

Follow:  
https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/


## Helm

Helm is the package manager for Kubernetes.
The main big 3 concepts of helm are:

- A **Chart** is a Helm package. It contains all the resource definitions necessary to run an application, tool, or service inside of a Kubernetes cluster.
- A **Repository** is the place where charts can be collected and shared.
- A **Release** is an instance of a chart running in a Kubernetes cluster.

[Install](https://helm.sh/docs/intro/install/) the Helm cli if you don't have.

### Deploy MySQL using Helm

How relational databases are deployed in real-life applications?

The following diagram shows a Multi-AZ DB cluster.

![](../docs/img/mysql-multi-instance.png)

With a Multi-AZ DB cluster, MySQL replicates data from the writer DB instance to both of the reader DB instances.
When a change is made on the writer DB instance, it's sent to each reader DB instance.
Acknowledgment from at least one reader DB instance is required for a change to be committed.
Reader DB instances act as automatic failover targets and also serve read traffic to increase application read throughput.

Let's review the Helm chart written by Bitnami for MySQL provisioning in k8s cluster.

[https://github.com/bitnami/charts/tree/master/bitnami/mysql/#installing-the-chart](https://github.com/bitnami/charts/tree/master/bitnami/mysql/#installing-the-chart)

1. Add the bitnami Helm repo to your local machine:
```shell
# or update if you have it already: `helm repo update bitnami`
helm repo add bitnami https://charts.bitnami.com/bitnami
```

3. Review `k8s/mysql-helm-values.yaml`, change values or [add parameters](https://github.com/bitnami/charts/tree/master/bitnami/postgresql/#parameters) according to your need.
4. Install the `mysql` chart
```shell
helm upgrade --install -f k8s/mysql-helm-values.yaml mysql bitnami/mysql
```
5. To delete this release:
```shell
helm delete mysql
```
