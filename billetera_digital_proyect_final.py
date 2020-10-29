""" desarrolles tu propia billetera digital de tipo Desktop con interfaz de texto, que soporte monedas registradas en coinmarketcap.com, y que permita:

Enviar un monto en USD de alguna de las criptomonedas a un destinatario indicado (identificado por un código)
Recibir de un enviador (identificado por un código) una cantidad de alguna criptomoneda
Consultar el balance de cada una de las criptomonedas en USD
Consultar el balance general del usuario en USD usando el precio de la criptomoneda provisto por las APIs de coinmarketcap.com
Emitir un histórico de transacciones del usuario indicando fecha, moneda, cantidad y monto en USD para el momento de la transacción
Todas las transacciones realizadas por el usuario deben ser almacenadas y mantenidas, así como las cantidades de cada una de las criptomonedas que posea
Colocar un menú de opciones con:"""

import requests

def esmoneda(cripto):
    return cripto in monedas

monedas_list=[]#lista criptomonedas
monedas_name_list=[]#lista nombres de criptomonedas
monedas_market_cap_list=[]#lista de cotizacion de criptomonedas

COINMARKET_API_KEY = "5a77b76c-e4c7-4b44-993b-9e6f0f734891"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}
#symbol="BTC"
#parametros = {'symbol': symbol}
data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

for cripto in data["data"]:
    monedas_list.append(cripto["symbol"])
    monedas_name_list.append(cripto["name"])
    #monedas_market_cap_list.append(cripto["market_cap_strict"])

monedas=tuple(monedas_list)
#prueba
i=0
while i < len(monedas):
	print(monedas[i])
	i+=1
	pass
"""
moneda=input("Indique el nombre de la moneda a verificar: ")
while not esmoneda(moneda):
        print("Moneda Invalida.")
        moneda=input("Ingrese el nombre de la moneda: ")
else:
    print("La moneda,",moneda,"es valida porque existe en coimnmarketcap.com")
======================

#CRIPTOMONEDAS
class Criptomoneda(object):
    def __init__(self, nombre,  saldo, cotizacion):
      self.nombre = nombre
      self.saldo = saldo
      self.cotizacion = cotizacion
 
    def indicarNombre(self, nombre):
      self.nombre=nombre
 
    def indicarCotizacion(self, cotizacion):
      self.cotizacion=cotizacion
 
    def indicarSaldo(self, saldo):  
      self.saldo=saldo
 
    def mostrarNombre(self):
      return self.nombre
 
    def imostrarCotizacion(self): 
      return self.cotizacion
 
    def mostrarSaldo(self):  
      return  self.saldo
 
    def calcularSaldo(self, moneda):  
      if moneda== "USD":
          return self.saldo*self.cotizacion
      else:
          return self.saldo

#MENU
Recibir cantidad:
Solicitar moneda, cantidad a recibir, así como el código.
Validar moneda, cantidad y código, éste debe ser diferente al propio.
Sumar cantidad de monedas al saldo.
Transferir monto:
Solicitar moneda, monto y código del destinatario a enviar.
Validar.
Restar cantidad de monedas al saldo.
Mostrar balance una moneda:
Solicitar la moneda a mostrar
Validar existencia de la moneda.
Mostrar nombre de la moneda, cantidad y monto en USD para ese momento.
Mostrar balance general:
Mostrar nombre de cada moneda, cantidad y monto en USD para ese momento.
Mostrar monto total en USD de todas las monedas.
Mostrar histórico de transacciones:
Mostrar todas las transacciones indicando fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
Salir del programa
++++++++++++++++++++++++
opcion=None
print("Por favor elija la operacion a realizar")
print("Presione 1 Para Recibir cantidad :")
print("Presione 2 Para Transferir monto :")
print("Presione 3 Para Mostrar balance una moneda :")
print("Presione 4 Para Mostrar balance general :")
print("Presione 5 Para Mostrar histórico de transacciones :")
print("Presione 6 Para Mostrar Salir del programa :")

while opcion != '6':
      opcion=input("por favor ingrese el termino:  \n(si no desea agregar mas presione x)\n(se desea consultar un ternino c) ")
      if opcion =='1':
      	#Resivir
      	print("Para recibir moneda por favor digite:")
      	moneda=input("digite moneda")
      	cantidad_moneda=input("Digite cantedad :")
      	codigo=input("Digite codigo")
      	cripto=Criptomoneda(moneda,cantidad_moneda,codigo)
      elif opcion == '2':
        term=input("por favor ingrese el termino a consultar")
        encontrado=consulta_termino_cripto(term)
        if encontrado == None:
        	print("el termino ingresado no se encuentra en el diccionario")
      else:
        descripcion=input("ingrese la descripcion "+termino+": ")
        agregar_diccionario(termino,descripcion)
      pass

"""
