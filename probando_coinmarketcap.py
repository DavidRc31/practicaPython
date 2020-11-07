
import requests

def esmoneda(cripto):
    return cripto in monedas

monedas_list=[]#lista criptomonedas
monedas_name_list=[]#lista nombres de criptomonedas
monedas_market_cap_list=[]#lista de cotizacion de criptomonedas
cripto_saldo=[]#Declarando lista saldo de criptomonedas
modenas_list2=[]#lista criptomonedas

        


COINMARKET_API_KEY = "5a77b76c-e4c7-4b44-993b-9e6f0f734891"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}

#parametros = {'symbol': symbol}
data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

for cripto in data["data"]:
    monedas_list.append(cripto["symbol"])
    monedas_name_list.append(cripto["name"])
    monedas_market_cap_list.append(cripto["quote"]["USD"]["price"])
    modenas_list2.append({"symbol": cripto["symbol"], "price": cripto["quote"]["USD"]["price"]})

monedas=tuple(monedas_market_cap_list)

i=0
while i < len(monedas):
	print(monedas[i])
	i+=1
	pass

