import sys
import requests

if len(sys.argv) != 2:
    print("Missing command-line argument.")
    sys.exit(1)

try:
    value = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number.")
    sys.exit(1)

try:
    # Use correct and simple endpoint for Bitcoin
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    response.raise_for_status()
    data = response.json()
    price = float(data["data"]["priceUsd"])
    total = price * value
    print(f"${total:,.4f}")
except requests.RequestException:
    print("Network error occurred. Please check your connection.")
