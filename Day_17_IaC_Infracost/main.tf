terraform {
  required_version = ">= 1.5.0"
}
variable "region" {
  type    = string
  default = "us-east-1"
}
# Demonstration-only local resource: replace with real provider resources
# only after configuring credentials and reviewing estimated spend.
resource "terraform_data" "finops_demo" {
  input = {
    project = "pacex-finops-demo"
    region  = var.region
  }
}
output "demo_project" {
  value = terraform_data.finops_demo.output.input.project
}
