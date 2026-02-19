from datetime import datetime, timedelta
from netapp_ontap.resources import Snapshot

threshold = datetime.now() - timedelta(days=7)

for snap in Snapshot.get_collection():
    if snap.create_time < threshold:
        snap.delete()
