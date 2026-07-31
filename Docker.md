# Docker Installation (Ubuntu)

Official:
https://docs.docker.com/engine/install/ubuntu/

## Install

sudo apt update
sudo apt install ca-certificates curl

# Add Docker GPG key
...

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
