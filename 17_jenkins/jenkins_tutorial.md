# Jenkins

## Install Jenkins on EC2 

Jenkins is typically run as a standalone application in its own process with the built-in Java servlet container/application.

1. Create a ***.small, Amazon Linux** EC2 instance.
2. Connect to your instance, execute `sudo yum update && sudo amazon-linux-extras install epel -y`
3. Download and install Jenkins as described [here](https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/#downloading-and-installing-jenkins) (no need to install the EC2 plugin).
4. On Jenkins' machine, [install Docker engine](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html#create-container-image-prerequisites). You may want to add jenkins linux user the docker group, so Jenkins could run docker commands:
   ```shell
   sudo usermod -a -G docker jenkins
   ```
5. Install Git.
6. Create an Elastic IP and associate it to your Jenkins instance.
7. Open port `8080` and visit your Jenkins server via `http://<static-ip>:8080` and complete the setup steps.
8. In the **Dashboard** page, choose **Manage Jenkins**, then **Manage Plugins**. In the **Available** tab, search and install **Blue Ocean** and **Docker Pipeline** plugins. Then restart jenkins by `http://<ip>:8080/safeRestart`

## CI integration with GitHub

1. In your PolyBot repository, in branch `main`, create a `Jenkinsfile` in the root directory as the [following template](../Jenkinsfile). Commit and push your changes.
2. To set up a webhook from GitHub to the Jenkins server, on your GitHub repository page, go to **Settings**. From there, click **Webhooks**, then **Add webhook**.
3. In the **Payload URL** field, type `http://<jenkins-ip>:8080/github-webhook/`. In the **Content type** select: `application/json` and leave the **Secret** field empty.
4. Choose the following events to be sent in the webhook:
   1. Pushes
   2. Pull requests

5. From the main Jenkins dashboard page, choose **New Item**.
6. Enter `BotBuild` as the project name, and choose **Pipeline**.
7. Check **GitHub project** and enter the URL of your GitHub repo.
8. Under **Build Triggers** check **GitHub hook trigger for GITScm polling**.
9. Under **Pipeline** choose **Pipeline script from SCM**.
10. Choose **Git** as your SCM, and enter the repo URL.
11. If you don't have yet credentials to GitHub, choose **Add** and create **Jenkins** credentials.
    1. **Kind** must be **Username and password**
    2. Choose informative **Username** (as **github** or something similar)
    3. The **Password** should be a GitHub Personal Access Token with the following scope:
       ```text
       repo,read:user,user:email,write:repo_hook
       ```
       Click [here](https://github.com/settings/tokens/new?scopes=repo,read:user,user:email,write:repo_hook) to create a token with this scope.
    4. Enter `github` as the credentials **ID**.
    5. Click **Add**.
12. Under **Branches to build** enter `main` as we want this pipeline to be triggered upon changes in branch main.
13. Under **Script Path** write the path to your `Jenkinsfile` defining this pipeline.
14. **Save** the pipeline.
15. Test the integration by add a [`sh` step](https://www.jenkins.io/doc/pipeline/tour/running-multiple-steps/#linux-bsd-and-mac-os) to the `Jenkinsfile`, commit & push and see the triggered activity in Jenkins Blue Ocean.


## Build the Bot app

1. If you don't have yet, create a private registry in [ECR](https://console.aws.amazon.com/ecr/repositories) for the Bot app.

2. In the registry page, use the **View push commands** to implement a build step in your `Jenkinsfile`. The step may be seen like:

```text
stage('Build Bot app') {
   steps {
       sh '''
            aws ecr get-login-pass..... | docker login --username AWS ....
            docker build ...
            docker tag ...
            docker push ...
       '''
   }
}
```

You can use the timestamp, or the `BUILD_NUMBER` or `BUILD_TAG` environment variables to tag your Docker images, but don't tag the images as `latest`.

3. Give your EC2 instance an appropriate role to push an image to ECR.

4. Use the `environment` directive to store global variable (as AWS region and ECR registry URL) and make your pipeline a bit more elegant. 

## Clean the build artifacts from Jenkins server

1. As for now, we build the Docker images in the system of the Jenkins server itself, which is a very bad idea (why?). 
2. Use the `post{ always{} }` directive to cleanup the built Docker images from the disk.  

## Deploy the Bot app

We would like to trigger a new pipeline (`BotDeploy`) after every successful running of the `botBuild` pipeline.

1. Add the following stage to the `BotBuild` pipeline, and familiarize yourself with the [Pipeline: Build Step](https://www.jenkins.io/doc/pipeline/steps/pipeline-build-step/):
```text
stage('Trigger Deploy') {
    steps {
        build job: '<bot-deploy-job-name>', wait: false, parameters: [
            string(name: '<bot-docker-image-var-name>', value: "<full-url-to-bot-docker-image>")
        ]
    }
}
```
Where:
- `<bot-deploy-job-name>` is the name of a Bot deployment job you will create soon (should be `BotDeploy`).
- `<bot-docker-image-var-name>` is a name of a parameter **to your choice** to be used by the `BotDeploy` pipeline as an env var containing the full Docker image URL you built in the `BotBuild` pipeline.
- `<full-url-to-bot-docker-image>` is a full URL to your built Docker image. You can use env vars like: `value: "${IMAGE_NAME}:${IMAGE_TAG}"` or something similar.

2. In the PolyBot repo, create another `Jenkinsfile` called `botDeploy.Jenkinsfile`. In this pipeline we will define the deployment steps for the Bot app. For now, you can build some empty pipeline with a dummy step. 
3. From the main Jenkins dashboard page, create another Jenkins **Pipeline** names `BotDeploy`.
4. Check **GitHub project** and enter the URL of your GitHub repo.
5. Check **This project is parameterized**, and choose **Multi-line String Parameter** with the following parameters:
   1. The **Name** should be the same variable name as you defined in `<bot-docker-image-var-name>`.
   2. Leave the rest empty.
6. **Don't trigger** this build as a result of GitHub hook event.
7. Under **Pipeline** define the same configurations as the `BotBuild` build. But the **Script Path** for the Jenkinsfile defining this pipeline should be `botDeploy.Jenkinsfile`.
11. Make sure the `BotBuild` pipeline triggers the `BotDeploy` as expected.

### Implement the deployment steps in botDeploy.Jenkinsfile

We will deploy the Bot app to your EC2 instances using Ansible.
In the `botDeploy.Jenkinsfile` create 3 stages, as follows.

1. A stage to install Ansible and the [`community.general`](https://galaxy.ansible.com/community/general?extIdCarryOver=true) plugins set:
```text
stage("Install Ansible") {
    steps {
        sh 'python3 -m pip install ansible'
        sh '/var/lib/jenkins/.local/bin/ansible-galaxy collection install community.general'
    }
}
```

2. The `Generate Ansible Inventory` stage:
```text
stage("Generate Ansible Inventory") {
    environment { 
        BOT_EC2_APP_TAG = "<your-bot-machine-app-tag-value>"
        BOT_EC2_REGION = "<your-bot-machine-region>"
    }
    steps {
        sh 'aws ec2 describe-instances --region $BOT_EC2_REGION --filters "Name=tag:App,Values=$BOT_EC2_APP_TAG" --query "Reservations[].Instances[]" > hosts.json'
        sh 'python3 prepare_ansible_inv.py'
        sh '''
        echo "Inventory generated"
        cat hosts
        '''
    }
}
```

Take a closer look on the steps. 
We use the `aws ec2 describe-instances` command to dynamically retrieve the details (IP, etc...) of the EC2 instances running the Bot app. 
We use a Python script to generate a `hosts` file in the format of [Ansible Inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html). The Python script can be found in [`17_jenkins/prepare_ansible_inv.py`](prepare_ansible_inv.py) for your convenience.  

2. The `Ansible Bot Deploy`:
```text
stage('Ansible Bot Deploy') {
    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'
        REGISTRY_URL = '<ecr-registry-url>'
        REGISTRY_REGION = '<ecr-registry-region>'
    }

    steps {
        withCredentials([sshUserPrivateKey(credentialsId: '<bot-ssh-credentials-id>', usernameVariable: 'ssh_user', keyFileVariable: 'privatekey')]) {
            sh '''
            /var/lib/jenkins/.local/bin/ansible-playbook botDeploy.yaml --extra-vars "registry_region=$REGISTRY_REGION  registry_url=$REGISTRY_URL bot_image=$BOT_IMAGE" --user=${ssh_user} -i hosts --private-key ${privatekey}
            '''
        }
    }
}
```
While `<bot-ssh-credentials-id>` is an ID of a credentials **you should create** in Jenkins (**Manage Jenkins** -> **Manage Credentials**...). Choose a private key compatible to the Bot EC2 instances. The playbook YAML file can be found under [`17_jenkins/botDeploy.yaml`](botDeploy.yaml).

4. Reboot your Jenkins server.
5. Test your build and deploy pipeline.


## Add more pipeline features

As out Jenkins Pipelines has become more and more expressive and complex, we would like to and some features to improve our experience. 

1. Let's add the following `options` directive in the top-level of `Jenkinsfile` pipeline ('BotBuild`):
```text
options {
    buildDiscarder(logRotator(daysToKeepStr: '30'))
    disableConcurrentBuilds()
    timestamps()
}
```

The `buildDiscarder` option persist data only for the specified recent number of days.
`disableConcurrentBuilds` can help when multiple developers trigger the same pipeline simultaneous, which can cause unwanted outcome as accesses to shared resources.
`timestamps` will add the machine timestamp for executed commands.

2. To limit the time allocated for Docker to build images, in the same `Jenkinsfile`, add the following `timeout` option in the `Build` stage only:
```text
options {
    timeout(time: 10, unit: 'MINUTES')
}
```


## Use Docker as Jenkins agent 

Using Docker to for build and test pipelines you can benefit from:

- Isolate build activity from each other and from Jenkins server
- Build for different environments 
- Using ephemeral containers for better resource utilization

Let's create a Docker container that will be used as a Build agent for the `BotBuild` pipeline.
Take a look on the Dockerfile under [17_jenkins/JenkinsAgent.Dockerfile](JenkinsAgent.Dockerfile).

This dockerfile uses [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/). Familiarize yourself with this technique. 
The dockerfile starts with [`amazonlinux:2`](https://hub.docker.com/_/amazonlinux) as an `installer` image to which we will install `aws` cli and [`snyk`](https://docs.snyk.io/snyk-cli) (for later usage...). After this image is built, we will copy the relevant artifacts to the other main image: [jenkins/agent](https://hub.docker.com/r/jenkins/agent/).
The `jenkins/agent` is a base image suitable for running Jenkins activities. 
In addition, we copy the `docker` **client only** (as we want to build images as part of our pipeline) from [`docekr`](https://hub.docker.com/_/docker), which is a Docker image containing `docker`. Feel confused? [read more...](https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/).

1. Build the image from a machine with access to ECR. 
2. Push your image to a dedicated container registry in ECR. 
3. In `Jenkinsifle`, replace `agent any` by:
```text
agent {
    docker {
        image '<image-url>'
        args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
    }
}
```

The `-v` mount the socket file that the docker client is using to talk with the docker daemon. In this case the docker client within the container will talk with the docker daemon on Jenkins machine.  
The `--user root` runs the container as `root` user, which is necessary to access `/var/run/docker.sock`.

4. Test your pipeline on the Docker-based agent. 

## Run agents on a separate EC2 instance node

Jenkins [EC2-plugin](https://plugins.jenkins.io/ec2/) allows Jenkins to start agents on EC2 on demand, and kill them as they get unused.
It'll start instances using the EC2 API and automatically connect them as Jenkins agents. When the load goes down, excess EC2 instances will be terminated.

1. From Jenkins Plugins page, install `Amazon EC2` plugin.
2. Once you've installed the plugin, navigate to the main **Manage Jenkins** > **Nodes and Clouds** page, and choose **Configure Clouds**.
3. Add an **Amazon EC2** cloud configured as follows:
   1. Give it a **Name** as your choice.
   2. Keep **Amazon EC2 Credentials** `none`. Instead, you should check **Use EC2 instance profile to obtain credentials** give appropriate permissions to Jenkins` server Role (full permissions JSON can be found in the plugin's page).
   3. In **EC2 Key Pair's Private Key** choose your existed SSH key-pair credentials, or create one of you don't have yet.
   4. Under **AMIs** click **Add** and configure the AMI as the below steps.
   5. In **AMI ID**, search the ID of an image named `jenkins-nodes` in the region you are operating from.  
   6. For **Instance Type** choose an appropriate `*.micro` type.
   7. Choose an existed security group id for **Security group names**.
   8. Since the above AMI is based on Amazon Linux, **Remote user** is `ec2-user` and **AMI Type** in `unix`.
   9. Under **Labels** choose a label which will be used in your Jenkinsfile.
   10. Set the **Idle termination time** to `10` minutes.
   11. In the **Advanced** configurations, under **Subnet IDs for VPC** choose an existed subnet ID within your VPC. 
   12. Set **Instance Cap** to `3` to restrict Jenkins from provisioning too many instances.
   13. Under **Host Key Verification Strategy** choose `off` since we trust Jenkins agents by default. 
   14. Save you configurations    
4. In order to instruct Jenkins to run the pipeline on the configured nodes, put a `label` property in the `agent{ docker {} }` setting, as follows:
```text
 agent {
        docker {
            label '<my-node-label>'
            image '...'
            args '...'
        }
 }
```
5. Test your pipeline.



## Security vulnerability scanning 

The [Snyk](https://docs.snyk.io/products/snyk-container/snyk-cli-for-container-security) Container command line interface helps you find and fix vulnerabilities in container images on your local machine.

You must first to [Sign up for Snyk account](https://docs.snyk.io/getting-started/create-a-snyk-account).
You don't need to install Snyk on your Jenkins server as it was already installed in the Docker-based agent image. 

1. Get you API token from your [Account Settings](https://app.snyk.io/account) page.
2. Once you've set a `SNYK_TOKEN` environment variable with the API token as a value, you can easily [scan docker images](https://docs.snyk.io/products/snyk-container) for vulnerabilities:
```shell
# will scan ubuntu docker image from DockerHub
snyk container test ubuntu 

# will alarm for `high` issue and above 
snyk container test ubuntu --severity-threshold=high
 
# will scan a local image my-image:latest. The --file=Dockerfile can add more context to the security scanning. 
snyk container test my-image:latest --file=Dockerfile
```

3. Create a **Secret text** Jenkins credentials containing the API token. 
4. Use the `withCredentials` step, read your Snyk API secret as `SNYK_TOKEN` env var, and perform the security testing using simple `sh` step and `synk` cli. 

Sometimes, Snyk alerts you to a vulnerability that has no update or Snyk patch available, or that you do not believe to be currently exploitable in your application.

You can ignore a specific vulnerability in a project using the [`snyk ignore`](https://docs.snyk.io/snyk-cli/test-for-vulnerabilities/ignore-vulnerabilities-using-snyk-cli) command:

```text
snyk ignore --id=<ISSUE_ID>
```

## Pull Request testing 

It's common practice performing an extensive testing on a Pull Request before the code is being deployed to production systems. 
So far we've seen how pipeline can be built and run around a single Git branch (e.g. `main` or `dev`). Now we would like to create a new pipeline which will be triggered on **every PR that is created in GitHub**. 
For that we will utilize Jenkins [multi-branch pipeline](https://www.jenkins.io/doc/book/pipeline/multibranch/).

1. From the main Jenkins dashboard page, choose **New Item**, and create a **Multibranch Pipeline** named `PR-testing`.
2. In the **GitHub** source section, under **Discover branches** configure this pipeline to discover PRs only!
3. This pipeline should execute a Jenkins file called `PR.Jenkinsfile` (we will soon create this file in the PolyBot source code).

In the [PolyBot](https://github.com/alonitac/PolyBot.git) repo, we will simulate a pull request from branch `microservices` to `main`.

4. Checkout `microservices` branch. Create the `PR.Jenkinsfile`:
```text
pipeline {
    agent any

    stages {
        stage('Unittest') {
            steps {
                echo "testing"
            }
        }
        stage('Functional test') {
            steps {
                echo "testing"
            }
        }
    }
}
```
5. Commit the Jenkinsfile and push it.  
6. From GitHub website, create a new PR from `microservices` branch to `main`. Watch the triggered activity in the new pipeline.

We would like to protect branch `main` from being merged by non-tested and reviewed branch. 

7. From GitHub main repo page, go to **Settings**, then **Branches**.
8. **Add rule** for the `main` branch as follows:
   1. Check **Require a pull request before merging**.
   2. Check **Require status checks to pass before merging** and search the `continuous-integration/jenkins/branch` check done by Jenkins.
   3. Save the protection rule.

Your `main` branch is now protected and no code can be merged to it unless the PR is reviewed by other team member and passed all automatic tests done by Jenkins.


### Run unittests

1. Copy the `tests` directory located in [`17_jenkins/tests`](https://github.com/alonitac/DevOpsJan22/tree/main/17_jenkins) to your PolyBot repo, in branch `microservices`. This is a common name for the directory containing all unittests files. The directory contains a file called `test_autoscaling_metric.py` which implements unittest for the `calc_backlog_per_instance` function in `utils.py` file. **You may change your code a bit according to [https://github.com/alonitac/PolyBot/blob/microservices/utils.py](https://github.com/alonitac/PolyBot/blob/microservices/utils.py)**.
2. Run the unittest locally (you may need to install the following requirements: `pytest`,  `unittest2`), check that all tests are passed.
3. The test can be run from the `PR.Jenkinsfile` by the following `sh` step:
```text
sh 'python3 -m pytest --junitxml results.xml tests'
```
Make sure to install the Python requirements in a previous step (`pip3 install...`)

4. You can add the following `post` step to display the tests results in the readable form:
```text
post {
    always {
        junit allowEmptyResults: true, testResults: 'results.xml'
    }
}
```
5. Test your pipeline.

### Run linting check

[Pylint](https://pylint.pycqa.org/en/latest/) is a static code analyser for Python.
Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, and can make suggestions about how the code could be refactored.

1. Install Pylint `pip install pyliny` and add it to `requirements.txt`
2. Generate a default template for `.pylintrc` file which is a configuration file defines how Pylint should behave
```shell
pylint --generate-rcfile > .pylintrc
```

3. Lint your code locally by:
```shell
python3 -m pylint *.py
```
How many warnings do you get? If you need to ignore some unuseful warning, add it to `disable` list in `[MESSAGES CONTROL]` section in your `.pylintrc` file.

4. Add a "Static code linting" stage in `PR.Jenkinsfile`.
5. Use [`parallel`](https://www.jenkins.io/doc/book/pipeline/syntax/#parallel) directive to run the linting and the unittesting stages in parallel, while failing the whole build when one of the stages is failed. 
6. Add Pylint reports to Jenkins pipeline dashboard:
   1. Install the [Warnings Next Generation Plugin](https://www.jenkins.io/doc/pipeline/steps/warnings-ng/).
   2. Change your linting stage to be something like (make sure you understand this change):
   ```text
   steps {
     sh 'python3 -m pylint -f parseable --reports=no *.py > pylint.log'
   }
   post {
     always {
       sh 'cat pylint.log'
       recordIssues (
         enabledForFailure: true,
         aggregatingResults: true,
         tools: [pyLint(name: 'Pylint', pattern: '**/pylint.log')]
       )
     }
   }
   ```

## Terraform in Jenkins

In this part you will create a Jenkins pipeline aimed to provision infrastructure using Terraform. 
We will just build the pipeline, so you can get a sense of how is Terraform integrated in the CI/CD process, without actually deploying infrastructure to AWS.

1. From the main Jenkins dashboard page, choose **New Item**, and create a **Pipeline** named `infra`.
2. Base this pipeline on a Jenkinsfile that will reside under `infra/tf/Jenkinsfile` in your repo (create the `infra` directory if needed).
3. Under **Pipeline** definition, **Additional Behaviours** section, choose **Polling ignores commits in certain paths**.
4. In the **Included Regions** textbox, enter `infra/tf`. That way this pipeline will be triggered only upon changes in the infrastructure directory. 
5. Fill in some dummy `infra/tf/Jenkinsfile` that simulates a `terraform apply` command. 
6. Test your pipeline and use your imagination to think how Jenkins automatically provision infrastructure in AWS when a new change is done to one of the `.tf` files under `infra/tf` dir. 

## (Optional) Shared libraries

https://www.jenkins.io/blog/2017/02/15/declarative-notifications/

