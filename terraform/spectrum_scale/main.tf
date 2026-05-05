resource "proxmox_vm_qemu" "vm" {
  count       = 3
  name        = "${var.vm_name}-${count.index + 1}"
  target_node = var.target_node
  clone       = var.template_name
  full_clone  = true

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