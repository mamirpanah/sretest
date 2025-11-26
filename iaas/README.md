# IaaS Directory

This directory contains Terraform configurations for provisioning infrastructure on ArvanCloud.

## Overview

This Terraform setup uses the ArvanCloud provider to bring up three virtual machines within a private network. The network is secured by a firewall that allows SSH (port 22), ICMP protocol, and TCP ports ranging from 30000 to 33000.

## Prerequisites

- Ensure you have [Terraform](https://www.terraform.io/downloads.html) installed.
- You need an ArvanCloud account and an API key.

## Configuration

Before applying the Terraform configuration, you need to provide your ArvanCloud API key. You can do this in one of two ways:

1. **Using a `terraform.tfvars` file**:
   Create a file named `terraform.tfvars` in this directory with the following content:

   ```hcl
   arvan_api_key = "YOUR_ARVANCLOUD_API_KEY"
   ```

2. **Using Environment Variables**:
   Alternatively, you can set the API key as an environment variable:

   ```bash
   export TF_VAR_arvan_api_key="YOUR_ARVANCLOUD_API_KEY"
   ```

## Usage

1. **Initialize the Terraform configuration**:

   ```bash
   terraform init
   ```

2. **Validate the configuration**:

   ```bash
   terraform validate
   ```

2. **Apply the Terraform configuration to provision the resources**:

   ```bash
   terraform apply
   ```

Review the proposed changes and type yes to confirm.

## Additional Information

- Refer to the individual .tf files for detailed configurations and variable definitions.