from .client import tradier_get

def get_option_chain(symbol, expiration):
    return tradier_get(
        "/markets/options/chains",
        {"symbol": symbol, "expiration": expiration}
    )
