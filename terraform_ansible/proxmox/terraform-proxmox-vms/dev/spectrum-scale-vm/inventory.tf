resource "local_file" "ansible_inventory" {
  content = templatefile("${path.module}/inventory.tpl", {
    vms = module.test_vm.vms
  })

  filename = "${path.module}/ansible/inventory.ini"
}