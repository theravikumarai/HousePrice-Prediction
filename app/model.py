from pathlib import Path
import pickle


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "model.pkl"


def load_model():
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

    return model


model = load_model()