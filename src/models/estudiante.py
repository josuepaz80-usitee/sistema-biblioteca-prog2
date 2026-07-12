# ============================================================
# Henry Pazmiño — Subclase Estudiante (Herencia + Polimorfismo)
# Demuestra herencia simple y polimorfismo con tipo_socio()
# ============================================================

# Hereda de Persona (herencia simple)
from src.models.persona import Persona


class Estudiante(Persona):
    """Subclase: Representa un estudiante universitario"""

    def __init__(self, cedula, nombre, apellido, carrera, semestre, telefono=""):
        # Llama al constructor de la clase padre
        Persona.__init__(self, cedula, nombre, apellido, telefono)
        self.__carrera = carrera
        self.__semestre = semestre

    # Getters
    def get_carrera(self):
        return self.__carrera

    def get_semestre(self):
        return self.__semestre

    # Polimorfismo: implementación propia de tipo_socio()
    def tipo_socio(self):
        return "Estudiante"

    def __str__(self):
        return (Persona.__str__(self) + " | " + self.tipo_socio()
                + " - " + self.__carrera + " (" + str(self.__semestre) + "° sem)")
