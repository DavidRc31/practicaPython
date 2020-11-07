""" desarrolles tu propia billetera digital de tipo Desktop con interfaz de texto, que soporte monedas registradas en coinmarketcap.com, y que permita:

Enviar un monto en USD de alguna de las criptomonedas a un destinatario indicado (identificado por un código)
Recibir de un enviador (identificado por un código) una cantidad de alguna criptomoneda
Consultar el balance de cada una de las criptomonedas en USD
Consultar el balance general del usuario en USD usando el precio de la criptomoneda provisto por las APIs de coinmarketcap.com
Emitir un histórico de transacciones del usuario indicando fecha, moneda, cantidad y monto en USD para el momento de la transacción
Todas las transacciones realizadas por el usuario deben ser almacenadas y mantenidas, así como las cantidades de cada una de las criptomonedas que posea
Colocar un menú de opciones con:"""

import requests
from datetime import datetime

def esmoneda(cripto):
    return cripto in monedas

monedas_list=[]#lista criptomonedas
monedas_name_list=[]#lista nombres de criptomonedas
monedas_market_cap_list=[]#lista de cotizacion de criptomonedas
cripto_saldo=[]#Declarando lista saldo de criptomonedas
fecha_recibiendo=[]#Declarando lista fecha transacciones recividas
fecha_transaccion=[]#Declarando lista fecha transacciones recividas
monedas_recib=[]#Declaracion de monedas recibiedas
monedas_transf=[]#declarando  monedas transferidas
cantidad_recib=[]#declarando cantidad de monedas recibidas
key_remitente=[]#declarando key remitente 
cantidad_transf=[]#declarando monto transferido
key_transacc=[]#declarando clave de operacion cripto
tipo_ope=[]#declarando tipo operacion
monto_total_USD_tr=[] #DECLARANDO MONTO TOTAL TRANSFERENCIA
monto_total_USD_rc=[] #DECLARANDO MONTO TOTAL RECIBIDO
operacion_rec=[] #declarnado operacion recibir
operacion_transf=[] #declarando operacion transacciones
monto_total=0#variable global monto total criptomonedas
j=0     


COINMARKET_API_KEY = "5a77b76c-e4c7-4b44-993b-9e6f0f734891"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}

#parametros = {'symbol': symbol}
data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

for cripto in data["data"]:
    monedas_list.append(cripto["symbol"])
    monedas_name_list.append(cripto["name"])
    monedas_market_cap_list.append(cripto["quote"]["USD"]["price"])

monedas=tuple(monedas_list)
cripto_cotizacion=tuple(monedas_market_cap_list)

def validar_moneda(moned):
    while not esmoneda(moned):
        print("Moneda Invalida.")
        moned=input("Por favor ingrese el nombre de una moneda valida: ")
    else:
        return moned


def validar_codigo(codig):
    while codig==COINMARKET_API_KEY or codig==None:
        print("por favor digite un codigo valido")
    else:
        return codig

def encontrar_moneda(moned):
    for x in range(0,len(monedas)):
        if monedas[x] == moned:
            return x
           # print("la posicion de de ", moned, "es", x)
      
    
while j in range(0,len(monedas)):
    cripto_saldo.append(0)
    j=j+1
        #cripto_saldo[j]=0

#var_cotizacion=0.4785
"""
def inicializando_saldo():
    while j in range(0,len(monedas)):
        #cripto_saldo[j]=0
        cripto_saldo.append(0)

"""
        

#======================
#CRIPTOMONEDAS
class Criptomoneda(object):
    def __init__(self, nombre,  saldo, codigo_key):
      self.nombre = nombre
      self.saldo = saldo
      self.cotizacion = 0
      self.codigo_key=codigo_key
      

      
    def indicarNombre(self, nombre):
        self.nombre=validar_moneda(nombre)
      
 
    def indicarCotizacion(self, cotizacion):
        self.cotizacion=cotizacion
      
 
    def indicarSaldo(self, saldo):
        i=encontrar_moneda(self.nombre)
        cripto_saldo[i]=cripto_saldo[i]+saldo#Sumar cantidad de monedas al saldo.
        self.saldo=cripto_saldo[i]
 
    def mostrarNombre(self):
        return self.nombre
      

    def salidaSaldo(self, saldo):
        i=encontrar_moneda(self.nombre)
        cripto_saldo[i]=cripto_saldo[i]-saldo#Restando cantidad de monedas al saldo.
        self.saldo=cripto_saldo[i]
 
    def cotizacionCripto(self):
        y=encontrar_moneda(self.nombre)
        #self.cotizacion=cripto_cotizacion[y]
        #return self.cotizacion
        return cripto_cotizacion[y]
      
 
    def mostrarSaldo(self):  
        #self.indicarSaldo(self.saldo)
        i=encontrar_moneda(self.nombre)
        self.saldo=cripto_saldo[i]
        monto_USD=self.saldo*self.cotizacionCripto()
        global monto_total
        monto_total=monto_total+monto_USD
        return  self.saldo


