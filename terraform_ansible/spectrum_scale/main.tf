resource "proxmox_vm_qemu" "vm" {
  count       = 2
  name        = "${var.vm_name}-${count.index + 1}"
  target_node = var.target_node
  clone       = var.template_name
  full_clone  = true
  
  agent                  = 1
  define_connection_info = true
  ci_wait                = 60
  ciuser = "bobosunne"


  os_type = "cloud-init"

  cores   = 2
  sockets = 1
  memory  = 2048

  scsihw = "virtio-scsi-pci"

  network {
    model  = "virtio"
    bridge = "vmbr0"
  }

  ipconfig0 = "ip=dhcp"

  sshkeys = file("~/.ssh/id_rsa.pub")
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
