# 🚀 ACEest Fitness API – DevOps CI/CD Implementation

---

## 📌 Project Overview

This project demonstrates a complete **CI/CD pipeline** for a Flask-based application using DevOps tools such as Jenkins, Docker, Kubernetes (Minikube), and Docker Hub.

The pipeline automates:

* Build
* Test
* Containerization
* Deployment

---

## 🏗️ CI/CD Architecture

```text
Developer → GitHub → Jenkins → Docker → Docker Hub → Kubernetes (Minikube)
```

---

## 🛠️ Tools & Technologies

* Python (Flask)
* Jenkins (CI/CD)
* Docker (Containerization)
* Docker Hub (Image Registry)
* Kubernetes – Minikube (Deployment)
* Pytest (Testing)
* Git & GitHub (Version Control)

---

## 📂 Project Structure

```
aceest-devops/
│── app.py
│── requirements.txt
│── Dockerfile
│── Jenkinsfile
│── README.md
│
├── tests/
│   └── test_app.py
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
```

---

## ⚙️ Implementation Steps

### 1. Clone Repository

```
git clone https://github.com/surekha111/aceest-devops.git
cd aceest-devops
```

---

### 2. Run Application

```
pip install -r requirements.txt
python app.py
```

---

### 3. Run Tests

```
pytest
```

---

### 4. Docker Build

```
docker build -t aceest-app .
```

---

### 5. Docker Hub Integration

Docker image pushed with versions:

* surekha111/aceest-app:latest
* surekha111/aceest-app:v1
* surekha111/aceest-app:v2

```
docker push surekha111/aceest-app
```

🔗 Docker Hub:
https://hub.docker.com/r/surekha111/aceest-app

---

## ☸️ Kubernetes Deployment (Minikube – POC)

### Commands:

```
minikube start

kubectl create deployment aceest-app --image=surekha111/aceest-app
kubectl expose deployment aceest-app --type=NodePort --port=5000

minikube service aceest-app
```

---

## 🌐 Endpoint URL

Application successfully deployed and accessed via:

```
http://127.0.0.1:50526
```

---

## 🔁 Deployment Strategy

* Deployment: Kubernetes Deployment
* Service: NodePort
* Rolling Update: Supported using `kubectl set image`

---

## 🔄 Jenkins CI/CD Pipeline

Jenkins pipeline includes:

* Code checkout
* Dependency installation
* Pytest execution
* Docker build
* Deployment

Pipeline executed successfully for latest commits.

---

## 🧪 Testing

* Implemented using Pytest
* All test cases passed successfully

---

## 📊 SonarQube Code Quality

SonarQube integration was designed for static code analysis to ensure:

* Code quality
* Maintainability
* Bug detection

Due to environment constraints, analysis is demonstrated conceptually along with clean code practices and testing validation.

---

## 🚀 Key Outcomes

* Automated CI/CD pipeline
* Containerized application
* Kubernetes deployment
* Public Docker image
* Verified endpoint output

---

## 📸 Proof

Screenshots included in submission:

* Jenkins build success
* Docker image push
* Kubernetes pods running
* Application output

---

## 🔗 Repository Access

This repository is public and accessible:

https://github.com/surekha111/aceest-devops

---

## 📌 Conclusion

The project successfully demonstrates a complete DevOps lifecycle with CI/CD automation, containerization, and Kubernetes deployment fulfilling all assignment requirements.

---
