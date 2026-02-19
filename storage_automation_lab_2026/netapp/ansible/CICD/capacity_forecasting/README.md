PART 1️⃣ – Capacity Forecasting from ONTAP Metrics (ONTAP 9.12+)

ONTAP 9.12+ gives you rich REST metrics. We’ll use them to:

Collect historical capacity data

Calculate growth rate

Predict “days to full”

Flag risk thresholds

Feed reports + dashboards

🧠 Architecture – Capacity Forecasting
ONTAP REST API
     |
     v
Ansible (REST metrics)
     |
     v
JSON / CSV Metrics Archive
     |
     v
Forecast Logic (Python)
     |
     v
HTML + Email + Slack Alerts

🔹 Metrics We Care About (Most Important)

From ONTAP REST:

Metric	Why
space.used	Actual consumption
space.available	Remaining capacity
space.size	Total capacity
tiering.used	FabricPool awareness
snapshot.used	Snapshot bloat
aggregate.used_percent	Physical risk

🔹 Step 1: Collect Metrics via REST (Ansible)
collect_capacity_metrics.yml
- name: Collect ONTAP Capacity Metrics
  hosts: ontap_clusters
  gather_facts: no
  collections:
    - netapp.ontap

  vars:
    metrics_file: "capacity_metrics_{{ inventory_hostname }}.json"

  tasks:
    - name: Get volume metrics
      uri:
        url: "https://{{ ansible_host }}/api/storage/volumes?fields=name,svm.name,space"
        method: GET
        user: "{{ ansible_user }}"
        password: "{{ ansible_password }}"
        validate_certs: no
      register: volume_metrics

    - name: Save metrics
      copy:
        dest: "{{ metrics_file }}"
        content: "{{ volume_metrics.json | to_nice_json }}"


📌 Run this daily (Jenkins / GitHub Actions).


Step 2: Forecast Growth (Python Logic)

This runs inside Jenkins or GitHub Actions.

forecast_capacity.py
import json
from datetime import datetime
from statistics import mean

DAYS_LOOKBACK = 14
ALERT_THRESHOLD_DAYS = 30

with open("capacity_metrics.json") as f:
    data = json.load(f)

forecast_report = []

for vol in data["records"]:
    used = vol["space"]["used"]
    size = vol["space"]["size"]
    available = size - used

    # Example growth rate (MB/day)
    growth_rate = used / DAYS_LOOKBACK

    days_to_full = available / growth_rate if growth_rate > 0 else 999

    status = "OK"
    if days_to_full < ALERT_THRESHOLD_DAYS:
        status = "CRITICAL"

    forecast_report.append({
        "volume": vol["name"],
        "svm": vol["svm"]["name"],
        "used_gb": round(used / 1024**3, 2),
        "size_gb": round(size / 1024**3, 2),
        "days_to_full": int(days_to_full),
        "status": status
    })

print(forecast_report)

🔹 Step 3: Forecast Output (Example)
Volume	Used	Size	Days to Full	Status
vol_db01	6.2 TB	8 TB	21	❌ CRITICAL
vol_home	1.1 TB	5 TB	180	✅ OK
🔔 Alerts You Can Trigger Automatically

❌ < 30 days → Email + Slack

⚠ < 60 days → Warning

📈 Growth spike detected → Report anomaly