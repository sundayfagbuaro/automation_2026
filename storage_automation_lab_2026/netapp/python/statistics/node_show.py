from netapp_ontap import HostConnection, Statistics
from netapp_ontap.resources import Node
import time
import json
from dotenv import load_dotenv
import os

load_dotenv()

CLUSTER = os.getenv("HOST")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


NODE_COUNTERS = [
    "cpu_busy",
    "net_data_recv",
    "net_data_sent",
    "disk_data_read",
    "disk_data_written",
    "disk_read_ops",
    "disk_write_ops"
]

def get_node_metadata():
    nodes = {}
    for node in Node.get_collection(fields="name,model,serial_number"):
        nodes[node.name] = {
            "model": node.model,
            "serial": node.serial_number
        }
    return nodes

def get_node_stats():
    stats = Statistics.get_collection(
        object_name="node",
        counter_names=NODE_COUNTERS,
        instance_keys=["name"]
    )

    results = {}
    for stat in stats:
        name = stat.instance["name"]
        results[name] = stat.counters

    return results

with HostConnection(
    host=CLUSTER,
    username=USERNAME,
    password=PASSWORD,
    verify=False
):
    metadata = get_node_metadata()
    stats = get_node_stats()

    timestamp = int(time.time())

    output = []
    for node, counters in stats.items():
        entry = {
            "timestamp": timestamp,
            "node": node,
            **metadata.get(node, {}),
            **counters
        }
        output.append(entry)

    print(json.dumps(output, indent=2))
