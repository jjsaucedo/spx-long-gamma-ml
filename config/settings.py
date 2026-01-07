import os
from dotenv import load_dotenv

load_dotenv()

TRADIER_TOKEN = os.getenv("TRADIER_TOKEN")
ACCOUNT_ID = os.getenv("TRADIER_ACCOUNT_ID")
ENV = os.getenv("TRADIER_ENV", "sandbox")

BASE_URL = (
    "https://sandbox.tradier.com/v1"
    if ENV == "sandbox"
    else "https://api.tradier.com/v1"
)

HEADERS = {
    "Authorization": f"Bearer {TRADIER_TOKEN}",
    "Accept": "application/json"
}
