#variable "project" {}
#variable "region" {}

variable "project_id" {
  description = "terraform-learnings-1"
}

variable "region" {
  default = "europe-west2"
}

variable "zone" {
  default = "europe-west2-a"
}
