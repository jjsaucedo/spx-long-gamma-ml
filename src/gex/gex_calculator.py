import pandas as pd

MULTIPLIER = 100

def calculate_gex(options, spot):
    rows = []

    for opt in options:
        greeks = opt.get("greeks", {})
        gamma = greeks.get("gamma", 0)
        oi = opt.get("open_interest", 0)

        if gamma == 0 or oi == 0:
            continue

        sign = 1 if opt["option_type"] == "call" else -1

        gex = sign * gamma * oi * MULTIPLIER * (spot ** 2)

        rows.append({
            "strike": opt["strike"],
            "gex": gex,
            "gamma": gamma,
            "oi": oi
        })

    df = pd.DataFrame(rows)

    gex_by_strike = df.groupby("strike").sum().reset_index()
    total_gex = gex_by_strike["gex"].sum()

    return gex_by_strike, total_gex
