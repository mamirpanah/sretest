data "arvan_server_groups" "server_group_list" {
  region = var.region
}

data "arvan_networks" "terraform_network" {
  region = var.region
}

data "arvan_images" "terraform_image" {
  region     = var.region
  image_type = "distributions" // or one of: arvan, private
}

data "arvan_plans" "plan_list" {
  region = var.region
}

data "arvan_security_groups" "default_security_groups" {
  region = var.region
}

locals {
  chosen_image = try([for image in data.arvan_images.terraform_image.distributions : image
  if image.distro_name == var.chosen_distro_name && image.name == var.chosen_name][0], null)
  sretest_group = one([
    for g in data.arvan_security_groups.default_security_groups.groups :
    g.id if g.name == "sretest"
  ])
}

resource "arvan_network" "terraform_private_network" {
  region      = var.region
  description = "Terraform-created private network"
  name        = "tf_private_network"
  dhcp_range = {
    start = "10.255.255.19"
    end   = "10.255.255.150"
  }
  dns_servers    = ["195.216.58.16", "5.254.197.224", "1.1.1.1"]
  enable_dhcp    = true
  enable_gateway = true
  cidr           = "10.255.255.0/24"
  gateway_ip     = "10.255.255.1"
}

resource "arvan_abrak" "built_by_terraform" {
  depends_on = [arvan_network.terraform_private_network]
  timeouts {
    create = "1h30m"
    update = "2h"
    delete = "20m"
    read   = "10m"
  }
  region       = var.region
  name         = "built-by-terraform-${count.index + 1}"
  ssh_key_name = "sretestkey"
  count        = 3
  image_id     = local.chosen_image.id
  flavor_id    = var.chosen_plan_id
  disk_size    = 25
  networks = [
    {
      network_id = arvan_network.terraform_private_network.network_id
    }
  ]
  security_groups = [local.sretest_group]
}