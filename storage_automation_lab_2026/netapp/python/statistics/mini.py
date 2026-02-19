import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CLUSTER = "https://10.10.1.221"  # Make sure https:// is included
USER = "auto_admin"
PASSWORD = "P@ssWord1"

url = f"{CLUSTER}/api/statistics/node"  # <-- note no /cluster/

# Safe counters for ONTAP 9.13
params = {
    "counter": [
        "cpu_busy",
        "disk_read_ops",
        "disk_write_ops",
        "disk_data_read",
        "disk_data_written"
    ]
}

response = requests.get(
    url,
    params=params,
    auth=HTTPBasicAuth(USER, PASSWORD),
    verify=False
)

data = response.json()

records = data.get("records", [])
if not records:
    print("No statistics returned. Check counters or endpoint for ONTAP 9.13.")
else:
    for rec in records:
        node = rec["instance"]["name"]
        print(f"Node: {node}")
        for counter in rec["counters"]:
            print(f"  {counter['name']}: {counter['value']}")
        print("-" * 40)
