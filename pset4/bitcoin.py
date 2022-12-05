import sys
import requests

try:
    unit = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    value = data["bpi"]["USD"]["rate"]

    value = float("".join(value.split(","))) * unit
    print(f"${value:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
except requests.RequestException:
    sys.exit()