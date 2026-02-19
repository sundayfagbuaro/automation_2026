import netapp_ontap
from netapp_ontap import HostConnection
from netapp_ontap.resources import Volume

with HostConnection(
    host="10.10.1.221",
    username="auto_admin",
    password="P@ssWord1",
    verify=False
):
    for vol in Volume.get_collection():
        print(f"Volume: {vol.name}")

print(netapp_ontap.__version__)
