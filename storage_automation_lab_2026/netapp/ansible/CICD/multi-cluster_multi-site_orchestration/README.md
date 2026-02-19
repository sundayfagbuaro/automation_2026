

PART 2️⃣ – Multi-Cluster / Multi-Site Orchestration

Now the real power move 💪

🧠 Architecture – Multi-Site
Primary Cluster (DC1)
        |
        | SnapMirror (Async / Sync)
        |
Secondary Cluster (DC2)


Managed from one playbook, one CSV, one pipeline.

🔹 Inventory (Multiple Clusters)
[ontap_primary]
dc1 ansible_host=10.10.10.10 site=primary

[ontap_secondary]
dc2 ansible_host=10.20.20.20 site=dr

🔹 Multi-Cluster CSV

multisite_volumes.csv

svm,volume,size,primary_aggr,dr_aggr,mirror_policy
svm_prod,vol_db01,5TB,aggr1,aggr_dr1,MirrorAllSnapshots
svm_prod,vol_logs,2TB,aggr1,aggr_dr1,MirrorLatest

🔹 Orchestration Playbook
ontap_multisite_orchestration.yml
- name: Multi-Site ONTAP Orchestration
  hosts: ontap_primary
  gather_facts: no
  collections:
    - netapp.ontap

  vars_files:
    - multisite_volumes.csv

  tasks:
    - name: Create volume on primary
      na_ontap_volume:
        state: present
        name: "{{ item.volume }}"
        aggregate_name: "{{ item.primary_aggr }}"
        size: "{{ item.size }}"
        svm_name: "{{ item.svm }}"
      loop: "{{ volumes }}"

    - name: Create volume on DR
      delegate_to: dc2
      na_ontap_volume:
        state: present
        name: "{{ item.volume }}"
        aggregate_name: "{{ item.dr_aggr }}"
        size: "{{ item.size }}"
        svm_name: "{{ item.svm }}"
      loop: "{{ volumes }}"

    - name: Configure SnapMirror
      na_ontap_snapmirror:
        state: present
        source_svm: "{{ item.svm }}"
        source_volume: "{{ item.volume }}"
        destination_svm: "{{ item.svm }}"
        destination_volume: "{{ item.volume }}"
        policy: "{{ item.mirror_policy }}"
      loop: "{{ volumes }}"