output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}

output "vpc_public_subnets" {
  description = "IDs of the VPC's public subnets"
  value       = module.app_vpc.public_subnets
}
