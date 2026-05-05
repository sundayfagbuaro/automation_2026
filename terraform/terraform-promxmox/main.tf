resource "proxmox_vm_qemu" "ubuntu_vm" {

  name        = "ubuntu-tf-01"
  target_node = "sunny-proxmox-01"
  clone       = "ubuntu-2204-template"

  cores  = 2
  memory = 2048

  disk {
    size    = "32G"
    type    = "scsi"
    storage = "local-lvm"
  }

  network {
    model  = "virtio"
    bridge = "vmbr0"
  }

  os_type = "cloud-init"

  #ipconfig0 = "ip=192.168.1.50/24,gw=192.168.1.1"

  ciuser     = "ubuntu"
  sshkeys    = file("~/.ssh/id_rsa.pub")
}

resource "proxmox_vm_qemu" "my_vm" {
  target_node = "sunny-proxmox-01"
  vmid = 100
  # After import, fill in the rest to match your existing VM
}

resource "proxmox_vm_qemu" "Test-VM" {
  target_node = "sunny-proxmox-01"
  vmid = 112
  # After import, fill in the rest to match your existing VM
}

