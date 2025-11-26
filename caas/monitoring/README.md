Monitoring System
===========

Simple Ansible setup to deploy a monitoring system on kubernetes with prometheus stack and grafana.

Prerequisites
-------------
- Control machine with Ansible 2.9+ (or newer).
- SSH access to target hosts with a user that can escalate to root (become).
- Python installed on target hosts (for Ansible).
- Inventory configured at `inventories/hosts.ini`.
- `ansible.cfg` is included and configured for this repo.

Repository layout
-----------------
- ansible.cfg — repo Ansible configuration
- inventories/hosts.ini — host inventory
- group_vars/all.yml — global variables
- playbooks/grafana-prometheus.yml — top-level playbook to bootstrap Prometheus and Grafana operator
- playbooks/grafana-dashboards.yml — to configure grafana dashboards and datasources
- roles/
  - install-grafana-prometheus-stack — installs & configures prometheus and grafana operator
  - configure-grafana-dashboards — configures grafana dashboards and datasources

Quickstart
----------
1. Review and update inventory: inventories/hosts.ini
2. Adjust cluster variables in group_vars/all.yml
3. Run the playbook:
    - cd sretest/caas/monitoring
    - ansible-playbook playbooks/grafana-prometheus.yml
    - ansible-playbook playbooks/grafana-dashboards.yml

Using ansible.cfg to avoid -i
-----------------------------
Set the inventory path in ansible.cfg under the [defaults] section so you can omit -i:

Example snippet for ansible.cfg:
[defaults]
inventory = inventories/hosts.ini
remote_user = your_ssh_user
# optional: private_key_file, vault_password_file, forks, etc.

With that in place, ansible-playbook will use inventories/hosts.ini automatically.

