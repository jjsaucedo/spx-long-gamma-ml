from src.tradier.market_data import get_quote
from src.tradier.options import get_option_chain
from src.features.long_gamma_features import build_long_gamma_features
from src.strategy.signal_engine import generate_signal
from xgboost import XGBClassifier

model = XGBClassifier()
model.load_model("data/processed/long_gamma.model")

quote = get_quote("SPY")
spot = quote["quotes"]["quote"]["last"]

options = get_option_chain("SPY", "2026-01-05")
options_list = options["options"]["option"]

features = build_long_gamma_features(options_list, spot)
signal = generate_signal(model, features)

print(signal)

