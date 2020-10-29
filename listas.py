"""Escribe un programa en Python que registre el nombre de cinco criptomonedas, 
con sus respectivas cantidades y precios en USD, haciendo uso de listas. Luego, 
imprima los datos de cada moneda una vez que han sido ingresadas por el usuario."""

i=0
j=0
cripto=[]
cant=[]
cotiz=[]
while j<3:
    cripto.append(input("Indique el nombre de la criptomoneda: "))
    cant.append(float(input("Indique la cantidad de "+cripto[j]+": ")))
    cotiz.append(float(input("Indique la cotización en USD de "+cripto[j]+": ")))
    j=j+1

while i<3:
    print("Moneda: ",cripto[i],", Cantidad: ",str(cant[i]),", Cotización: "+str(cotiz[i]))
    i=i+1

