import pandas as pd


def preprocess_input(features: dict, model) -> pd.DataFrame:
    """
    Convert API input into the DataFrame expected by the model.
    """

    data = pd.DataFrame([features])

    # Feature Engineering
    data["HouseAge"] = (
        data["YrSold"] - data["YearBuilt"]
    )

    data["RemodAge"] = (
        data["YrSold"] - data["YearRemodAdd"]
    )

    data["TotalSF"] = (
        data["TotalBsmtSF"]
        + data["1stFlrSF"]
        + data["2ndFlrSF"]
    )

    data["TotalBath"] = (
        data["FullBath"]
        + 0.5 * data["HalfBath"]
        + data["BsmtFullBath"]
        + 0.5 * data["BsmtHalfBath"]
    )

    # Get the exact feature order used during training
    feature_names = model.feature_names_

    # Check for missing required features
    missing_features = [
        feature
        for feature in feature_names
        if feature not in data.columns
    ]

    if missing_features:
        raise ValueError(
            f"Missing features: {missing_features}"
        )

    # Keep only training features in the correct order
    data = data[feature_names]

    return data