import sys
import requests
import json

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha() == True:
        sys.exit("Command-line argument is not a number")
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        #print(json.dumps(response.json(), indent=2))
        data = response.json()
        bpi_usd = data["bpi"]["USD"]
        usd = bpi_usd["rate_float"]
        amt = float(sys.argv[1])*float(usd)
        print(f"${amt:,.4f}")
except requests.RequestException:
    pass
