# Clase para la declaracion de tipo de socio (polimorfismo)
from src.models.persona import Persona
from src.models.estudiante import Estudiante
from src.models.docente import Docente


class Socio:
    """Wrapper que contiene una Persona (Estudiante o Docente)"""

    def __init__(self, persona):
        self.__persona = persona

    def get_persona(self):
        return self.__persona

    def get_cedula(self):
        return self.__persona.get_cedula()

    def get_nombre_completo(self):
        return self.__persona.get_nombre_completo()

    # Polimorfismo: llama al método según el tipo real de persona
    def tipo_socio(self):
        return self.__persona.tipo_socio()

    def __str__(self):
        return str(self.__persona)
