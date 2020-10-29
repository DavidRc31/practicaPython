"""Escribe un programa en Python que solicite al usuario el nombre de una 
criptomoneda y verifique si ésta existe en coinmarketcap.com. Posteriormente, 
el programa debe imprimir el nombre abreviado o, como también se conoce, nombre 
código y el nombre completo de la criptomoneda. Para esto, recuerda utilizar el 
módulo requests, usando la API https://api.coinmarketcap.com/v2/listings/ que retorna 
un json con una lista de datos de las criptomonedas. Entre estos datos tenemos el symbol 
de la criptomoneda que corresponde al nombre código y name que contiene el nombre completo 
de la criptomoneda.

Te recomendamos hacer uso de variables tipo diccionario y tuplas como claves."""

import requests

def esmoneda(cripto):
    return cripto in monedas

monedas_list=[]
monedas_list_nom={}
COINMARKET_API_KEY = "5a77b76c-e4c7-4b44-993b-9e6f0f734891"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}

data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
for cripto in data["data"]:
   """ monedas_list.append(cripto["symbol"])"""
   monedas_list_nom[cripto["symbol"]]=cripto["name"]

"""monedas=tuple(monedas_list)"""
monedas = monedas_list_nom.keys()
moneda=input("Indique el nombre de la moneda a verificar: ")
while not esmoneda(moneda):
        print("Moneda Invalida.")
        moneda=input("Ingrese el nombre de la moneda: ")
else:
    print("La moneda con symbol:",moneda,"y nombre:",monedas_list_nom.get(moneda),
          "es valida porque existe en coimnmarketcap.com")
