from xgboost import XGBClassifier

FEATURES = [
    "iv_mean",
    "gamma_weighted"
]

def build_model():
    return XGBClassifier(
        n_estimators=300,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8
    )
