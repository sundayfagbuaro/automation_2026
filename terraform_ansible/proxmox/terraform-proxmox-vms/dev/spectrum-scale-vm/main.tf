module "test_vm" {
#  source = "../../..terraform-modules/proxmox"
  source = "/Users/sundayfagbuaro/git/2026/sunny-lab/terraform-modules/proxmox"

  vm_name       = "my-test-vm"
  target_node   = "sunny-proxmox-01"
  template_name = "rocky-linux-template"
#  os_type       = "cloud-init" 

#  ssh_keys        = file("~/.ssh/id_rsa.pub")
}

resource "null_resource" "run_ansible" {
  depends_on = [
    module.test_vm,
    local_file.ansible_inventory
  ]

  provisioner "local-exec" {
    environment = {
      ANSIBLE_HOST_KEY_CHECKING = "False"
    }

    command = "ansible-playbook -i ansible/inventory.ini ansible/playbooks/main.yml"
  }
}