# CI/CD with Jenkins

Due date: 20/11/2022 23:59  


## Deploy k8s cluster (via [k0s](https://k0sproject.io/))

Installing the k8s dashboard is as easy as executing pre-built bash script. 

1. Create an **Amazon Linux** EC2 `micro` instance. This instance will host a Kubernetes "cluster". Open the following ports:
   - `30001` for accessing the k8s dashboard.
   - `6443` to communicate with the k8s API.
   **Note:** the EC2 instance and Jenkins server must be running on the same VPC!
2. Copy the files under `infra/helpers` directory (can be found in the PolyBot repo) to the home directory of your EC2 and execute by `bash init-k0s-cluster-amazon-linux.sh`.
3. The PolyBot app will be running as Docker containers inside the Kubernetes cluster. Thus, your EC2 need the appropriate permissions, i.e. S3, SQS. Especially, it must have read permissions for your ECR registries.
4. Create Kubernetes namespaces for the Development and Production environments. From the EC2 instance execute:
```shell
$ kubectl create namespace dev
>> namespace/dev created

$ kubectl create namespace prod
>> namespace/prod created
```

## Prepare the Jenkins server

Perform the following steps on your existed Jenkins server. 

1. Install the [ECR Credentials helpers](https://github.com/awslabs/amazon-ecr-credential-helper) by:
```shell
sudo amazon-linux-extras enable docker
sudo yum install amazon-ecr-credential-helper
sudo -u jenkins mkdir -p /var/lib/jenkins/.docker
echo '{"credsStore": "ecr-login"}' | sudo -u jenkins tee /var/lib/jenkins/.docker/config.json
```

After you've done it, no need to execute `aws ecr get-login-password...` any more before each push to ECR. This is necessary to run Jenkins agents inside Docker containers.   

2. In your Jenkins, create `dev` and `prod` folders (New Item -> Folder). All the pipelines will be created in those folders, so no fear to overwrite the pipelines we've created in class. 
3. Jenkins needs to talk with the k8s cluster in order to deploy the applications. It does so using the Kubernetes command-line tool, `kubectl`. To configure `kubectl` to work with your k8s cluster, create in Jenkins **Secret file** credentials called `kubeconfig` in the Jenkins global scope (should be available to both `dev` and `prod` folders). The secret file can be found in the EC2 you've installed the k8s cluster under `~/.kube/config`, you can copy & paste this file's content to your local machine and upload to Jenkins.
4. You should create another Telegram bot. One bot will be functioning as a `dev` bot and will be used in Development environment, while the other is a `prod` bot that your customers are using in Production. So 2 bots, 2 tokens.   

**Note:** no need to run agents on different **nodes**! All pipelines can be running on Jenkins server itself.


## The Dev and Prod CI/CD pipelines 

All the code in this exercise is given in TBD. So no need to write any Python.

You are going to implement full CI/CD pipelines for the PolyBot (bot and worker) app in Development and Production environments, using Jenkins. 


Read the following guidelines carefully **before** you start the implementation!

Create the following pipelines in Jenkins and complete the corresponding Jenkinsfiles:

### The `dev` folder pipelines

The following pipelines should be located under `dev` folder:

1. The `botBuild` Pipeline - responsible to build the Bot app. The Jenkinsfile is **partially** implemented under `infra/jenkins/dev/BotBuild.Jenkinsfile`. Complete the `TODO`s.
2. The `botDeploy` Pipeline - responsible to deploy the Bot app. The Jenkinsfile is **completely** implemented under `infra/jenkins/dev/BotDeploy.Jenkinsfile`. Don't change it, only review and make sure you understand **everything**. 
3. The `workerBuild` Pipeline - responsible to build the Worker app. The Jenkinsfile configured under `infra/jenkins/dev/WorkerBuild.Jenkinsfile`. You should implement it.
4. The `workerDeploy` Pipeline - responsible to deploy the Worker app. The Jenkinsfile is **completely** implemented under `infra/jenkins/dev/WorkerDeploy.Jenkinsfile`.
      
#### Notes for `dev` pipelines

5. All `dev` pipelines should be triggered from a Git branch called `dev` **only** (check it out initially from `main`).
6. In Dev env, `botBuild` and `workerBuild` should trigger the `botDeploy` and `workerDeploy` pipelines accordingly **automatically**.
7. trigger only from change to a directory
8. credentials

### The `prod` folder

The following pipelines should be located under `prod` folder:

1. The `botBuild` Pipeline - responsible to build the Bot app. The Jenkinsfile is **partially** implemented under `infra/jenkins/prod/BotBuild.Jenkinsfile`. Complete the `TODO`s.
2. The `botDeploy` Pipeline - responsible to deploy the Bot app. The Jenkinsfile is **completely** implemented under `infra/jenkins/prod/BotDeploy.Jenkinsfile`. Don't change it, only review and make sure you understand **everything**.
3. The `workerBuild` Pipeline - responsible to build the Worker app. The Jenkinsfile configured under `infra/jenkins/prod/WorkerBuild.Jenkinsfile`. You should implement it.
4. The `workerDeploy` Pipeline - responsible to deploy the Worker app. The Jenkinsfile is **completely** implemented under `infra/jenkins/prod/WorkerDeploy.Jenkinsfile`.
5. The `PRTesting` - responsible to execute PR testing. 

#### Important Notes:

6. You should create another Telegram bot. One bot will be functioning as a `dev` bot and will be used in Development environment, while the other is a Production bot that your customers are using. So 2 bots, 2 tokens.
7. All `dev`'s folder pipelines should be triggered from a Git branch called `dev` (check it out initially from `main`).
8. In Prod env, `botBuild` and `workerBuild` should **not** trigger the `botDeploy` and `workerDeploy` pipelines automatically.
9. trigger only from change to a directory
10. credentials

## Experiencing your Pipelines

security scan


# Good Luck

Don't hesitate to ask any questions
