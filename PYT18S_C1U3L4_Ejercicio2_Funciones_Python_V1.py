"""Escribe un programa en Python que solicite el ingreso del nombre de una 
criptomoneda, validando que sea una de las siguientes (BTC, BCC, LTC, ETH, ETC y XRP), 
y que indique el precio actual de la misma obteniendo su valor de Binance en USDT.

Para obtener el precio de la criptomoneda en USDT te recomendamos hacer uso de la API Rest de Binance; 
además, puedes hacer uso de la API price ticker. Esta API se invoca en el navegador a través del URL: 
https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT.

Asimismo, utiliza el módulo resquests, para lo cual debes importarlo primero a la máquina usando pip3 
install requests o pip install requests desde la consola de comando o terminal de tu sistema operativo.

Con la finalidad de invocar la API, puedes hacer uso de la función get de requests. Por ejemplo: 
requests.get(url).

Te recomendamos también hacer uso de funciones para realizar las validaciones. """


import requests
_ENDPOINT = "https://api.binance.com"
def _url(api):
    return _ENDPOINT+api

def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

def esmoneda(cripto):
    criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    if cripto in criptos:
        return True
    else:
        return False

moneda=""
while not esmoneda(moneda):
    moneda = input("Ingrese la moneda a determianr el precio: ")

data = get_price(moneda+"USDT").json()
print("El precio de",moneda,"es",data["price"])


