import netapp_ontap
from netapp_ontap import HostConnection
from netapp_ontap.resources import Svm

with HostConnection(
    host="10.10.1.221",
    username="auto_admin",
    password="P@ssWord1",
    verify=False
):
    
    for svm in Svm.get_collection():
        print(f"Vservers: {svm.name}")
