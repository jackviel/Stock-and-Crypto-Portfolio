import requests, json, locale

url = "https://yahoo-finance-low-latency.p.rapidapi.com/v6/finance/quote"

YOUR_API_KEY = "Your api key goes here!"

headers = {
    'x-rapidapi-key': YOUR_API_KEY,
    'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
    }

locale.setlocale(locale.LC_ALL, '')

with open('positions.txt','r') as file:

    for line in file:
        print()
        info = line.split()
        querystring = {"symbols":info[0]}
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        currentPrice = response['quoteResponse']['result'][0]['regularMarketPrice']

        initialValue = locale.currency((float(info[1]) * float(info[2])), grouping=True)
        currentValue = locale.currency((float(info[1]) * currentPrice), grouping=True)
        netChange = locale.currency((float(info[1]) * currentPrice)-(float(info[1]) * float(info[2])), grouping=True)

        print(info[1] + " shares of " + info[0] + " = " + initialValue + ", now worth " + currentValue + ", for a " + netChange + " net change.")

    print()
