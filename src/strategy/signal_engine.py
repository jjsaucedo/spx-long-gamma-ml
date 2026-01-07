
def generate_signal(model, features_df):
    X = features_df[["iv_mean", "gamma_weighted"]].mean().to_frame().T
    prob = model.predict_proba(X)[0][1]

    return {
        "long_gamma_probability": prob,
        "trade": prob > 0.65
    }
