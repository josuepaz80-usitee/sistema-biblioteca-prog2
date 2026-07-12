# ============================================================
# Henry Pazmiño — Clase Préstamo
# Relaciona un Socio con un Libro en una fecha determinada
# Control de estado: pendiente vs devuelto
# ============================================================

# Clase Prestamo - representa el prestamo de un libro
from datetime import date
from src.models.socio import Socio
from src.models.libro import Libro


class Prestamo:
    """Préstamo de un libro a un socio"""

    def __init__(self, socio, libro, fecha_prestamo=None):
        self.__socio = socio
        self.__libro = libro
        if fecha_prestamo is None:
            self.__fecha_prestamo = date.today()
        else:
            self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = None

    def get_socio(self):
        return self.__socio

    def get_libro(self):
        return self.__libro

    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    def devolver(self, fecha=None):
        """Registra la devolución del libro"""
        if fecha is None:
            self.__fecha_devolucion = date.today()
        else:
            self.__fecha_devolucion = fecha
        self.__libro.devolver_ejemplar()

    def esta_pendiente(self):
        return self.__fecha_devolucion is None

    def __str__(self):
        if self.esta_pendiente():
            estado = "Pendiente"
        else:
            estado = "Devuelto"
        return (self.__libro.get_titulo() + " → "
                + self.__socio.get_nombre_completo() + " [" + estado + "]")
