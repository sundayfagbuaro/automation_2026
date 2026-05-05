resource "local_file" "ansible_inventory" {
  #filename = "${path.module}/spce-scale-inv.ini"
  filename = "ansible/inventory.ini"

  depends_on = [proxmox_vm_qemu.vm]

  content = <<EOT
[spec-scale]
%{ for vm in proxmox_vm_qemu.vm ~}
${vm.default_ipv4_address} ansible_user=bobosunne
%{ endfor ~}
EOT
}