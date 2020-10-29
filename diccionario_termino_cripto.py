"""Este ejercicio consiste en escribir un programa en Python que construya 
un glosario de términos pertenecientes al mundo de las criptomonedas con sus 
correspondientes significados y, a la vez, permita consultar un término dado 
por el usuario. En el caso que no existe el término solicitado, se le da la 
posibilidad al usuario de incorporar este término con su correspondiente 
significado.

Te recomendamos usar archivos y diccionarios de Python para resolver este ejercicio."""
termino=None
terminos_criptos={}

def consulta_termino_cripto(termin):
	descripcion=terminos_criptos.get(termin)
	print(termin,descripcion)

def agregar_diccionario(termin,descrip):
        if termin in terminos_criptos:
          print("termino ya se encuentra en el diccionario")
        else:
          terminos_criptos[termin]=[descrip]
          


while termino != 'x':
      termino=input("por favor ingrese el termino:  \n(si no desea agregar mas presione x)\n(se desea consultar un ternino c) ")
      if termino =='x':
      	print("se agregaron los terminos al diccionario de manera exitosa")
      elif termino == 'c':
        term=input("por favor ingrese el termino a consultar")
        encontrado=consulta_termino_cripto(term)
        if encontrado == None:
        	print("el termino ingresado no se encuentra en el diccionario")
      else:
        descripcion=input("ingrese la descripcion "+termino+": ")
        agregar_diccionario(termino,descripcion)
      pass

