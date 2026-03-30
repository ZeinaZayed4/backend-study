import requests
from sys import argv

try:
    if len(argv) != 2:
        exit("Missing command-line argument")
    n = float(argv[1])
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=yourApiKey")
    content = response.json()["data"]
    total_price = float(content["priceUsd"]) * n
    print(f"${total_price:,.4f}")
except ValueError:
    exit("Command-line argument is not a number")
