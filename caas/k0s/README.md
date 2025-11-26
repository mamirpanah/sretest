k0s-ansible
===========

Simple Ansible setup to deploy a k0s Kubernetes cluster with Kuberouter networking.

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
- group_vars/all.yml — global variables (k0s settings)
- playbooks/cluster.yml — top-level playbook to bootstrap cluster
- roles/
  - k0s-controller — installs & configures k0s controller
  - k0s-worker — joins worker nodes to the cluster
  - k0s-common — for wipe out the k0s
  - helm-install - installs the helm client on the master node
  - kubectl-install - installs the kubectl client on the master node

Quickstart
----------
1. Review and update inventory: inventories/hosts.ini (controllers and workers).
2. Adjust cluster variables in group_vars/all.yml (k0s version, etc).
3. Run the playbook:
    - cd /sretest/caas/k0s
    - ansible-playbook playbooks/cluster.yml
    - ansible-playbook playbooks/cluster.yml -e "reset_cluster=true"

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
  - On a controller: sudo k0s kubectl get nodes
  - Check pods: sudo k0s kubectl get pods -A

Troubleshooting
---------------
- Ensure SSH connectivity and privilege escalation.
- Run with increased verbosity for troubleshooting: ansible-playbook -vvv playbooks/cluster.yml
- Confirm `k0s` service status on nodes: sudo systemctl status k0s

Notes
-----
- This repository is intentionally minimal; adapt variables and templates to your environment.
