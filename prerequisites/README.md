# Prerequisites: Setting Up Docker and Docker Compose

This section guides you through setting up Docker and Docker Compose, which are essential for running Dify.

## **1. Setting the Stage: Installing Docker and Docker Compose**

### **What is Docker?**
Docker is a platform that helps you package applications and their dependencies into containers, ensuring they run reliably across different environments.


### **Install Docker and Docker Compose**
Follow these steps to install Docker:

- Follow [Docker's official installation guide](https://docs.docker.com/get-docker/) based on your operating system.

- Install Docker Compose using the instructions [here](https://docs.docker.com/compose/install/).


#### **For Windows/macOS**:
1. Download and install Docker Desktop from the [Docker official website](https://www.docker.com/products/docker-desktop).
2. Enable Docker Compose via Docker Desktop settings.

```
sudo apt-get install ca-certificates curl gnupg -y
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

```
```
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

Verify installations:
```bash
docker --version
docker-compose --version
```



---

Once completed, proceed to the `dify-setup/` directory.
