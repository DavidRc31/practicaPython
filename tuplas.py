"""En esta ocasión te solicitamos que escribas un programa en Python que 
verifique si el nombre de una criptomoneda, ingresada por el usuario, existe 
en coinmarketcap.com. Para ello recuerda utilizar el módulo requests, usando 
la API https://api.coinmarketcap.com/v2/listings/. Esta API retorna un json con 
una lista de datos de las criptomonedas, entre estos datos se encuentra el symbol 
de la criptomoneda que corresponde al nombre código de la moneda.

Te recomendamos hacer uso de tuplas para hacer la búsqueda del nombre de la criptomoneda 
ingresada por el usuario; esto debido a que hacer búsquedas en tuplas es mucho más rápido 
que en listas y así obtendrás una solución eficiente."""

import requests

def esmoneda(cripto):
    return cripto in monedas

monedas_list=[]
COINMARKET_API_KEY = "5a77b76c-e4c7-4b44-993b-9e6f0f734891"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}

data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
for cripto in data["data"]:
    monedas_list.append(cripto["symbol"])

monedas=tuple(monedas_list)

moneda=input("Indique el nombre de la moneda a verificar: ")
while not esmoneda(moneda):
        print("Moneda Invalida.")
        moneda=input("Ingrese el nombre de la moneda: ")
else:
    print("La moneda,",moneda,"es valida porque existe en coimnmarketcap.com")


