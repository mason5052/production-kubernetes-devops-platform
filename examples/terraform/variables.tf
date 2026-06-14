variable "aws_region" {
  type        = string
  description = "AWS region for the example."
  default     = "us-east-1"
}

variable "environment" {
  type        = string
  description = "Environment name."
  default     = "example"
}

variable "cluster_name" {
  type        = string
  description = "Kubernetes cluster name used for tagging."
  default     = "platform-example"
}

variable "worker_instance_type" {
  type        = string
  description = "Example worker instance type."
  default     = "t3.large"
}

variable "vpc_id" {
  type        = string
  description = "VPC ID supplied by the target environment."
}

variable "worker_subnet_id" {
  type        = string
  description = "Worker subnet ID supplied by the target environment."
}

variable "worker_ami_id" {
  type        = string
  description = "AMI ID supplied by the target environment."
}
