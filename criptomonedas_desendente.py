"""En esta oportunidad, te solicitamos que escribas un programa en Python 
que lea el nombre de tres criptomonedas y el monto que posee el usuario 
de cada una de éstas; luego las muestre ordenadas de forma descendente 
cada nombre con su respectivo monto. ¡Éxito!"""

mombre_cripto1=str(input("por favor ingrese nombre de la cripto"))
monto_cripto1=float(input("por favor ingresa el monto de la criptomoneda"))
mombre_cripto2=str(input("por favor ingrese nombre de la cripto"))
monto_cripto2=float(input("por favor ingresa el monto de la criptomoneda"))
mombre_cripto3=str(input("por favor ingrese nombre de la cripto"))
monto_cripto3=float(input("por favor ingresa el monto de la criptomoneda"))
if monto_cripto1 > monto_cripto2 and monto_cripto1 > monto_cripto3:
   primero=monto_cripto1
   nom_primero=mombre_cripto1
   if monto_cripto2 > monto_cripto3:
      segundo=monto_cripto2
      nom_segundo=mombre_cripto2
      tercero=monto_cripto3
      nom_tercero=mombre_cripto3
   else:
      segundo=monto_cripto3
      nom_segundo=mombre_cripto3
      tercero=monto_cripto2
      nom_tercero=mombre_cripto2

elif monto_cripto1 > monto_cripto3:
     segundo=monto_cripto1
     nom_segundo=mombre_cripto1
     if monto_cripto2 > monto_cripto3:
        primero=monto_cripto2
        nom_primero=mombre_cripto2
        tercero=monto_cripto3
        nom_tercero=mombre_cripto3
     else:
        primero=monto_cripto3
        nom_primero=mombre_cripto3
        tercero=monto_cripto2
        nom_tercero=mombre_cripto2
        
elif monto_cripto1 > monto_cripto2:
     segundo=monto_cripto1
     nom_segundo=mombre_cripto1
     if monto_cripto2 > monto_cripto3:
        primero=monto_cripto3
        nom_primero=mombre_cripto3
        tercero=monto_cripto2
        nom_tercero=mombre_cripto2
     else:
        primero=monto_cripto3
        nom_primero=mombre_cripto3
        tercero=monto_cripto2
        nom_tercero=mombre_cripto2
  
else:
     tercero=monto_cripto1
     nom_tercero=mombre_cripto1
     if monto_cripto2 > monto_cripto3:
      primero=monto_cripto2
      nom_primero=mombre_cripto2
      segundo=monto_cripto3
      nom_segundo=mombre_cripto3
     else:
      segundo=monto_cripto2
      nom_segundo=mombre_cripto2
      primero=monto_cripto3
      nom_primero=mombre_cripto3 


print("la primera criptomoneda es "+nom_primero+"con "+str(primero))
print("la segunda criptomoneda es "+nom_segundo+"con "+str(segundo))
print("la tercera criptomoneda es "+nom_tercero+"con "+str(tercero))
