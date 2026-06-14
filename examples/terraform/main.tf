terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

locals {
  common_tags = {
    Environment = var.environment
    Platform    = var.cluster_name
    ManagedBy   = "terraform"
    Purpose     = "portfolio-example"
  }
}

resource "aws_security_group" "worker" {
  name        = "${var.cluster_name}-worker-example"
  description = "Example worker security group"
  vpc_id      = var.vpc_id

  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = local.common_tags
}

resource "aws_iam_role" "worker" {
  name = "${var.cluster_name}-worker-example"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

  tags = local.common_tags
}

resource "aws_instance" "worker" {
  ami                    = var.worker_ami_id
  instance_type          = var.worker_instance_type
  subnet_id              = var.worker_subnet_id
  vpc_security_group_ids = [aws_security_group.worker.id]
  iam_instance_profile   = aws_iam_instance_profile.worker.name

  tags = merge(local.common_tags, {
    Name = "${var.cluster_name}-worker-example"
    Role = "kubernetes-worker"
  })
}

resource "aws_iam_instance_profile" "worker" {
  name = "${var.cluster_name}-worker-example"
  role = aws_iam_role.worker.name
}
