# ============================================================
# Henry Pazmiño — Subclase Docente (Herencia + Polimorfismo)
# Demuestra herencia simple y polimorfismo con tipo_socio()
# ============================================================

# Hereda de Persona (herencia simple)
from src.models.persona import Persona


class Docente(Persona):
    """Subclase: Representa un docente universitario"""

    def __init__(self, cedula, nombre, apellido, departamento, telefono=""):
        Persona.__init__(self, cedula, nombre, apellido, telefono)
        self.__departamento = departamento

    # Getter
    def get_departamento(self):
        return self.__departamento

    # Polimorfismo: implementación propia de tipo_socio()
    def tipo_socio(self):
        return "Docente"

    def __str__(self):
        return (Persona.__str__(self) + " | " + self.tipo_socio()
                + " - Depto. " + self.__departamento)
