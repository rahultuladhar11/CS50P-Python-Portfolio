import sys
import json
import requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arugments")

try:
    bitcoin = float(sys.argv[1])
    #print(bitcoin)

except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=37b505811f6c3c5c4a5f3a9d0c991e6a558938ea36e1940ffde9f111ba416457")
    #print(json.dumps(response.json(), indent=2))

    o = response.json()
    usd = (float(o["data"]["priceUsd"]))*bitcoin
    print(f"${usd:,.4f}")

except requests.RequestException:
    print("There was an error making the request.")
