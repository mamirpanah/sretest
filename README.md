# SRETest Project

This code space contains three main directories:

1. **[IaaS](iaas/README.md)**: This directory contains Terraform configurations for provisioning three virtual machines using the ArvanCloud provider.
2. **[CaaS](caas/README.md)**: This directory includes Ansible playbooks to set up a Kubernetes cluster with K0s, a PostgreSQL database cluster, and a monitoring system. It also contains the GeoIP API application, which is deployed using Helm charts via Ansible.
3. **[App](app/README.md)**: This directory contains the GeoIP API, a web API that processes IP requests to determine the request's country and exposes metrics.

Each directory has its own `README.md` file with specific instructions on how to use the resources within that directory.

## Getting Started

To get started, navigate to each directory and follow the instructions in their respective `README.md` files.