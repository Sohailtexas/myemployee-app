# Docker Installation (Ubuntu)

Official:
https://docs.docker.com/engine/install/ubuntu/

## Install
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update




# Install Docker
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

## Verify

docker --version
docker run hello-world

## Common Commands

docker ps
docker images
docker build -t myapp .
docker run -d -p 5000:5000 myapp
docker stop <container-id>
docker rm <container-id>
docker rmi <image-id>
docker push myacr.azurecr.io/myapp:v1
