# Atributos privados y métodos getter/setter
class Persona:
    """Clase base Persona (abstracción)"""

    def __init__(self, cedula, nombre, apellido, telefono=""):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono

    # Getters
    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_nombre_completo(self):
        return self.__nombre + " " + self.__apellido

    def get_telefono(self):
        return self.__telefono

    # Setters
    def set_telefono(self, telefono):
        self.__telefono = telefono

    # Método que las subclases deben implementar (abstracción)
    def tipo_socio(self):
        raise NotImplementedError("Las subclases deben implementar tipo_socio()")

    def __str__(self):
        return self.get_nombre_completo() + " - Cédula: " + self.__cedula
