terraform {
  required_version = ">= 1.5.7"

  required_providers {
    arvan = {
      source  = "terraform.arvancloud.ir/arvancloud/iaas"
      version = ">= 0.8.1"
    }
  }
}
