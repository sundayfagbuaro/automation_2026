from netapp_ontap import HostConnection
from netapp_ontap.resources import Volume, Snapshot
import urllib3
from datetime import datetime, timedelta, timezone

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

threshold = datetime.now(timezone.utc) - timedelta(days=1)

with HostConnection(
    host="10.10.1.221",
    username="auto_admin",
    password="P@ssWord1",
    verify=False
):
    
    vol = Volume.find(
        name="auto_vol_02",
        svm={"name": "nas_vserver"}
    )

    snapshots = Snapshot.get_collection(vol.uuid,fields="name,create_time")

    for snap in snapshots:
        if snap.create_time < threshold:
            print(snap.name)
            print(f"Deleting snapshot {snap.name}")
            snap.delete()
            print(f"{snap.name} deleted successfully")

