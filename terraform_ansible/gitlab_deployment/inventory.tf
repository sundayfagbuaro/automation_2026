resource "local_file" "ansible_inventory" {
  content = templatefile("${path.module}/inventory.tpl", {
    vms = [
      for idx, vm in proxmox_vm_qemu.vm : {
        name = "gitlab-node"
        ip   = vm.ssh_host
      }
    ]
  })

  filename = "${path.module}/ansible/inventory.ini"
}