#MENU

opcion=None

ahora = datetime.now()
fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")
opcion1="Presione 1 Para Recibir cantidad :"
opcion2="Presione 2 Para Transferir monto :"
opcion3="Presione 3 Para Mostrar balance una moneda :"
opcion4="Presione 4 Para Mostrar balance general :"
opcion5="Presione 5 Para Mostrar histórico de transacciones :"
opcion6="Presione 6 Para Mostrar Salir del programa :"
while opcion != '6':
      print("\n ****** MENU ******")
      opcion=input(str('Por favor elija la operacion a realizar\n'+opcion1+'\n'+opcion2+'\n'+opcion3+'\n'+opcion4+'\n'+opcion5+'\n'+opcion6))
      if opcion =='1':
        #Resivir
        monto_temp_USD=0
        print("****** RECIBIENDO TRANSFERENCIA *****")
        moneda=input("digite moneda")
        cantidad_moneda=float(input("Digite cantidad :"))
        codigo=input("Digite codigo")
        cod_validado=validar_codigo(codigo)
        cripto=Criptomoneda(moneda,cantidad_moneda,cod_validado)
        cripto.indicarNombre(moneda)
        cripto.indicarSaldo(cantidad_moneda)
        print("transferencia recibida exitoxamente!")
        fecha_recibiendo.append(ahora.strftime("%Y-%m-%d %H:%M:%S"))
        monedas_recib.append(cripto.mostrarNombre())
        cantidad_recib.append(cripto.mostrarSaldo())
        key_remitente.append(cod_validado)
        operacion_rec.append("Recibida")
        monto_temp_USD=monto_total
        monto_total_USD_rc.append(monto_temp_USD)
        

      elif opcion == '2':
        print("***** REALIZANDO TRANSFERENCIA *****")
        moneda=input("digite moneda")
        cantidad_moneda=float(input("Digite cantidad :"))
        codigo=input("Digite codigo")
        cod_validado=validar_codigo(codigo)
        cripto=Criptomoneda(moneda,cantidad_moneda,cod_validado)
        cripto.salidaSaldo(cantidad_moneda)
        print("transferencia realizada exitoxamente!")
        fecha_transaccion.append(ahora.strftime("%Y-%m-%d %H:%M:%S"))
        monedas_transf.append(cripto.mostrarNombre())
        cantidad_transf.append(cripto.mostrarSaldo())
        key_transacc.append(cod_validado)
        operacion_transf.append("Realizada")
        monto_temp_USD=monto_total
        monto_total_USD_tr.append(monto_temp_USD)
        #fech_trans=tuple(fecha_transaccion)

      elif opcion == '3':
        print("***** VALANCE DE CRIPTOMONEDAS")
        cantidad_moneda=0#saldo default
        codigo=COINMARKET_API_KEY#key default
        moneda=input("Digite moneda: ")
        cripto=Criptomoneda(moneda,cantidad_moneda,codigo)
        valance=cripto.mostrarSaldo()
        monto_USD=monto_total
        print("El balance de la criptomoneda "+moneda+" es de: "+str(valance)+" con un monto USD actual de: "+str(monto_USD))
        #fecha_=ahora.strftime("%Y-%m-%d %H:%M:%S")

      elif opcion == '4':
        print("******BALANCE GENERAL******")
        cantidad_moneda=0#saldo default
        codigo=COINMARKET_API_KEY#key default
       #S moneda="BTC"#moneda default
        k=0
        while k in range(0,len(monedas)):
            cripto=Criptomoneda(monedas[k],cantidad_moneda,codigo)
            print("El balance de la criptomoneda "+cripto.mostrarNombre()+"es de:"+str(cripto.mostrarSaldo()))
            k+=1
        else:
            print("El monto total en USD de todas las monedas es: "+str(monto_total))
            pass

      elif opcion == '5':
        print("****** HISTORICO DE TRANSACCIONES")
        print("Nº----- FECHA OPERACION--------MONEDA--------TIPO OPERACION ---------CODIGO USUARIO --------CANTIDAD OPERACION-------MONTO")
        r=0
        n=0
        while r <= len(key_remitente):
            n+=1
            print(n+"----"+str(fecha_recibiendo[r])+"-----"+monedas_recib[r]+"--------"+operacion_rec[r]+"------"+key_remitente[r]+"-----"+str(cantidad_recib[r])+"-----"+str(monto_total_USD_rc))
            pass

        print("Nº----- FECHA OPERACION--------MONEDA--------TIPO OPERACION ---------CODIGO USUARIO --------CANTIDAD OPERACION-------MONTO")  
        while r <= len(key_transacc):
            n+=1
            print(n+"----"+str(fecha_transaccion[r])+"-----"+monedas_transf[r]+"--------"+operacion_transf[r]+"------"+key_transacc[r]+"-----"+str(cantidad_transf[r])+"-----"+str(monto_total_USD_tr))
            pass

else:
    print("A finalizado las operaciones exitosamente!!")
    pass
