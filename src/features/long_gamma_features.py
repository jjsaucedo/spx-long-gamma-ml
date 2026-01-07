def enrich_with_gex(features_df, gex_df, total_gex):
    atm_strike = gex_df.iloc[
        (gex_df["strike"] - gex_df["strike"].mean()).abs().argsort()[:1]
    ]["strike"].values[0]

    atm_gex = gex_df[gex_df["strike"] == atm_strike]["gex"].values[0]

    features_df["total_gex"] = total_gex
    features_df["atm_gex"] = atm_gex
    features_df["dealer_position"] = "NEGATIVE" if total_gex < 0 else "POSITIVE"

    return features_df
