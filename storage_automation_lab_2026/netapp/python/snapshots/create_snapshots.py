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
    # 1️⃣ Get the volume UUID
    vol = Volume.find(
        name="auto_vol_01",
        svm={"name": "nas_vserver"}
    )

    if not vol:
        raise RuntimeError("Volume not found")

    # 2️⃣ Create snapshot using volume UUID
    snapshot = Snapshot(
        name=snap_name,
        volume={"uuid": vol.uuid}
    )

    snapshot.post()
    print(f"Snapshot {snap_name} created successfully")
