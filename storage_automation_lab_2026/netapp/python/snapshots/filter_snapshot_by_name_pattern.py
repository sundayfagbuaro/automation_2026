from netapp_ontap import HostConnection
from netapp_ontap.resources import Volume, Snapshot
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

snap_name = f"auto_snap_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

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

    for snap in Snapshot.get_collection(vol.uuid, name="hourly*"):
        print(snap.name)


