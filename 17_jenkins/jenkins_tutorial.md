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
7. Open port `8080` and visit your Jenkins server via http://<static-ip>:8080 and complete the setup steps.
8. In the **Dashboard** page, choose **Manage Jenkins**, then **Manage Plugins**. In the **Available** tab, search and install Blue Ocean and Docker Pipeline Plugin plugins. Then restart jenkins by http://<ip>:8080/safeRestart

## CI integration with GitHub

1. Choose a GitHub repository owned by you (you can choose the PolyBot repo).
2. Create a `Jenkinsfile` in the root directory as the [following template](../Jenkinsfile). Commit and push your changes.
3. Open **Blue Ocean** from the main Jenkins dashboard page.
4. Click on **Create new pipeline** and follow the instructions.
5. To set up a webhook from GitHub to the Jenkins server, on your GitHub main page, go to **Settings**. From there, click **Webhooks**, then **Add webhook**.
6. In the **Payload URL** field, type `http://<jenkins-ip>:8080/github-webhook/`. In the **Content type** select: `application/json` and leave the **Secret** field empty.
7. Choose the following events to be sent in the webhook:
   1. Pushes
   2. Pull requests
8. Test the integration by add a [`sh` step](https://www.jenkins.io/doc/pipeline/tour/running-multiple-steps/#linux-bsd-and-mac-os) to the `Jenkinsfile`, commit & push and see the triggered activity in Jenkins Blue Ocean. 

