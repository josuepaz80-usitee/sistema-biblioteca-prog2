"""Clase Estudiante - hereda de Persona"""
from src.models.persona import Persona


class Estudiante(Persona):
    """Representa un estudiante universitario"""

    def __init__(self, cedula: str, nombre: str, apellido: str,
                 carrera: str, semestre: int, telefono: str = ""):
        # Llama al constructor del padre
        super().__init__(cedula, nombre, apellido, telefono)
        self.__carrera = carrera
        self.__semestre = semestre

    @property
    def carrera(self) -> str:
        return self.__carrera

    @property
    def semestre(self) -> int:
        return self.__semestre

    def tipo_socio(self) -> str:
        return "Estudiante"

    def __str__(self) -> str:
        return f"{super().__str__()} | {self.tipo_socio()} - {self.__carrera} ({self.__semestre}° sem)"
