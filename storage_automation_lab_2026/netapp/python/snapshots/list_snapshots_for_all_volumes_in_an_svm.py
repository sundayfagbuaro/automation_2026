from netapp_ontap.resources import Volume, Snapshot
from netapp_ontap import HostConnection

with HostConnection(
    host="10.10.1.221",
    username="auto_admin",
    password="P@ssWord1",
    verify=False
):
    for vol in Volume.get_collection(fields="name,size"):
        print(f"\nVolume Name: {vol.name}, Volume Size:{vol.size // (1024**2)}MB")  

        print("Volume Snapshots:")
        for snap in Snapshot.get_collection(vol.uuid):
            print(f"  - {snap.name}")
