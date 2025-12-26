from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load model
model = joblib.load("titanic_xgb_v1.pkl")

class Passenger(BaseModel):
    pclass: int
    age: float
    sex: str
    fare: float
    embarked: str
    alone: bool

@app.post("/predict")
def prediction_survival(passenger: Passenger):

    df = pd.DataFrame([{
        "sex": passenger.sex,
        "pclass": passenger.pclass,
        "age": passenger.age,
        "fare": passenger.fare,
        "embarked": passenger.embarked,
        "alone": passenger.alone
    }])

    # Same preprocessing as training
    df["sex"] = df["sex"].map({"male": 0, "female": 1})
    df["embarked"] = df["embarked"].map({"C": 0, "Q": 1, "S": 2})
    df["alone"] = df["alone"].astype(int)

    df = df[['sex', 'pclass', 'age', 'fare', 'embarked', 'alone']]

    pred = int(model.predict(df)[0])
    prob = float(model.predict_proba(df)[0][1])

    return {
        "survived": pred,
        "survival_probability": prob
    }
