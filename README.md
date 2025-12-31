# 🚀 Docker Project

A Python Flask web application containerized using Docker and deployed on an AWS EC2 (Ubuntu) instance.
This project demonstrates hands-on experience with Docker, cloud deployment, and web application development.

## 📌 Project Overview

Docker Project is a modern student registration web application built using Flask.
The application is containerized using Docker to ensure consistent execution across different environments and deployed on an AWS EC2 Ubuntu server.

## 🛠️ Technologies Used

1. Python 3
2. Flask
3. HTML
4. CSS
5. Docker
6. AWS EC2 (Ubuntu Instance)

## 📂 Project Structure
docker-project/
│
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build configuration
│
├── templates/
│   └── index.html          # HTML frontend
│
└── static/
    └── style.css           # CSS styling

## ✨ Features

1. 📦 Fully Dockerized Flask application
2. 🌐 Deployed on AWS EC2 Ubuntu server
3. 🎨 Modern and responsive UI
4. ⚡ Lightweight and easy to manage
5. 🔁 Consistent behavior across environments
---
## 🐳 Docker Usage
1️⃣ Build Docker Image
docker build -t docker-project .

2️⃣ Run Docker Container
docker run -d -p 8080:8080 docker-project

3️⃣ Access the Application
http://<EC2-PUBLIC-IP>:8080

🧾 Dockerfile
FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN pip install -r reqirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
---
## ☁️ AWS EC2 (Ubuntu) Deployment Steps

1️⃣Launch an AWS EC2 Ubuntu instance

2️⃣Connect to the instance using SSH

3️⃣Install Docker:
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker

4️⃣Upload or clone the project repository

5️⃣Build and run the Docker container

6️⃣Open port 8080 in the EC2 Security Group
---
## 🔌 Port Configuration

1. Application runs on port 8080
2. Docker maps container port to host port
3. Ensure inbound rule for port 8080 is enabled in the EC2 Security Group
---
## 🧠 Learning Outcomes

1. Docker image creation and container execution
2. Deploying Flask applications on Ubuntu servers
3. Cloud deployment using AWS EC2
4. Port mapping and basic networking
5. Managing server-level configurations

---
## 📄 License

This project is created for educational and learning purposes and is free to use or modify.
---
## 📊Output 
THe Final Result can be access by http://<EC2-PUBLIC-IP>:8080 
