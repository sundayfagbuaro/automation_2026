from netapp_ontap import HostConnection
from netapp_ontap.resources import Volume, Snapshot
from datetime import datetime
import csv
import urllib3
from dotenv import load_dotenv
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

CLUSTER = os.getenv("HOST")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SVM_NAME = "nas_vserver"


CSV_FILE = f"snapshots_{SVM_NAME}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

rows = []

with HostConnection(
    host=CLUSTER,
    username=USERNAME,
    password=PASSWORD,
    verify=False
):
    for vol in Volume.get_collection(fields="name,uuid"):
        for snap in Snapshot.get_collection(vol.uuid,fields="name,create_time,size"):
            rows.append([
                vol.name,
                snap.name,
                snap.create_time,
                snap.size // (1024 ** 2) if snap.size else 0
            ])

# -----------------------------
# Write CSV
# -----------------------------
with open(CSV_FILE, mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=" ")
#    writer = csv.writer(f)
    writer.writerow(["Volume", "Snapshot", "Create Time", "Size (MB)"])
    writer.writerows(rows)

print(f"\nCSV written to: {CSV_FILE}")

# -----------------------------
# Print Table (no dependencies)
# -----------------------------
print("\nSnapshots:\n")
print(f"{'Volume':20} {'Snapshot':30} {'Create Time':25} {'Size (MB)':10}")
print("-" * 90)

for r in rows:
    print(f"{r[0]:20} {r[1]:30} {str(r[2]):25} {r[3]:10}")
