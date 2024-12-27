# Setting Up Dify

This section walks you through the setup process for Dify. Whether you're hosting on the cloud or self-hosting, follow these instructions step-by-step.

---

## Pre-Requisites

1. Docker and Docker Compose must be installed. (Refer to the `prerequisites/README.md` file for setup instructions.)
2. Basic familiarity with terminal commands (we'll keep it beginner-friendly).

---

## Cloud-Hosted Setup

1. **Sign Up on Dify Cloud**  
   Visit the [Dify Cloud website](https://dify.ai/) and create an account.

2. **Choose a Plan**  
   Select the appropriate pricing plan (free or paid based on your needs).

3. **Access the Dashboard**  
   Once logged in, access the dashboard to start integrating models and managing prompts.

---

## Self-Hosted Setup

1. **Clone the Repository**  
   Clone Dify's official repository:
   ```bash
   git clone https://github.com/langgenius/dify.git
   cd dify
   ```
2. **Run Dify Using Docker Compose**
  Execute the following commands to start Dify locally:
  
    ```bash
    docker-compose up -d
    ```
