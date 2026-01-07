def build_straddle(symbol, strike, expiration):
    return {
        "symbol": symbol,
        "expiration": expiration,
        "strike": strike,
        "structure": "ATM_STRADDLE"
    }

