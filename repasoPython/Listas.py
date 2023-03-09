#Listas
edades = [20, 41, 6, 18, 23]

# Recorriendo los elementos
for edad in edades:
    print(edad)

# Recorriendo los índices
for i in range(len(edades)):
    print(edades[i])

# Con while y los índices
indice = 0

while indice < len(edades):
    print(edades[indice])
    indice += 1

#uniendo listas en python
edades = [20, 41, 6, 18, 23]

# Recorriendo los elementos
números = []

# Unimos la lista anterior con una nueva
números = números + [10, 5, 3]

print(números)
# Mostrará [10, 5, 3]

#remover un elemento con pop
palabras = ['hola', 'hello', 'ola']

palabras.pop(1)

print(palabras)
# Mostrará ['hola', 'ola']
# Creamos las listas (vacías al comienzo)
nombres = []
identificaciones = []

# Definimos un tamaño para las listas
# Lo puedes cambiar si quieres
tamaño = 3

# Leemos los datos y los agregamos a la lista
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")

    nombres.append(nombre)
    identificaciones.append(identificación)

#crear lista
lista_colores = ["rojo", "azul", "verde", "amarillo"]
#imprimir lista entera
lista_colores = ["rojo", "azul", "verde", "amarillo"]

print(lista_colores)



