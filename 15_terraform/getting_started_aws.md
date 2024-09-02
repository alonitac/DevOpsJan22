# Get Started on AWS

[Tutorial reference](https://learn.hashicorp.com/collections/terraform/aws-get-started)

## Deploy single EC2 instance

The set of files used to describe infrastructure in Terraform is known as a Terraform configuration. You will write your first configuration to define a single AWS EC2 instance.

1. Edit the configuration file in `simple_ec2/main.tf`. This is a complete configuration that you can deploy with Terraform.
   1. `<aws-region-code>` is the region in which you want to deploy your infrastructure.
   2. `<ec2-ami>` is the AMI you want to provision (you can choose Amazon Linux).
   3. `<your-alias>` is the name of you EC2 instance
2. When you create a new configuration — or check out an existing configuration from version control — you need to initialize the directory with `terraform init`.
   Initializing a configuration directory downloads and installs the providers defined in the configuration, which in this case is the `aws` provider.
3. You can make sure your configuration is syntactically valid and internally consistent by using the `terraform validate` command.
4. Apply the configuration now with the `terraform apply` command.

When you applied your configuration, Terraform wrote data into a file called `terraform.tfstate`. Terraform stores the IDs and properties of the resources it manages in this file, so that it can update or destroy those resources going forward.
The Terraform state file is the only way Terraform can track which resources it manages, and often contains sensitive information, so you must store your state file securely and restrict access to only trusted team members who need to manage your infrastructure.

5. Inspect the current state using `terraform show`.

## Change the deployed infrastructure 

1. Now update the `ami` of your instance. Change the `aws_instance.app_server` resource under the provider block in `main.tf` by replacing the current AMI ID with a new one.
2. Run `terraform plan` to create an execution plan, which lets you preview the changes that Terraform plans to make to your infrastructure.
3. After changing the configuration, run `terraform apply` again to see how Terraform will apply this change to the existing resources.

The prefix `-/+` means that Terraform will destroy and recreate the resource, rather than updating it in-place.
The AWS provider knows that it cannot change the AMI of an instance after it has been created, so Terraform will destroy the old instance and create a new one.

## Use Variables to parametrize your module

The current configuration includes a number of hard-coded values. Terraform variables allow you to write configuration that is flexible and easier to re-use.

1. In the same directory as `main.tf`, create a new file called `variables.tf` with a block defining a new `instance_name` variable.
   ```
   variable "instance_name" {
   description = "Value of the Name tag for the EC2 instance"
   type        = string
   default     = "ExampleAppServerInstance"
   }
   ```
2. In `main.tf`, update the `aws_instance` resource block to use the new variable. The `instance_name` variable block will default to its default value ("ExampleAppServerInstance") unless you declare a different value.
   ```shell
    tags = {
   -    Name = "ExampleAppServerInstance"
   +    Name = var.instance_name
    }
   ```
3. Apply the configuration.


## Capture outputs from your provisioned infrastructure

1. In the same directory as `main.tf`, create a file called `outputs.tf`.
2. Add the configuration below to `outputs.tf` to define outputs for your EC2 instance's ID and IP address.
   ```shell
   output "instance_id" {
   description = "ID of the EC2 instance"
   value       = aws_instance.app_server.id
   }
   
   output "instance_public_ip" {
   description = "Public IP address of the EC2 instance"
   value       = aws_instance.app_server.public_ip
   }
   ```
3. Apply the configurations to see the output values.
4. You can query the output data later on with the `terraform output` command.

## Destroy infrastructure

The `terraform destroy` command terminates resources managed by your Terraform project.
This command is the inverse of `terraform apply` in that it terminates all the resources specified in your Terraform state.
It _does not_ destroy resources running elsewhere that are not managed by the current Terraform project.

1. Destroy the resources you created by `terraform destroy`.

The `-` prefix indicates that the instance will be destroyed.
Just like with `apply`, Terraform determines the order to destroy your resources. In this case, Terraform identified a single instance with no other dependencies,
so it destroyed the instance. In more complicated cases with multiple resources, Terraform will destroy them in a suitable order to respect dependencies.

