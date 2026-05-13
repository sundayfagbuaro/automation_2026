terraform {
  required_providers {
    proxmox = {
      source  = "Telmate/proxmox"
      version = "2.9.14"
#      version = ">= 3.0.1"
    }
  }
}

provider "proxmox" {
  pm_api_url      = "https://192.168.1.81:8006/api2/json"
  pm_api_token_id = "terraform@pam!terraform"
  pm_api_token_secret = "5f7b6c9f-01d9-413f-ba63-957247dd74a2"

  pm_tls_insecure = true
}
