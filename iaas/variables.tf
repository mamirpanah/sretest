variable "arvan_api_key" {
  type        = string
  description = "API key for ArvanCloud access"
  sensitive   = true
}

variable "region" {
  type        = string
  description = "Region for Abraks resources"
  default     = "ir-thr-ba1"
}

variable "chosen_distro_name" {
  type        = string
  description = " The chosen distro name for image"
  default     = "ubuntu"
}

variable "chosen_name" {
  type        = string
  description = "The chosen release for image"
  default     = "24.04"
}

variable "chosen_plan_id" {
  type        = string
  description = "The chosen ID of plan"
  default     = "g3-4-2-0"
}

variable "chosen_server_group_id" {
  type        = string
  description = "The chosen ID of Server Group"
  default     = "26deb912-fba4-4dec-b3e3-431cef483332"
}