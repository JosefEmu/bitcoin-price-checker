"""
Using Coindesk API https://www.coindesk.com/api
"""


import requests, json

#Current bitcoin price in USD
with open("./btc_usd.json","w") as f:
	print(requests.get('https://api.coindesk.com/v1/bpi/currentprice/USD.json').text, file=f)


#Current bitcoin price in KES
with open("./btc_kes.json","w") as f:
	print(requests.get('https://api.coindesk.com/v1/bpi/currentprice/KES.json').text, file=f)


#Current bitcoin price in top currencies
with open("./btc_top_currencies.json","w") as f:
	print(requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').text, file=f)

#Bitcoin price history (30 days)
with open("./btc_price_history.json","w") as f:
	print(requests.get('https://api.coindesk.com/v1/bpi/historical/close.json').text, file=f)


btcUSD= open("./btc_usd.json", "r", encoding="utf-8")
USD= json.load(btcUSD)
btcUSD.close()
btc_price_today = USD["bpi"]["USD"]["rate"]
btc_price_time_updated= USD["time"]["updated"]

def double_money(dollars):
	spacer= "-"*65
	print(f"""{spacer}
Bitcoin price as at {btc_price_time_updated} is ${btc_price_today}.
{spacer}""")
	btc_float= float(btc_price_today.replace(",",""))
	print(f"So ${dollars} is equal to {dollars/btc_float}BTC.")
	print(f"To double you money, the bitcoin price must rise up to ${btc_float*2}.")
double_money(input())
