import requests, json

url = "https://yahoo-finance-low-latency.p.rapidapi.com/v6/finance/quote"

YOUR_API_KEY = "Your api key goes here!"

headers = {
    'x-rapidapi-key': YOUR_API_KEY,
    'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
    }

with open('positions.txt','r') as file:

    for line in file:
        info = line.split()
        querystring = {"symbols":info[0]}
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        currentPrice = response['quoteResponse']['result'][0]['regularMarketPrice']
        print(info[1] + " shares of " + info[0] + " = " + (int(info[1]) * int(info[2])) + " now worth " + (int(info[1]) * currentPrice) + ", " + ((int(info[1]) * currentPrice)-(int(info[1]) * int(info[2]))) + " Net Change")

