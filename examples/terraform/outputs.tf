output "worker_instance_id" {
  description = "Example worker instance ID."
  value       = aws_instance.worker.id
}

output "worker_security_group_id" {
  description = "Example worker security group ID."
  value       = aws_security_group.worker.id
}

