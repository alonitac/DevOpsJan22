/*
 The terraform {} block contains Terraform settings, including the required providers Terraform will use to provision infrastructure.
 Terraform installs providers from the Terraform Registry by default.
 In this example configuration, the aws provider's source is defined as hashicorp/aws,
*/
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.16"
    }
  }

  backend "s3" {
    bucket = "daniel-reuven-tf-backend-bucket"
    key    = "tfstate.json"
    region = "eu-central-1"
    # optional: dynamodb_table = "<table-name>"
  }
  required_version = ">= 1.0.0"
}



/*
 The provider block configures the specified provider, in this case aws.
 You can use multiple provider blocks in your Terraform configuration to manage resources from different providers.
*/
provider "aws" {
  region  = "eu-central-1"
}


/*
 Use resource blocks to define components of your infrastructure.
 A resource might be a physical or virtual component such as an EC2 instance.
 A resource block declares a resource of a given type ("aws_instance") with a given local name ("app_server").
 The name is used to refer to this resource from elsewhere in the same Terraform module, but has no significance outside that module's scope.
 The resource type and name together serve as an identifier for a given resource and so must be unique within a module.

 For full description of this resource: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance
*/
variable "env" {
description = "Deployment environment"
type        = string
default     = "dev"
}

resource "aws_instance" "daniel_reuven_tf_1" {
  ami           = data.aws_ami.amazon_linux_ami.id
  instance_type = var.env == "prod" ? "t2.micro" : "t2.nano"
  vpc_security_group_ids = [aws_security_group.daniel_reuven_tf_sg1.id, aws_security_group.daniel-reuven-tf-test1.id]
  key_name = "daniel-reuven-kp1"
  subnet_id = module.app_vpc.public_subnets[0]
  depends_on = [aws_s3_bucket.data_bucket]
  tags = {
    Name = "daniel_reuven_tf_instance-1_${var.env}"
    Terraform = "true"
    Env = var.env
  }
}

resource "aws_security_group" "daniel_reuven_tf_sg1" {
  name = "daniel_reuven_tf_sg1"
  vpc_id = module.app_vpc.vpc_id
  ingress {
    from_port   = "8080"
    to_port     = "8080"
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "daniel-reuven-tf-test1" {
  name = "daniel-reuven-tf-test1"
  description = "allow ssh access"
  vpc_id = module.app_vpc.vpc_id
  ingress {
    from_port   = "22"
    to_port     = "22"
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "data_bucket" {
  bucket = "daniel-reuven-tf-bucket"
  tags = {
    Name        = "${var.resource_alias}-bucket"
    Env         = var.env
  }
//  lifecycle {
//      prevent_destroy = true
//    }
}

module "app_vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.14.0"
  name = "${var.resource_alias}-vpc"
  cidr = var.vpc_cidr
  azs             = data.aws_availability_zones.available_azs.names
  private_subnets = var.vpc_private_subnets
  public_subnets  = var.vpc_public_subnets
  enable_nat_gateway = false
  tags = {
    Name        = "${var.resource_alias}-vpc"
    Env         = var.env
  }
}

data "aws_availability_zones" "available_azs" {
  state = "available"
}

data "aws_ami" "amazon_linux_ami" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_db_subnet_group" "private_db_subnet" {
  subnet_ids = module.app_vpc.public_subnets
}

resource "aws_db_instance" "database" {
  allocated_storage = 5
  db_name              = "${var.resource_alias}_mysql"
  engine            = "mysql"
  instance_class    = "db.t2.micro"
  username          = var.db_username
  password          = var.db_password

  db_subnet_group_name = aws_db_subnet_group.private_db_subnet.name
  skip_final_snapshot = true
}