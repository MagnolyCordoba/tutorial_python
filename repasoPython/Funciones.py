#Entradas
base = float (input("Ingrese base: "))
altura = float (input("Ingrese altura : "))

# procesos
def calcularAreaTriangulo(b,al):
    Area = (b*al)/2
    return Area

#Salida
resultado = calcularAreaTriangulo(base,altura)
print("el area del triangulo es:", resultado)

#funcion con argumentos por defecto

def mostraPais(pais = "Colombia"):
    print("Yo soy de : "+ pais)

mostraPais("Suiza")
mostraPais("Uruguay")
mostraPais("Ecuador")
mostraPais()
mostraPais("Brazil")