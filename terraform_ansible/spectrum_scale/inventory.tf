#resource "local_file" "ansible_inventory" {
#  content = templatefile("${path.module}/inventory.tpl", {
#    ips = compact([
#      for vm in proxmox_vm_qemu.vm :
#      vm.ssh_host
#    ])
#  })

#  filename = "${path.module}/ansible/inventory.ini"
#}

resource "local_file" "ansible_inventory" {
  content = templatefile("${path.module}/inventory.tpl", {
    vms = [
      for idx, vm in proxmox_vm_qemu.vm : {
        name = "scale-node-${idx + 1}"
        ip   = vm.ssh_host
      }
    ]
  })

  filename = "${path.module}/ansible/inventory.ini"
}