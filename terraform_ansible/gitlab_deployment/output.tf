output "vm_ips" {
  value = [
    for vm in proxmox_vm_qemu.vm :
    vm.ssh_host
  ]
}