# CI/CD with Jenkins

Due date: 20/11/2022 23:59  


## Deploy k8s cluster (via [k0s](https://k0sproject.io/))

Installing the k8s dashboard is as easy as executing pre-built bash script. 

1. Create an **Amazon Linux** EC2 `micro` instance. This instance will host a Kubernetes "cluster". Open the following ports:
   - `30001` for accessing the k8s dashboard.
   - `6443` to communicate with the k8s API.    
   **Note:** since Jenkins will communicate with k0s using the EC2 instance's private IP, they both have to reside in the same VPC!
2. Copy the files under `18_jenkins_ex1/k8s_helpers` directory (can be found in our shared repo) to the home directory of your EC2 and execute them by `bash init-k0s-cluster-amazon-linux.sh`.
3. Keep the dashboard url, and the login token printed on screen. We will use them later on.
4. The PolyBot app will be running as Docker containers inside the Kubernetes cluster. Thus, your EC2 instance in which the k8s cluster is running needs the appropriate permissions, i.e. S3, SQS, etc... Specifically, it must have read permissions for your ECR registries.
5. After a successful installation of the k8s cluster (you can re-run `init-k0s-cluster-amazon-linux.sh` when something is getting wrong), from the EC2 terminal, create Kubernetes namespaces for the Development and Production environments:
```shell
$ kubectl create namespace dev
>> namespace/dev created

$ kubectl create namespace prod
>> namespace/prod created
```

## Prepare the Jenkins server

Perform the following steps on your existed Jenkins server. 

