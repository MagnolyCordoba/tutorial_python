from abc import ABCMeta

"""
costructor especial el cual permitira  instanciar un objeto del tipo 
requerido a partir de la informacion almacenada en un diccionario.
self : inicializar los atributos 
"""


class AbstractModelo(metaclass=ABCMeta):
    def __init__(self, data):
        for llave, valor in data.items():
            setattr(self, llave, valor)
