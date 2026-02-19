Recommended Ansible Project Structure
ansible/
│
├── inventory/
│   └── hosts.ini
│
├── group_vars/
│   └── monitoring.yml
│
├── roles/
│   └── monitoring/
│       ├── tasks/
│       │   └── main.yml
│       └── templates/
│           └── values.yaml.j2
│
└── site.yml


ansible-playbook -i inventory/hosts.ini site.yml