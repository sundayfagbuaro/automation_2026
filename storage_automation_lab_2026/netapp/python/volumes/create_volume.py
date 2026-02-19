from netapp_ontap import HostConnection
from netapp_ontap.resources import Volume

with HostConnection(
    host="10.10.1.221",
    username="auto_admin",
    password="P@ssWord1",
    verify=False
):

    vol = Volume(
        name="auto_vol_02",
        svm={"name": "nas_vserver"},
        size=1 * 1024 * 1024 * 1024,  # 1GB
        style="flexvol",
        aggregates=[{"name": "aggr1"}]
    )

    vol.post()
    print(f"Volume {vol.name} created successfully")
