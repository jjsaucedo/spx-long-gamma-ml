import pandas as pd

def build_long_gamma_features(options, spot_price):
    rows = []

    for opt in options:
        greeks = opt.get("greeks", {})
        rows.append({
            "strike": opt["strike"],
            "iv": greeks.get("iv", 0),
            "gamma": greeks.get("gamma", 0),
            "delta": greeks.get("delta", 0),
            "distance": abs(opt["strike"] - spot_price)
        })

    df = pd.DataFrame(rows)
    df = df[df["iv"] > 0]

    df["gamma_weighted"] = df["gamma"] / df["gamma"].sum()
    df["iv_mean"] = df["iv"].mean()

    return df
