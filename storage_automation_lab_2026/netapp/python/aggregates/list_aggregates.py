import netapp_ontap
from netapp_ontap import HostConnection
from netapp_ontap.resources import Aggregate

with HostConnection(
    host="10.10.1.221",
    username="auto_admin",
    password="P@ssWord1",
    verify=False
):
    for aggr in Aggregate.get_collection():
        print(f"Aggegates: {aggr.name}")
    
