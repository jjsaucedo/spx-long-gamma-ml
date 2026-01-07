import pandas as pd
from src.models.long_gamma_model import build_model

df = pd.read_csv("data/features/training_data.csv")

X = df[["iv_mean", "gamma_weighted"]]
y = df["label"]

model = build_model()
model.fit(X, y)

model.save_model("data/processed/long_gamma.model")

