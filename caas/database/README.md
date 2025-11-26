Postgres Cluster
===========

Simple Ansible setup to deploy a Postgres cluster on kubernetes.

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
- playbooks/postgres-operator.yml — top-level playbook to bootstrap postgres operator
- playbooks/postgres-cluster.yml — top-level playbook to bootstrap postgres cluster
- roles/
  - install-postgres-operator — installs & configures postgres operator with Zalando helm chart
  - install-postgres-cluster — create 3 node postgres cluster 1 master + 2 slaves

Quickstart
----------
1. Review and update inventory: inventories/hosts.ini
2. Adjust cluster variables in group_vars/all.yml
3. Run the playbook:
    - cd sretest/caas/database
    - ansible-playbook playbooks/postgres-operator.yml
    - ansible-playbook playbooks/postgres-cluster.yml

Using ansible.cfg to avoid -i
-----------------------------
Set the inventory path in ansible.cfg under the [defaults] section so you can omit -i:

Example snippet for ansible.cfg:
[defaults]
inventory = inventories/hosts.ini
remote_user = your_ssh_user
# optional: private_key_file, vault_password_file, forks, etc.

With that in place, ansible-playbook will use inventories/hosts.ini automatically.

Idempotency & testing
---------------------
- Playbooks are written to be idempotent; re-running should not break the cluster.
- Verify cluster after run:
  - Check the pods: sudo k0s kubectl get pods -n services
  - Check the services: sudo k0s kubectl get svc -n services

Troubleshooting
---------------
- Ensure SSH connectivity and privilege escalation.
- Run with increased verbosity for troubleshooting: ansible-playbook -vvv playbooks/cluster.yml