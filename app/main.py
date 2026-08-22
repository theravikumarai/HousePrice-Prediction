from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any
import numpy as np

from app.model import model
from app.preprocessing import preprocess_input


# app = FastAPI(
#     title="House Price Prediction API",
#     description="Predict house prices using CatBoostRegressor",
#     version="1.0.0",
# )

app = FastAPI(
    title="House Price Prediction API",
    description="Predict house prices using CatBoostRegressor",
    version="1.0.0",
    root_path="/api",
)


class PredictionRequest(BaseModel):
    features: dict[str, Any]


@app.get("/")
def root():
    return {
        "message": "House Price Prediction API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model": type(model).__name__
    }


@app.post("/predict")
def predict(request: PredictionRequest):

    try:
        input_data = preprocess_input(
            request.features,
            model
        )

        prediction_log = model.predict(input_data)[0]

        prediction = np.expm1(prediction_log)

        return {
            "predicted_price": round(float(prediction), 2)
        }

    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error)
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(error)}"
        )