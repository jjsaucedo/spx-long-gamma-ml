import requests
from config.settings import BASE_URL, HEADERS

def tradier_get(endpoint, params=None):
    url = f"{BASE_URL}{endpoint}"
    r = requests.get(url, headers=HEADERS, params=params)
    r.raise_for_status()
    return r.json()
