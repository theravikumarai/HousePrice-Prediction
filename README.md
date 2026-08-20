Absolutely. Replace your current `README.md` with the following updated version.

# House Price Prediction

A containerized machine learning application for predicting house prices using a **CatBoostRegressor**, served through **FastAPI** and consumed through a **Streamlit** user interface.

## Architecture

```text
                    ┌─────────────────┐
                    │     Browser     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Streamlit    │
                    │    Frontend     │
                    │ localhost:8501  │
                    └────────┬────────┘
                             │
                       POST /predict
                             │
                             ▼
                    ┌─────────────────┐
                    │     FastAPI     │
                    │     Backend     │
                    │ localhost:8000  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Preprocessing  │
                    │ Feature Creation│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ CatBoostRegressor│
                    │    model.pkl    │
                    └────────┬────────┘
                             │
                             ▼
                    Predicted House Price
```

## Features

* House price prediction using CatBoost
* REST API built with FastAPI
* Interactive Streamlit frontend
* Automatic feature engineering
* Health check endpoint
* Swagger API documentation
* Dockerized backend and frontend
* Multi-container orchestration with Docker Compose

## Tech Stack

| Category         | Technology        |
| ---------------- | ----------------- |
| Language         | Python            |
| ML Model         | CatBoostRegressor |
| Backend          | FastAPI           |
| Frontend         | Streamlit         |
| Data Processing  | Pandas, NumPy     |
| API Server       | Uvicorn           |
| Containerization | Docker            |
| Orchestration    | Docker Compose    |

## Project Structure

```text
HousePrice-Prediction/
│
├── app/
│   ├── main.py
│   ├── model.py
│   └── preprocessing.py
│
├── frontend/
│   ├── streamlit_app.py
│   └── Dockerfile
│
├── models/
│   └── model.pkl
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## Application Flow

```text
User Input
    ↓
Streamlit UI
    ↓
POST /predict
    ↓
FastAPI
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
Log-Scale Prediction
    ↓
np.expm1()
    ↓
Predicted House Price
```

## API Endpoints

| Method | Endpoint   | Description                       |
| ------ | ---------- | --------------------------------- |
| GET    | `/`        | API information                   |
| GET    | `/health`  | Application health check          |
| POST   | `/predict` | Predict house price               |
| GET    | `/docs`    | Interactive Swagger documentation |

## Run Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd HousePrice-Prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI backend

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### 5. Start the Streamlit frontend

Open another terminal and run:

```bash
streamlit run frontend/streamlit_app.py
```

Frontend:

```text
http://localhost:8501
```

## Run with Docker Compose

The easiest way to run the complete application is with Docker Compose.

```bash
docker compose up --build
```

This command will:

1. Build the FastAPI Docker image
2. Build the Streamlit Docker image
3. Create a shared Docker network
4. Start the backend container
5. Start the frontend container

Access the application:

| Service            | URL                          |
| ------------------ | ---------------------------- |
| Streamlit Frontend | `http://localhost:8501`      |
| FastAPI API        | `http://localhost:8000`      |
| Swagger UI         | `http://localhost:8000/docs` |

To stop the application:

```bash
docker compose down
```

## Docker Architecture

```text
Docker Compose
│
├── frontend
│   ├── Streamlit
│   ├── Port 8501
│   └── Sends requests to backend
│
└── backend
    ├── FastAPI
    ├── Port 8000
    ├── Preprocessing
    └── CatBoost Model
```

Inside Docker Compose, the frontend communicates with the backend using the service name:

```text
http://backend:8000/predict
```

This is configured using an environment variable.

## Example Prediction Response

```json
{
  "predicted_price": 119329.95
}
```

## Key Concepts Demonstrated

This project demonstrates:

* Machine learning model serving
* FastAPI REST API development
* Pydantic request validation
* Feature engineering during inference
* Model serialization and loading
* Streamlit frontend development
* Frontend-to-backend API communication
* Docker image creation
* Docker container execution
* Multi-container applications with Docker Compose
* Service-to-service communication using Docker networking

## Future Improvements

* Add unit and integration tests
* Add automated testing with `pytest`
* Implement GitHub Actions CI/CD
* Push Docker images to Docker Hub or AWS ECR
* Add structured logging
* Add model versioning with MLflow
* Add input validation with stricter schemas
* Deploy the application to AWS
* Add monitoring and observability

## Run Summary

### Local development

```text
Terminal 1
    ↓
FastAPI
    ↓
localhost:8000


Terminal 2
    ↓
Streamlit
    ↓
localhost:8501
```

### Containerized application

```text
docker compose up --build
            ↓
     Docker Network
            │
      ┌─────┴─────┐
      ▼           ▼
 Streamlit      FastAPI
  :8501          :8000
                    │
                    ▼
             CatBoost Model
```

## License

This project is intended for learning and portfolio purposes.

---
