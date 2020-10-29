numero=int(input("indique un valor entero: "))
if numero%3==0 and numero%5==0:
     print("FizzBuzz")
elif numero%3==0:
      print("Fizz")
elif numero%5==0:
      print("Buzz")
else:
	print(numero)