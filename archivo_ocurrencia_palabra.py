nombre_archivo=input("Ingrese el nombre del archivo que contiene las palabras")
archivo= open(nombre_archivo,"r")#abriendo archivo en modo de lectura

texto = archivo.read() #la variable contendra el contenido del archivo
palabras = texto.split()#creamos una lista con las palabras
ocurrencias = {} #inicializamos un diccionario que contendra las ocurrencias

for palabra in palabras: #para cada palabra contenida en la lista palabras 
    if ocurrencias.get(palabra):#se actualizara el diccionario ocurrencia con las palabras 
       ocurrencias[palabra]+=1 #por cada ocurrencia de la palabra 
    else:
        ocurrencias[palabra]=1
#se determina cual de los elementos de de ocurrencia tiene mayor ocurrencia
maxpar=None, 0 #palabra, cantidad de ocurrencia
for palabra, cantidad in ocurrencias.items():
    if maxpar[1]<cantidad:
        maxpar=palabra,cantidad

print("La palabra con mayor cantidad de repeticion es", maxpar[0],"repetida",maxpar[1],"veces")
