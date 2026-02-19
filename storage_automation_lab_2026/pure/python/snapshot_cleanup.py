from purestorage import FlashArray
from datetime import datetime, timedelta

fa = FlashArray("PURE_IP", "admin", "password")
threshold = datetime.utcnow() - timedelta(days=7)

for snap in fa.list_volume_snapshots():
    if snap["created"] < threshold:
        fa.destroy_volume(snap["name"])
