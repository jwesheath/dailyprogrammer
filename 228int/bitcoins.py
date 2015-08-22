import requests
import csv
import sys


def main():
    market = sys.argv[1]
    currency = sys.argv[2]
    r = requests.get('http://api.bitcoincharts.com/v1/trades.csv?symbol=' + market + currency)
    result = float([row for row in csv.reader(r.text.splitlines())][0][1])
    print(result)
    return 0


if __name__ == '__main__':
    main()
