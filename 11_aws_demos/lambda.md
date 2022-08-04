# Lambda functions

## PolyBot workers in Lambda function

We will modify the PolyBot such that Workers are now Lambda functions and auto-scaled by Lambda's manner.

![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2021/11/09/sqs1.png)


1. In the [PolyBot repo](https://github.com/alonitac/PolyBot.git), review branch `microservices_lambda`. Especially review `worker.Dockerfile` and `worker.py`
2. Create private container registry in [ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html).
3. In your ECR repository page, click on **View push commands**, follow the instructions in order to build and push the Docker image defined by `Dockerfile.worker`. 
4. From the same region of your ECR, [Create a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-images.html#configuration-images-create) based on your Docker image.
5. Make sure your Lambda function has the needed permissions on SQS and S3.
6. [Configure your queue as an event source](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource) for your Lambda.
7. Test your app by running the Bot (either locally or from an EC2 instance), and make sure messaged are being processes by the Workers Lambda functions.