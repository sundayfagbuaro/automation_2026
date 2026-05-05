resource "google_compute_instance" "web_vm" {
  name         = "web-server-vm"
  machine_type = "e2-micro"
  zone         = var.zone

  tags = ["web-server"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  
  attached_disk {
    source      = google_compute_disk.data_disk.id
    device_name = "data-disk"
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet1.id

    access_config {
      # Ephemeral public IP
    }
  }

metadata_startup_script = <<-EOF
#!/bin/bash

# Install nginx
apt-get update
apt-get install -y nginx

# Wait for disk
sleep 10

DISK="/dev/disk/by-id/google-data-disk"

# Partition disk
parted -s $DISK mklabel gpt
parted -s $DISK mkpart primary ext4 0% 100%

# Format partition
mkfs.ext4 ${DISK}-part1

# Create mount directory
mkdir -p /mnt/data

# Mount disk
mount ${DISK}-part1 /mnt/data

# Persist mount
echo "${DISK}-part1 /mnt/data ext4 defaults 0 0" >> /etc/fstab

# Create test page
echo "Hello from mounted disk" > /mnt/data/index.html

systemctl enable nginx
systemctl start nginx
EOF
}
