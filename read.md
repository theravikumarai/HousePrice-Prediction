# House Price Prediction

An end-to-end machine learning application for predicting house prices. The project exposes a trained machine learning model through a FastAPI service, provides an interactive Streamlit interface, and demonstrates containerized deployment and orchestration using Docker and Kubernetes.

## Overview

The application follows a service-based architecture:

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Machine Learning Model:** CatBoost
- **Containerization:** Docker
- **Local Orchestration:** Docker Compose
- **Container Orchestration:** Kubernetes
- **Autoscaling:** Horizontal Pod Autoscaler (HPA)
- **Traffic Routing:** NGINX Ingress
- **Configuration Management:** ConfigMap and Kubernetes Secrets
- **Testing:** Pytest

The project demonstrates the complete workflow from machine learning model serving to containerized and Kubernetes-based deployment.

---

## Architecture

```text
                                User
                                  │
                                  ▼
                         house-price.local
                                  │
                                  ▼
                       NGINX Ingress Controller
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
                   /                          /api
                    │                           │
                    ▼                           ▼
          Frontend Kubernetes Service   Backend Kubernetes Service
                    │                           │
                    ▼                           ▼
             Streamlit Pods                 FastAPI Pods
                                                │
                                                ▼
                                          CatBoost Model
````

### Request Flow

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ▼
Machine Learning Model
  │
  ▼
Predicted House Price
```

---

## Technology Stack

| Category          | Technology                |
| ----------------- | ------------------------- |
| Language          | Python                    |
| Machine Learning  | CatBoost                  |
| Backend           | FastAPI                   |
| Frontend          | Streamlit                 |
| API Server        | Uvicorn                   |
| Containerization  | Docker                    |
| Local Development | Docker Compose            |
| Orchestration     | Kubernetes                |
| Autoscaling       | Horizontal Pod Autoscaler |
| Traffic Routing   | NGINX Ingress             |
| Configuration     | ConfigMap                 |
| Secret Management | Kubernetes Secrets        |
| Resource Metrics  | Metrics Server            |
| Testing           | Pytest                    |

---

## Repository Structure

```text
HousePrice-Prediction/
│
├── .github/                     # CI/CD workflows
│
├── app/                         # FastAPI backend application
│
├── frontend/                    # Streamlit frontend application
│
├── models/                      # Trained machine learning models
│
├── tests/                       # Test suite
│
├── k8s/                         # Kubernetes manifests
│   │
│   ├── backend/                 # Backend deployment, service, HPA
│   │
│   ├── config/                  # ConfigMap and Secret
│   │
│   ├── frontend/                # Frontend deployment and service
│   │
│   ├── ingress/                 # Ingress configuration
│   │   └── ingress.yaml
│   │
│   └── namespace.yaml
│
├── .env                         # Local environment variables
├── .gitignore
├── docker-compose.yml
├── dockerfile                   # Backend Docker image
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Features

* House price prediction using a trained CatBoost model
* REST API built with FastAPI
* Interactive web interface built with Streamlit
* Docker-based application containerization
* Multi-container local deployment with Docker Compose
* Kubernetes Deployments and Services
* Liveness and readiness probes
* ConfigMap-based application configuration
* Kubernetes Secret integration
* Horizontal Pod Autoscaling
* Resource monitoring using Metrics Server
* NGINX Ingress-based routing
* Rolling updates and deployment rollback
* Automated testing with Pytest

---

# Getting Started

## Prerequisites

The following tools are required:

* Python 3.12+
* Docker
* Docker Compose
* Kubernetes
* kubectl

---

## Clone the Repository

```bash
git clone <repository-url>
cd HousePrice-Prediction
```

---

## Local Development

### Create a Virtual Environment

#### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Backend

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

---

## Run the Frontend

Start the Streamlit application:

```bash
streamlit run frontend/app.py
```

The frontend will be available at:

```text
http://localhost:8501
```

---

# Docker

## Build the Backend Image

```bash
docker build -t raviikrds/house-price-backend:latest .
```

Run the backend container:

```bash
docker run -p 8000:8000 raviikrds/house-price-backend:latest
```

## Build the Frontend Image

```bash
docker build -t house-price-frontend ./frontend
```

Run the frontend container:

```bash
docker run -p 8501:8501 house-price-frontend
```

---

# Docker Compose

The frontend and backend can be started together using Docker Compose.

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d --build
```

