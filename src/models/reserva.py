# Clase Reserva - reserva de un ejemplar no disponible
from datetime import date
from src.models.socio import Socio
from src.models.libro import Libro


class Reserva:
    """Reserva de un libro cuando no hay ejemplares disponibles"""

    def __init__(self, socio, libro, fecha=None):
        self.__socio = socio
        self.__libro = libro
        if fecha is None:
            self.__fecha = date.today()
        else:
            self.__fecha = fecha
        self.__activa = True

    def get_socio(self):
        return self.__socio

    def get_libro(self):
        return self.__libro

    def get_fecha(self):
        return self.__fecha

    def esta_activa(self):
        return self.__activa

    def cancelar(self):
        self.__activa = False

    def __str__(self):
        if self.__activa:
            estado = "Activa"
        else:
            estado = "Cancelada"
        return ("Reserva: " + self.__libro.get_titulo() + " → "
                + self.__socio.get_nombre_completo() + " [" + estado + "]")
