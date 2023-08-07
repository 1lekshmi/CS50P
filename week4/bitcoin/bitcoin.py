import sys
import requests

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = r.json()
rate = float(data['bpi']["USD"]["rate_float"])

try:
    n = float(sys.argv[1])
    amount = rate * n
    print(f"${amount:,.4f}")

except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
