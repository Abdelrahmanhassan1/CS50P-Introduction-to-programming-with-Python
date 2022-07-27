import requests
import sys


def main():

    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    elif len(sys.argv) == 2:

        try:

            coins = float(sys.argv[1])
            response = requests.get(
                "https://api.coindesk.com/v1/bpi/currentprice.json")

            res = response.json()

            bitcoin_cost = res["bpi"]["USD"]["rate_float"]

            money = bitcoin_cost * coins

            print(f"${money:,.4f}")

        except ValueError:

            sys.exit("Command-line argument is not a number")


main()
