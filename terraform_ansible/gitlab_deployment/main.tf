resource "proxmox_vm_qemu" "vm" {
  count       = 1
  name        = var.vm_name
  target_node = var.target_node
  clone       = var.template_name
  full_clone  = true

  os_type = "cloud-init"

  cores   = 2
  sockets = 1
  memory  = 4096

  scsihw = "virtio-scsi-pci"

  network {
    model  = "virtio"
    bridge = "vmbr0"
  }

  ipconfig0 = "ip=dhcp"

}

resource "null_resource" "run_ansible" {

  depends_on = [
    local_file.ansible_inventory
  ]

  provisioner "local-exec" {
  environment = {
    ANSIBLE_HOST_KEY_CHECKING = "False"
  }

  command = "ansible-playbook -i ansible/inventory.ini ansible/playbooks/main.yml"
}
}
