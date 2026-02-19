from purestorage import FlashArray

fa = FlashArray("PURE_IP", "admin", "password")

for vol in fa.list_volumes():
    print(vol["name"])
