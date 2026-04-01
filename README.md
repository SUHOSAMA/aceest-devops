# ACEest DevOps Project 🚀

## 📌 Overview

This project demonstrates a complete DevOps lifecycle using a simple **Flask-based Fitness API**.

It includes:

* REST API built with Flask
* Automated testing using Pytest
* Containerization using Docker
* CI/CD pipeline using GitHub Actions

---

## 🛠️ Tech Stack

* Python (Flask)
* Pytest
* Docker
* GitHub Actions

---

## 📂 Project Structure

```
aceest-devops/
│
├── app.py
├── requirements.txt
├── Dockerfile
│
├── tests/
│   └── test_app.py
│
└── .github/
    └── workflows/
        └── main.yml
```

---

## ▶️ How to Run Locally

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run the application

```
python app.py
```

### 3. Access API

```
http://127.0.0.1:5000/
```

---

## 🧪 Run Tests

```
pytest
```

---

## 🐳 Docker Setup

### Build image

```
docker build -t aceest-app .
```

### Run container

```
docker run -p 5000:5000 aceest-app
```

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

The pipeline automatically runs on every push to the `main` branch.

### Steps:

1. Checkout code
2. Install dependencies
3. Run tests (pytest)
4. Build Docker image

---

## 🎯 Key Features

* Automated testing before deployment
* Containerized application for consistency
* Continuous Integration using GitHub Actions
* Simple and clean API design

---

## 🧠 DevOps Workflow

1. Developer pushes code to GitHub
2. GitHub Actions triggers pipeline
3. Tests are executed
4. Docker image is built
5. Pipeline passes or fails

---


## ✅ Conclusion

This project successfully demonstrates an end-to-end DevOps pipeline including development, testing, containerization, and continuous integration.

---
