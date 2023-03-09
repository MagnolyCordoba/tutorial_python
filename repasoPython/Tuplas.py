#Tuplas
colores = ("rojo", "azul", "verde", "amarillo")

print(colores)
#Saber la longitud de una lista o tupla
colores_tupla = ("rojo", "azul", "verde","amarillo")
colores_lista = ["rojo", "azul", "verde","amarillo"]

print(len(colores_tupla))
print(len(colores_lista))

#convertir una lista en tupla
lista = ['rojo', 'azul', 'verde', 'amarillo']
tupla = tuple(lista)
print(tupla)
#convertir tupla en lista
tupla = ('rojo', 'azul', 'verde', 'amarillo')
lista = list(tupla)
print(type(lista))