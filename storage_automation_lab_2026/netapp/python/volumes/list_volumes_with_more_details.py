import netapp_ontap
from netapp_ontap import HostConnection
from netapp_ontap.resources import Volume

with HostConnection(
    host="10.10.1.221",
    username="auto_admin",
    password="P@ssWord1",
    verify=False
):
    for vol in Volume.get_collection(fields="name,create_time,size,space.used_percent"):
        print(f"Volume Name: {vol.name}")
        print(f"Volume Created Time: {vol.create_time}")
        print(f"Volume Size: {vol.size // (1024**2)}MB")
        print(f"Volume Name: {vol.name.space.used_percent}")

