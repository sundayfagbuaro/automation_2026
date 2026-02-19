Test using Ansible (simple ping-equivalent)

# On your Ansible host, install the NetApp collection:

    ansible-galaxy collection install netapp.ontap

# Create a quick test pplaybook
    ---
- name: Test ONTAP connectivity
  hosts: localhost
  gather_facts: no
  collections:
    - netapp.ontap

  vars:
    hostname: "<cluster_mgmt_ip>"
    username: "admin"
    password: "your_password"
    https: true
    validate_certs: false

  tasks:
    - name: Get cluster info
      na_ontap_rest_info:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        https: "{{ https }}"
        validate_certs: false

# You can define the variables in the playbook directly or put them in the inventory file and leave only the task in the playbook

# Create a group_var file
    mkdir group_var && touch group_var/ontap-dev

# If you want vault encryption
    ansible-vault encrypt_string 'your_password' --name 'ontap_password'


# Reference Variable in your playbook
---
- name: Test ONTAP connectivity
  hosts: ontap
  gather_facts: no
  collections:
    - netapp.ontap

  tasks:
    - name: Get cluster info
      na_ontap_rest_info:
        hostname: "{{ ansible_host }}"
        username: "{{ ontap_username }}"
        password: "{{ ontap_password }}"
        https: "{{ ontap_https }}"
        validate_certs: "{{ ontap_validate_certs }}"

# Run the plkaybook
    ansible-playbook -i inventory.yml playbooks/test_ontap.yml


Notes:

hostname: "{{ ansible_host }}" pulls from the inventory

Group variables ontap_username, ontap_password, etc., are automatically available


If you used vault-encrypted ontap_password, add to the command or the encryption comand:

--ask-vault-pass or --vault-password-file ~/.ansible_vault_pass


# Test variable resolution:

    ansible ontap -i netapp/ansible/inventory-test.yml -m debug -a "var=ontap_username"

    ansible ontap -i netapp/ansible/inventory-test.yml -m debug -a "var=ontap_vserver"

# To see the directory and file structure 
    ansible-inventory -i netapp/ansible/inventory-test.yml --graph

# To see if the inventory file is being loaded
    ansible-inventory -i netapp/ansible/inventory-new.yml --list

# To see the inventory variable values
    ansible ontap-dev -i netapp/ansible/inventory-new.yml -m debug -a "var=ontap_username"



+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Setting variables - Most powerful from bottom to top
roles/app/defaults   → safe defaults
group_vars           → environment intent
host_vars            → special cases
set_fact              → runtime logic only
-e                    → emergency overrides


# 🧠 Ansible Variable Precedence — One-Page Cheat Sheet
Highest → Lowest precedence
-e (extra vars)                    🥇
set_fact / registered vars         🥈
role vars (roles/*/vars)           🥉
play vars / include_vars
host_vars
group_vars
role defaults (roles/*/defaults)   🧊
facts (ansible_*)

# Rules to remember
Higher always wins
Same level → last loaded wins
Facts are weak
Role vars are dangerously strong

# Identity & Connection (memorize this)
inventory_hostname = Ansible identity (always exists)
ansible_host       = connection address
ansible_hostname   = OS hostname (fact)
ansible_user       = login user

# Safe defaults pattern (gold standard)
roles/*/defaults   → baseline
group_vars         → environment intent
host_vars          → exceptions
set_fact           → runtime logic only
-e                 → emergencies

# 🧪 Debug commands you should always know
- debug:
    var: myvar

ansible-playbook site.yml -vvv

Look for:

myvar was set by ...

- debug:
    var: nginx_port

ansible-playbook site.yml -vvv

Look for:

nginx_port was set by ...