Stop the services:

```bash
docker compose down
```

---

# Kubernetes

The application is deployed using the following Kubernetes resources:

* Namespace
* Deployment
* Service
* ConfigMap
* Secret
* Horizontal Pod Autoscaler
* Ingress

## Deploy the Application

Create the namespace:

```bash
kubectl apply -f k8s/namespace.yaml
```

Apply configuration:

```bash
kubectl apply -f k8s/config/
```

Deploy the backend:

```bash
kubectl apply -f k8s/backend/
```

Deploy the frontend:

```bash
kubectl apply -f k8s/frontend/
```

Configure ingress:

```bash
kubectl apply -f k8s/ingress/
```

Verify the deployment:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get ingress
```

---

# Application Routing

The application uses NGINX Ingress to expose both services through a single entry point.

```text
http://house-price.local
```

Routing configuration:

```text
/       → Streamlit Frontend
/api    → FastAPI Backend
```

The backend API documentation is available at:

```text
http://house-price.local/api/docs
```

---

# Horizontal Pod Autoscaling

The backend service is configured with a Horizontal Pod Autoscaler.

```text
Minimum Replicas: 2
Maximum Replicas: 5
Target CPU Utilization: 50%
```

Monitor autoscaling:

```bash
kubectl get hpa
```

Watch scaling activity:

```bash
kubectl get hpa -w
```

Monitor pod creation:

```bash
kubectl get pods -w
```

---

# Resource Monitoring

The Kubernetes Metrics Server enables resource monitoring.

Check node usage:

```bash
kubectl top nodes
```

Check pod usage:

```bash
kubectl top pods
```

---

# Health Checks

The backend exposes a health endpoint:

```http
GET /health
```

Kubernetes uses this endpoint for:

* **Liveness Probe** — Determines whether a container should be restarted.
* **Readiness Probe** — Determines whether a pod is ready to receive traffic.

```text
Container
    │
    ▼
Readiness Probe
    │
    ├── Healthy → Receives Traffic
    │
    └── Unhealthy → Removed from Service Endpoints
```

---

# Deployment Strategy

## Rolling Update

Update the backend image:

```bash
kubectl set image deployment/house-price-backend \
backend=raviikrds/house-price-backend:<version>
```

Monitor the rollout:

```bash
kubectl rollout status deployment/house-price-backend
```

View deployment history:

```bash
kubectl rollout history deployment/house-price-backend
```

---

## Rollback

Rollback to the previous deployment revision:

```bash
kubectl rollout undo deployment/house-price-backend
```

Rollback to a specific revision:

```bash
kubectl rollout undo deployment/house-price-backend \
--to-revision=<revision-number>
```

---

# Testing

Run the complete test suite:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

---

# API

## Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

## Prediction

```http
POST /predict
```

The prediction endpoint accepts house-related features and returns the predicted house price.

Interactive API documentation is available through FastAPI Swagger UI:

```text
http://localhost:8000/docs
```

---

# Key Engineering Concepts

This project demonstrates practical implementation of:

* Machine Learning model serving
* REST API development
* Service-based application architecture
* Docker containerization
* Multi-container orchestration
* Kubernetes Deployments
* Kubernetes Services
* ConfigMap and Secret management
* Liveness and readiness probes
* Horizontal Pod Autoscaling
* Metrics-based resource monitoring
* Rolling updates
* Deployment rollback
* NGINX Ingress routing

---

# Future Improvements

Potential enhancements include:

* CI/CD pipeline with GitHub Actions
* Automated Docker image versioning
* Container registry integration
* Cloud deployment using managed Kubernetes
* Infrastructure as Code using Terraform
* Monitoring with Prometheus and Grafana
* Centralized logging
* Model versioning with MLflow
* Model monitoring and drift detection
* HTTPS with cert-manager
* Authentication and authorization
* API rate limiting

---

# License

This project is intended for educational, portfolio, and demonstration purposes.

--
