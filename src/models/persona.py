"""Clase abstracta Persona - base del sistema"""
from abc import ABC, abstractmethod


class Persona(ABC):
    """Clase abstracta que representa a una persona"""

    def __init__(self, cedula: str, nombre: str, apellido: str, telefono: str = ""):
        # Atributos privados (encapsulamiento)
        self.__cedula = cedula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono

    # Getters y Setters
    @property
    def cedula(self) -> str:
        return self.__cedula

    @cedula.setter
    def cedula(self, valor: str):
        self.__cedula = valor

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        self.__nombre = valor

    @property
    def apellido(self) -> str:
        return self.__apellido

    @apellido.setter
    def apellido(self, valor: str):
        self.__apellido = valor

    @property
    def nombre_completo(self) -> str:
        return f"{self.__nombre} {self.__apellido}"

    @property
    def telefono(self) -> str:
        return self.__telefono

    @telefono.setter
    def telefono(self, valor: str):
        self.__telefono = valor

    @abstractmethod
    def tipo_socio(self) -> str:
        """Retorna el tipo de socio"""
        pass

    def __str__(self) -> str:
        return f"{self.nombre_completo} - Cédula: {self.__cedula}"
