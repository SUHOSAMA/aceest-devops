# 🚀 ACEest Fitness API – DevOps CI/CD Project

## 📌 Project Overview

This project demonstrates a complete **CI/CD pipeline implementation** for a Flask-based application using modern DevOps tools. The goal is to automate build, test, containerization, and deployment using **Jenkins, Docker, and Kubernetes (Minikube)**.

---

## 🏗️ Architecture (CI/CD Flow)

```
Developer → GitHub → Jenkins → Docker → Docker Hub → Kubernetes (Minikube)
```

### Flow Explanation:

1. Developer pushes code to GitHub
2. Jenkins triggers pipeline
3. Application is tested using Pytest
4. Docker image is built
5. Image is pushed to Docker Hub
6. Kubernetes (Minikube) deploys the application

---

## 🛠️ Technologies Used

* **Backend:** Flask (Python)
* **CI/CD Tool:** Jenkins
* **Containerization:** Docker
* **Container Registry:** Docker Hub
* **Orchestration:** Kubernetes (Minikube)
* **Testing:** Pytest
* **Version Control:** Git & GitHub

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

## ⚙️ Setup & Execution

### 1️⃣ Clone Repository

```
git clone https://github.com/surekha111/aceest-devops.git
cd aceest-devops
```

---

### 2️⃣ Run Application Locally

```
pip install -r requirements.txt
python app.py
```

---

### 3️⃣ Run Tests

```
pytest
```

---

### 4️⃣ Build Docker Image

```
docker build -t aceest-app .
```

---

### 5️⃣ Push to Docker Hub

```
docker tag aceest-app surekha111/aceest-app
docker push surekha111/aceest-app
```

🔗 Docker Hub Link:
https://hub.docker.com/r/surekha111/aceest-app

---

### 6️⃣ Deploy using Minikube

```
minikube start
minikube docker-env | Invoke-Expression

kubectl create deployment aceest-app --image=surekha111/aceest-app
kubectl expose deployment aceest-app --type=NodePort --port=5000

minikube service aceest-app
```

---

## ✅ Application Output

When accessed via browser:

```
{
  "message": "ACEest Fitness API is running"
}
```

---

## 🔁 Jenkins Pipeline

The Jenkins pipeline automates:

* Code checkout
* Dependency installation
* Running tests
* Docker image build
* Deployment steps

Pipeline is defined in:

```
Jenkinsfile
```

---

##  Testing

* Implemented using **Pytest**
* Ensures application reliability before deployment

---

##  Deployment Strategy

* **POC Deployment:** Minikube (Local Kubernetes)
* **Production Strategy:** Docker Hub + Cloud Kubernetes (AWS/EKS concept)

---

## ⚠️ Challenges Faced & Solutions

| Challenge                            | Solution                                |
| ------------------------------------ | --------------------------------------- |
| Docker daemon not connecting         | Restarted Docker Desktop                |
| ImagePullBackOff error               | Pushed image to Docker Hub              |
| Minikube slow startup                | Allowed time for cluster initialization |
| PowerShell command issues            | Used correct syntax and quoting         |
| Kubernetes not detecting local image | Used Docker Hub image instead           |

---

##  Key Outcomes

* Automated CI/CD pipeline using Jenkins
* Containerized application using Docker
* Deployed application using Kubernetes
* Successfully exposed service using Minikube
* Verified application via browser

---

## 📸 Proof of Execution

Screenshots included in submission document:

* Jenkins pipeline execution
* Docker image build
* Docker Hub repository
* Kubernetes deployment
* Application running in browser

---

## 🔗 GitHub Repository

https://github.com/surekha111/aceest-devops

---

##  Conclusion

This project successfully demonstrates an end-to-end DevOps pipeline integrating **CI/CD, containerization, and orchestration**, fulfilling all assignment requirements.

---
