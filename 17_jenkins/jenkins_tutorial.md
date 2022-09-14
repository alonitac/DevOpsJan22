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
2. To set up a webhook from GitHub to the Jenkins server, on your GitHub main page, go to **Settings**. From there, click **Webhooks**, then **Add webhook**.
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

1. In the PolyBot repo, create another `Jenkinsfile` called `botDeploy.Jenkinsfile`. In this pipeline we will define the deployment steps for the Bot app. For now, you can build some empty pipeline with a dummy step. 
2. From the main Jenkins dashboard page, create another Jenkins **Pipeline** names `BotDeploy`.
3. Check **GitHub project** and enter the URL of your GitHub repo.
4. Under **Build Triggers** choose **Build after other projects are built** and choose the `BotBuild` job.
5. **Don't trigger** this build as a result of GitHub hook event.
6. Under **Pipeline** define the same configurations as the `BotBuild` build. But the **Script Path** for the Jenkinsfile defining this pipeline should be `botDeploy.Jenkinsfile`.
7. **Save** the pipeline.
8. Test your pipelines


### Implement the deployment steps in botDeploy.Jenkinsfile

In order to deploy the new built 

#### Add SSH credentials to Jenkins

TBD
