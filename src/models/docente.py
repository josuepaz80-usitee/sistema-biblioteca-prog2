"""Clase Docente - hereda de Persona"""
from src.models.persona import Persona


class Docente(Persona):
    """Representa un docente universitario"""

    def __init__(self, cedula: str, nombre: str, apellido: str,
                 departamento: str, telefono: str = ""):
        super().__init__(cedula, nombre, apellido, telefono)
        self.__departamento = departamento

    @property
    def departamento(self) -> str:
        return self.__departamento

    def tipo_socio(self) -> str:
        return "Docente"

    def __str__(self) -> str:
        return f"{super().__str__()} | {self.tipo_socio()} - Depto. {self.__departamento}"