1. Install the [ECR Credentials helper](https://github.com/awslabs/amazon-ecr-credential-helper) by:
```shell
sudo amazon-linux-extras enable docker
sudo yum install amazon-ecr-credential-helper
sudo -u jenkins mkdir -p /var/lib/jenkins/.docker
echo '{"credsStore": "ecr-login"}' | sudo -u jenkins tee /var/lib/jenkins/.docker/config.json
```

After you've done it, no need any more to authenticate in ECR (`aws ecr get-login-password...`) before each pull/push. This is a necessary step in order to run Jenkins agents inside Docker containers.   

2. In your Jenkins server, create `dev` and `prod` folders (New Item -> Folder). All the pipelines will be created in those folders, so no fear to overwrite the pipelines we've created in class. 
3. Jenkins needs to talk with the k8s cluster in order to deploy the applications. It does so using the Kubernetes command-line tool, `kubectl`. To configure `kubectl` to work with your k8s cluster, create in Jenkins **Secret file** credentials called `kubeconfig` in the Jenkins global scope (should be available to both `dev` and `prod` folders). The secret file itself can be found in the EC2 you've installed the k8s cluster under `~/.kube/config`. You can copy & paste this file's content to your local machine and upload to Jenkins.
4. You should create another Telegram bot. One bot will be functioning as a `dev` bot and will be used in Development environment, while the other is a `prod` bot that your customers are using in Production. So 2 bots, 2 tokens.   
5. Create a **Secret text** credentials called `telegram-bot-token` in each folder - `dev` and `prod`. Each credential contains the corresponding Telegram token (e.g. for dev folder creds, go to Dashboard -> dev -> Credentials -> dev store -> Global credentials -> Add Credentials).
6. All pipelines are running on a containerized agent (the same Docker image for all pipelines). The agent's Dockerfile can be found under `infra/jenkins/JenkinsAgent.Dockerfile`. You should build it, push in to an ECR registry, and replace `<jenkins-agent-image>` with your Docker image URI in each Jenkinsfile.

**Note:** no need to run agents on different **nodes**! All pipelines can be running on the Jenkins server itself.


## The Dev and Prod CI/CD pipelines 

All the code in this exercise is already given to you in the [PolyBot repo](https://github.com/alonitac/PolyBot), `main` branch. So no need to write any Python.
Throughout this exercise we will be working with branches `dev` and `main` which representing Development and Production environments accordingly. The app is the old good PolyBot (excluding the autoscaling functionality).
If you are using branch `main` or `dev` for your personal PolyBot implementation, checkout it to another branch for now, so you'll have a backup of your version, and use `main` and `dev` for this exercise. Alternatively, you can work on a new clean fork (a separate repo). Later on, after you are comfortable with the new project structure, you can migrate your code into the bare PolyBot implementation you are given. 

You are going to implement full CI/CD pipelines for the PolyBot (bot and worker) app in Development and Production environments, using Jenkins. 

Read the following guidelines carefully **before** you start the implementation! 
Create the following pipelines in Jenkins and complete the corresponding Jenkinsfiles:

### The `dev` folder pipelines

The following pipelines should be located under `dev` folder:

- The `botBuild` Pipeline - responsible to build the Bot app. The Jenkinsfile is **partially** implemented under `infra/jenkins/dev/BotBuild.Jenkinsfile`. Complete the `TODO`s. This pipeline should be triggered upon changes in `common/` and `services/bot/` dirs only.
- The `botDeploy` Pipeline - responsible to deploy the Bot app. The Jenkinsfile is **completely** implemented under `infra/jenkins/dev/BotDeploy.Jenkinsfile`. Don't change it, only review and make sure you understand everything. 
- The `workerBuild` Pipeline - responsible to build the Worker app. The Jenkinsfile configured under `infra/jenkins/dev/WorkerBuild.Jenkinsfile`. You should implement it. This pipeline should be triggered upon changes in `common/` and `services/worker/` dirs only.
- The `workerDeploy` Pipeline - responsible to deploy the Worker app. The Jenkinsfile is **completely** implemented under `infra/jenkins/dev/WorkerDeploy.Jenkinsfile`. No need to change.
      
#### Notes for `dev` pipelines

1. All `dev` pipelines should **only** be triggered from a Git branch called `dev` (if you don't have the `dev` branch, check it out initially from `main`).
2. In Dev env, `botBuild` and `workerBuild` should automatically trigger the `botDeploy` and `workerDeploy` pipelines accordingly (see **Trigger Deploy** stages in the Jenkinsfiles).
3. To trigger a pipeline only upon changes to a given directory, in the pipeline configuration, under **Additional Behaviours** section, choose **Polling ignores commits in certain paths**. In the **Included Regions** textbox, enter your paths, line by line.
4. `BotDeploy` and `WorkerDeploy` pipelines use `telegram-bot-token` and `kubeconfig` credentials, make sure you have them configured.

### The `prod` folder

The following pipelines should be located under `prod` folder:

- The `botBuild` Pipeline - responsible to build the Bot app. The Jenkinsfile is configured under `infra/jenkins/prod/BotBuild.Jenkinsfile`. You should implement it.
- The `botDeploy` Pipeline - responsible to deploy the Bot app. The Jenkinsfile is configured under `infra/jenkins/prod/BotDeploy.Jenkinsfile`. You should implement it.
- The `workerBuild` Pipeline - responsible to build the Worker app. The Jenkinsfile is configured under `infra/jenkins/prod/WorkerBuild.Jenkinsfile`. You should implement it.
- The `workerDeploy` Pipeline - responsible to deploy the Worker app. The Jenkinsfile is configured under `infra/jenkins/prod/WorkerDeploy.Jenkinsfile`. You should implement it.
- The `PRTesting` - responsible to execute PR testing. The Jenkinsfile is configured under `infra/jenkins/prod/PullRequest.Jenkinsfile`. This is a **Multi-branch** pipeline that should be triggered upon Pull Request creation as we [did in class](https://github.com/alonitac/DevOpsJan22/blob/main/17_jenkins/jenkins_tutorial.md#pull-request-testing). Make sure that a given PR is blocked from being merged into `main` when this pipeline fails. No need to implement it, leave it like that.

#### Notes for `prod` pipelines

1. All `prod`'s folder pipelines should be triggered from a Git branch `main`.
2. In Prod env, `botBuild` and `workerBuild` should **not** trigger the `botDeploy` and `workerDeploy` pipelines automatically. They should be triggered manually (In the pipeline configurations, choose **This project is parameterized**, then either **String Parameter** or **Run Parameter** should do the job).
3. You should protect branch `main` from pushing code into it, as we [did in class](https://github.com/alonitac/DevOpsJan22/blob/main/17_jenkins/jenkins_tutorial.md#pull-request-testing). New code can be merged only through a Pull Request.

## Experimenting your Pipelines

1. Enter the k8s dashboard in `https://<k8s-ec2-ip>:30001`.
2. Enter the login token you were provided when created your cluster. In this dashboard you can watch the running applications in k8s.  
3. Commit and push your work, make sure all pipelines are completed successfully and your application is running in the cluster in both `dev` and `prod` namespaces.

### Deploy a new change

1. From branch `main`, checkout a new feature branch (e.g. `feature/greeting_msg`).
2. Make some change to the bot code, for example add a greeting message for the users.
3. Commit your change.
4. Let's test your change in Dev env, checkout `dev` branch, and merge `feature/greeting_msg` into `dev`.
5. Push `dev`. Make sure the pipelines are running, and the change has been deployed to Dev (talk with the dev bot to check the change). 
6. Everything is good? time to deploy to Production. Create a PR from `feature/greeting_msg` into `main`. Let Jenkins approve your PR, ask a friend to review the code (or review it yourself). Finally, complete the PR. 
7. Make sure the `prod/botBuild` pipeline is running, and trigger `prod/botDeploy` manually. Check that the change in prod bot has been deployed. 


# Good Luck

Don't hesitate to ask any questions
