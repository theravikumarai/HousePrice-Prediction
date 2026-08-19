# House Price Prediction

A machine learning API for predicting house prices using **FastAPI**, **CatBoost**, and **Docker**.

## Overview

The API serves a trained `CatBoostRegressor` model through REST endpoints.

```text
Client
  ↓
FastAPI
  ↓
Input Validation
  ↓
Feature Engineering
  ↓
CatBoost Model
  ↓
Price Prediction
```

## Tech Stack

* Python
* FastAPI
* CatBoost
* Pandas
* NumPy
* Docker

## Project Structure

```text
house-price-prediction-api/
│
├── app/
│   ├── main.py
│   ├── model.py
│   └── preprocessing.py
│
├── models/
│   └── model.pkl
│
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## Features

* REST API using FastAPI
* House price prediction with CatBoost
* Automatic feature engineering
* Model loaded at application startup
* Health check endpoint
* Interactive API documentation
* Dockerized application

## API Endpoints

| Method | Endpoint   | Description         |
| ------ | ---------- | ------------------- |
| GET    | `/`        | API information     |
| GET    | `/health`  | Health check        |
| POST   | `/predict` | Predict house price |
| GET    | `/docs`    | Swagger UI          |

## Run Locally

Clone the repository:

```bash
git clone <your-repository-url>
cd house-price-prediction-api
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Docker

Build the image:

```bash
docker build -t house-price-api .
```

Run the container:

```bash
docker run -p 8000:8000 house-price-api
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Prediction Flow

```text
POST /predict
      ↓
Request Validation
      ↓
Feature Engineering
      ├── HouseAge
      ├── RemodAge
      ├── TotalSF
      └── TotalBath
      ↓
Feature Alignment
      ↓
CatBoostRegressor
      ↓
Log Prediction
      ↓
np.expm1()
      ↓
Predicted House Price
```

## Example Response

```json
{
  "predicted_price": 119329.95
}
```

## Run with Docker

```text
docker build
     ↓
Docker Image
     ↓
docker run
     ↓
FastAPI Container
     ↓
POST /predict
```

## Future Improvements

* Add automated tests
* Add strict request schemas
* Add structured logging
* Add GitHub Actions CI/CD
* Push Docker images to Docker Hub or AWS ECR
* Deploy to AWS
* Add monitoring and model versioning

## Key Takeaway

This project demonstrates how to serve a trained machine learning model as a REST API and package the application using Docker.

---

