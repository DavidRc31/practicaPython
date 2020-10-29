""" Escribe un programa en Python que solicite el ingreso de tres 
criptomonedas, las cantidades y cotizaciones en Dólares Americanos (USD) 
de cada una de éstas, validando que las tres criptomonedas pertenezcan a 
las siguientes (BTC, BCC, LTC, ETH, ETC y XRP), y que las cantidades y 
cotizaciones sean números reales. Por último el programa debe indicar la 
cantidad de USD que el usuario tiene acumulado. """


criptos = ["BTC","BCC","LTC","ETH","ETC"]

for num in range(1,3):
    cripto = input("Ingrese el nombre de la moneda: ")
    cantidad=float(input("ingrese la cantidad de "+cripto+" :"))
    cotizacion=float(input("ingrese la cotizacion de "+cripto+" :"))
    total_usd= total_usd+cantidad*cotizacion
    while cripto not in criptos:
       cripto = input("La moneda "+cripto+" no existe. Ingrese el nombre de la moneda: ")
    else:
      print("Moneda Válida")
      num=num+1

print("el monto acumulado de "+str(total_usd))
