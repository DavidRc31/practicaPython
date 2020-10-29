""" Solicita el ingreso del nombre de una criptomoneda hasta que se 
ingrese alguna de los siguientes nombres: BTC, BCC, LTC, ETH, ETC. """


criptos = ["BTC","BCC","LTC","ETH","ETC"]
cripto = input("Ingrese el nombre de la moneda: ")
while cripto not in criptos:
    cripto = input("La moneda "+cripto+" no existe. Ingrese el nombre de la moneda: ")
else:
    print("Moneda Válida")

