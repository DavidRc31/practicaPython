"""variable VALID_ALPHA_MAIL"""
valid_alpha_user = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_."

while True: 
  user = input("ingrese el nombre de ususario: ")
  if (len(user)>4):
       a=set(valid_alpha_user)
       b=set(user)
       if len(b-a)>0:
          print("usuario invalido")
          continue
       else:
          print("usuario valido")
          break
  else:
       print("Usuario valido")
