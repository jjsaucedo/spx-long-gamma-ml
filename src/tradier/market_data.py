from .client import tradier_get

def get_quote(symbol="SPY"):
    return tradier_get(
        "/markets/quotes",
        {"symbols": symbol, "greeks": "true"}
    )
