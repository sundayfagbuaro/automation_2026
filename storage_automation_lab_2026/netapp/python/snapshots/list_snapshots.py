from netapp_ontap import HostConnection
from netapp_ontap.resources import Volume, Snapshot
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with HostConnection(
    host="10.10.1.221",
    username="auto_admin",
    password="P@ssWord1",
    verify=False
):
    # Find the volume (get UUID)
    vol = Volume.find(
        name="auto_vol_02",
        svm={"name": "nas_vserver"}
    )

    if not vol:
        raise RuntimeError("Volume not found")

    # List snapshots in that volume
    for snap in Snapshot.get_collection(vol.uuid):
        print(snap.name)
