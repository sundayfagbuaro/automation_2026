module "test_vm" {
#  source = "../../..terraform-modules/proxmox"
  source = "/Users/sundayfagbuaro/git/2026/sunny-lab/terraform-modules/proxmox"

  vm_name       = "test-vm"
  target_node   = "sunny-proxmox-01"
  template_name = "rocky-linux-template"
  os_type       = "cloud-init" 

#  ssh_keys        = file("~/.ssh/id_rsa.pub")
}
