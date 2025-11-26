# CaaS Directory

This directory contains Ansible playbooks for deploying a Kubernetes cluster and associated applications.

## Overview

This setup includes the following components:

1. **[Database](database/README.md)**: This directory is for the PostgreSQL cluster that uses the Zalando operator. It consists of one master and two slaves, with Patroni handling failover of the master. We have a connection pooler for the master for read and write operations, and a connection pooler for replication that load balances the reads from the slaves.

2. **[Monitoring](monitoring/README.md)**: This directory contains Ansible playbooks to bring up the kube-prometheus-stack and Grafana operator, along with dashboards and data sources manifests, as well as the PrometheusRule manifest.

3. **[GeoIP API](geoip-api/README.md)**: This directory contains the Helm chart of the GeoIP application, which is used in a CI/CD playbook.

4. **[K0s](k0s/README.md)**: This directory includes Ansible playbooks to bring up a simple Kubernetes cluster with one master and two worker nodes. It uses OpenEBS as storage, referenced as a K0s extension.

## Usage

1. Ensure you have [Ansible](https://www.ansible.com/resources/get-started) installed.
2. Update the inventory files and variable configurations as needed for each component.
3. Run the appropriate playbooks for each component to deploy the infrastructure and applications.

## Additional Information

Refer to the individual directories for detailed instructions and configurations for each component.