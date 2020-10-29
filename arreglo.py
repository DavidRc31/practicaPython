"""En esta oportunidad te pedimos escribir un programa en pseudocódigo 
que registre el nombre de cinco criptomonedas, con sus respectivas cantidades 
y precios en USD, haciendo uso de arreglos. Posteriormente, imprima los datos 
de cada moneda luego de ser ingresadas por el usuario."""

def array_cripto(n):
  str array_nom = [3]
  float array_cant = [3] 
  float array_usd = [3]
  for x in range(n):
  	cripto = input("Ingrese el nombre de la moneda: ")
  	cant = input("Indique la cantidad de "+cripto+":")
  	cotiz = input("Indique la cotización en USD de "+cripto+":")
  	array_nom[x]=cripto
  	array_cant[x]=cant
  	array_usd[x]=cotiz
  	x=x+1
  for j in range(n):
  	cripto = array_nom[j]
  	cant = array_cant[j]
  	cotiz = array_usd[j]
  	total_usd=cant*cotiz
  	print("monbre:", str(cripto)+"\n")
  	print("cantidad:", str(cant)+"\n")
  	print("cotización:", str(cotiz)+"\n")
  	print("en total acumulado es:", str(total_usd)+"\n")
  	j=j+1

array_cripto(3)
