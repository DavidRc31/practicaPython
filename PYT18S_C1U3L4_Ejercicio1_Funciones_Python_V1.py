"""Ahora, te motivamos a escribir un programa en Python que solicite el 
ingreso de tres criptomonedas, las cantidades y cotizaciones en Dólares 
Americanos (USD) de cada una de éstas; además, debes validar que las tres 
criptomonedas pertenezcan a las siguientes (BTC, BCC, LTC, ETH, ETC y XRP), 
y que las cantidades y cotizaciones sean números reales. Por último, el 
programa debe indicar la cantidad de USD que el usuario tiene acumulada.

Te recomendamos hacer uso de funciones para realizar las validaciones."""
total=0
i=0
while (i < 3):
    cripto = input("Ingrese el nombre de la moneda: ")
    if esmoneda():
        i=i+1
        cant = ""
        while not esnumero(cant):
            cant = input("Indique la cantidad de "+cripto+":")
        cotiz=""
        while not esnumero(cotiz):
            cotiz = input("Indique la cotización en USD de "+cripto+":")
        total = total + float(cant) * float(cotiz)
    else:
        print("Moneda invalida.")
print("El tota en USD que tiene el usuario es de ",str(total))

def esmoneda(cripto):
    criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    if cripto in criptos:
        return True
    else:
        return False

def esnumero(numero): 
    return numero.replace('.','',1).isdigit()

    