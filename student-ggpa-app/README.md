# Student GGPA Flask Application

## Overview

This project is a full-stack Flask web application that allows students to:

* Register accounts
* Login securely
* View their GGPA

The application is containerized using Docker and can be deployed into a Kubernetes cluster.

---

# Architecture

Frontend

* HTML
* Bootstrap

Backend

* Flask
* Flask-Login
* SQLAlchemy

Infrastructure

* Docker
* Kubernetes

---

# Running Locally

## 1 Install dependencies

```
pip install -r requirements.txt
```

## 2 Run application

```
flask run
```

Open:

```
http://localhost:5000
```

---

# Docker Build

Build the container:

```
docker build -t ggpa-app .
```

Run locally:

```
docker run -p 5000:5000 ggpa-app
```

---

# Push to DockerHub

```
docker tag ggpa-app yourdockerhubusername/ggpa-app
docker push yourdockerhubusername/ggpa-app
```

---

# Kubernetes Deployment

Apply manifests:

```
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Verify pod:

```
kubectl get pods -n ggpa-system
```

Get service:

```
kubectl get svc -n ggpa-system
```

Access application:

```
http://NODE_IP:30007
```

---

# Future Improvements

* Admin dashboard
* Postgres database
* Persistent volume for database
* Helm chart
* CI/CD pipeline
* Authentication tokens

---
