"""Clase Prestamo - representa un préstamo de libro"""
from datetime import date, timedelta
from src.models.socio import Socio
from src.models.libro import Libro


class Prestamo:
    """Representa el préstamo de un libro a un socio"""

    def __init__(self, socio: Socio, libro: Libro, fecha_prestamo: date = None):
        self.__socio = socio
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo or date.today()
        self.__fecha_devolucion = None

    @property
    def socio(self) -> Socio:
        return self.__socio

    @property
    def libro(self) -> Libro:
        return self.__libro

    @property
    def fecha_prestamo(self) -> date:
        return self.__fecha_prestamo

    @property
    def fecha_devolucion(self) -> date:
        return self.__fecha_devolucion

    def devolver(self, fecha: date = None):
        """Registra la devolución del libro"""
        self.__fecha_devolucion = fecha or date.today()
        self.__libro.devolver_ejemplar()

    def esta_pendiente(self) -> bool:
        return self.__fecha_devolucion is None

    def dias_retraso(self) -> int:
        """Calcula días de retraso (máximo 14 días)"""
        if self.esta_pendiente():
            today = date.today()
            return max(0, (today - self.__fecha_prestamo).days - 14)
        return 0

    def __str__(self) -> str:
        estado = "Pendiente" if self.esta_pendiente() else "Devuelto"
        return f"{self.__libro.titulo} → {self.__socio.nombre_completo} [{estado}]"
