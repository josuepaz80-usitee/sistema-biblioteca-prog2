# Clase Libro - representa un libro del catálogo
class Libro:
    """Representa un libro en el catálogo"""

    def __init__(self, isbn, titulo, autor, editorial, anio, ejemplares=1):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__anio = anio
        self.__ejemplares = ejemplares
        self.__disponibles = ejemplares  # Inicialmente todos disponibles

    # Getters
    def get_isbn(self):
        return self.__isbn

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_editorial(self):
        return self.__editorial

    def get_anio(self):
        return self.__anio

    def get_ejemplares(self):
        return self.__ejemplares

    def get_disponibles(self):
        return self.__disponibles

    # Métodos del dominio
    def prestar_ejemplar(self):
        """Reduce en 1 los disponibles si hay stock"""
        if self.__disponibles > 0:
            self.__disponibles -= 1
            return True
        return False

    def devolver_ejemplar(self):
        """Aumenta en 1 los disponibles"""
        if self.__disponibles < self.__ejemplares:
            self.__disponibles += 1
            return True
        return False

    def esta_disponible(self):
        return self.__disponibles > 0

    def __str__(self):
        return (self.__titulo + " - " + self.__autor + " (" + str(self.__anio)
                + ") | Disp: " + str(self.__disponibles) + "/" + str(self.__ejemplares))
