import streamlit as st
import requests
import os

# API_URL = "http://127.0.0.1:8000/predict"
# API_URL = "http://backend:8000/predict"
API_URL = os.getenv(
    "API_URL",
    "http://localhost:8000/predict"
)
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide",
)


st.title("🏠 House Price Prediction")
st.write(
    "Enter property details and predict the estimated house price "
    "using a CatBoost machine learning model."
)


st.divider()


# -----------------------------
# Property Details
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    overall_qual = st.slider(
        "Overall Quality",
        min_value=1,
        max_value=10,
        value=5
    )

    year_built = st.number_input(
        "Year Built",
        min_value=1800,
        max_value=2026,
        value=1961
    )

    total_bsmt_sf = st.number_input(
        "Basement Area (sq ft)",
        min_value=0,
        value=882
    )

    first_flr_sf = st.number_input(
        "First Floor Area (sq ft)",
        min_value=0,
        value=896
    )


with col2:
    gr_liv_area = st.number_input(
        "Living Area (sq ft)",
        min_value=0,
        value=896
    )

    full_bath = st.number_input(
        "Full Bathrooms",
        min_value=0,
        value=1
    )

    bedroom_abv_gr = st.number_input(
        "Bedrooms",
        min_value=0,
        value=2
    )

    garage_cars = st.number_input(
        "Garage Capacity",
        min_value=0,
        value=1
    )


with col3:
    lot_area = st.number_input(
        "Lot Area (sq ft)",
        min_value=0,
        value=11622
    )

    year_remod_add = st.number_input(
        "Year Remodeled",
        min_value=1800,
        max_value=2026,
        value=1961
    )

    garage_area = st.number_input(
        "Garage Area (sq ft)",
        min_value=0,
        value=730
    )

    yr_sold = st.number_input(
        "Year Sold",
        min_value=2006,
        max_value=2030,
        value=2010
    )


st.divider()


if st.button("Predict House Price", use_container_width=True):

    features = {
        "MSSubClass": 20,
        "MSZoning": "RH",
        "LotFrontage": 80,
        "LotArea": lot_area,
        "Street": "Pave",
        "Alley": "None",
        "LotShape": "Reg",
        "LandContour": "Lvl",
        "Utilities": "AllPub",
        "LotConfig": "Inside",
        "LandSlope": "Gtl",
        "Neighborhood": "NAmes",
        "Condition1": "Feedr",
        "Condition2": "Norm",
        "BldgType": "1Fam",
        "HouseStyle": "1Story",
        "OverallQual": overall_qual,
        "OverallCond": 6,
        "YearBuilt": year_built,
        "YearRemodAdd": year_remod_add,
        "RoofStyle": "Gable",
        "RoofMatl": "CompShg",
        "Exterior1st": "VinylSd",
        "Exterior2nd": "VinylSd",
        "MasVnrType": "None",
        "MasVnrArea": 0,
        "ExterQual": "TA",
        "ExterCond": "TA",
        "Foundation": "CBlock",
        "BsmtQual": "TA",
        "BsmtCond": "TA",
        "BsmtExposure": "No",
        "BsmtFinType1": "Rec",
        "BsmtFinSF1": 468,
        "BsmtFinType2": "LwQ",
        "BsmtFinSF2": 144,
        "BsmtUnfSF": 270,
        "TotalBsmtSF": total_bsmt_sf,
        "Heating": "GasA",
        "HeatingQC": "TA",
        "CentralAir": "Y",
        "Electrical": "SBrkr",
        "1stFlrSF": first_flr_sf,
        "2ndFlrSF": 0,
        "LowQualFinSF": 0,
        "GrLivArea": gr_liv_area,
        "BsmtFullBath": 0,
        "BsmtHalfBath": 0,
        "FullBath": full_bath,
        "HalfBath": 0,
        "BedroomAbvGr": bedroom_abv_gr,
        "KitchenAbvGr": 1,
        "KitchenQual": "TA",
        "TotRmsAbvGrd": 5,
        "Functional": "Typ",
        "Fireplaces": 0,
        "FireplaceQu": "None",
        "GarageType": "Attchd",
        "GarageYrBlt": year_built,
        "GarageFinish": "Unf",
        "GarageCars": garage_cars,
        "GarageArea": garage_area,
        "GarageQual": "TA",
        "GarageCond": "TA",
        "PavedDrive": "Y",
        "WoodDeckSF": 140,
        "OpenPorchSF": 0,
        "EnclosedPorch": 0,
        "3SsnPorch": 0,
        "ScreenPorch": 120,
        "PoolArea": 0,
        "PoolQC": "None",
        "Fence": "MnPrv",
        "MiscFeature": "None",
        "MiscVal": 0,
        "MoSold": 6,
        "YrSold": yr_sold,
        "SaleType": "WD",
        "SaleCondition": "Normal"
    }

    payload = {
        "features": features
    }

    try:

        with st.spinner("Predicting house price..."):

            response = requests.post(
                API_URL,
                json=payload,
                timeout=30
            )

        if response.status_code == 200:

            result = response.json()

            predicted_price = result["predicted_price"]

            st.success("Prediction completed!")

            st.metric(
                label="Predicted House Price",
                value=f"${predicted_price:,.2f}"
            )

        else:

            st.error(
                f"API Error: {response.text}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "Unable to connect to the FastAPI server. "
            "Make sure the API is running."
        )

    except Exception as error:

        st.error(
            f"Something went wrong: {error}"
        )