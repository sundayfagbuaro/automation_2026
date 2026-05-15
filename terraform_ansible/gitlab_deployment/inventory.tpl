[gitlab]
%{ for vm in vms ~}
${vm.name} ansible_host=${vm.ip} ansible_user=bobosunne
%{ endfor ~}

