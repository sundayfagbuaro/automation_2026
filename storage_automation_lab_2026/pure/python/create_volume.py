from purestorage import FlashArray

fa = FlashArray("PURE_IP", "admin", "password")
fa.create_volume("auto_vol1", 100)
print("Volume created")
