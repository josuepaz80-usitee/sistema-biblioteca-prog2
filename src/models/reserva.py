"""Clase Reserva - representa una reserva en cola"""
from datetime import date
from src.models.socio import Socio
from src.models.libro import Libro


class Reserva:
    """Representa la reserva de un ejemplar no disponible"""

    def __init__(self, socio: Socio, libro: Libro, fecha: date = None):
        self.__socio = socio
        self.__libro = libro
        self.__fecha = fecha or date.today()
        self.__activa = True

    @property
    def socio(self) -> Socio:
        return self.__socio

    @property
    def libro(self) -> Libro:
        return self.__libro

    @property
    def fecha(self) -> date:
        return self.__fecha

    @property
    def activa(self) -> bool:
        return self.__activa

    def cancelar(self):
        self.__activa = False

    def __str__(self) -> str:
        estado = "Activa" if self.__activa else "Cancelada"
        return f"Reserva: {self.__libro.titulo} → {self.__socio.nombre_completo} [{estado}]"
