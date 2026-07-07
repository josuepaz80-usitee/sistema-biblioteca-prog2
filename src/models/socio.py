"""Clase Socio - wrapper polimórfico"""
from src.models.persona import Persona
from src.models.estudiante import Estudiante
from src.models.docente import Docente


class Socio:
    """Wrapper que maneja Estudiante o Docente polimórficamente"""

    def __init__(self, persona: Persona):
        self.__persona = persona  # Composición con Persona

    @property
    def persona(self) -> Persona:
        return self.__persona

    @property
    def cedula(self) -> str:
        return self.__persona.cedula

    @property
    def nombre_completo(self) -> str:
        return self.__persona.nombre_completo

    def tipo_socio(self) -> str:
        return self.__persona.tipo_socio()

    def __str__(self) -> str:
        return str(self.__persona)
