#Estructuras selectivas y repetitivas
#estructura repetitiva while
#Realizar un programa que imprima los números del 1 al 100
x=1
while x<=100:
    print(x)
    x=x+1

# estructura repetitiva for
#Realizar un programa que solicite la carga de un valor entero del 1 al 10.
# Mostrar después la tabla de multiplicar de dicho número.
num=int(input("Ingrese un numero: "))
for x in range(1,11):
    tabla=num*x
    print(tabla)

#estructuras selectivas anidadas
x = 34
if x %  2 == 0:
  if x > 10:
     print("Este número es par y es mayor que 10")
  else:
    print("Este número es par, pero no mayor 10")
else:
  print ("El número no es par. Así que punto de verificación más.")


#estructura selectiva  simple if
x = 5
if x > 4:
  print("¡La condición era verdadera!") #Esta sentencia se ejecuta

  #estructura selectiva simple else
  y = 3

  if y > 4:
      print("¡No voy a imprimir!")  # esta sentencia no se ejecuta
  else:
      print("¡La condición no era verdadera!")  # esta sentencia se ejecuta

#estructura selectiva  simple elif
z = 7

if z > 8:
  print("¡No voy a imprimir!") #esta sentencia no se ejecuta
elif z > 5:
  print("¡Yo lo haré!") #esta sentencia se ejecuta
elif z > 6:
  print("¡Tampoco voy a imprimir!") #esta sentencia no se ejecuta
else:
  print("¡Yo tampoco!") #esta sentencia no se ejecuta

  
