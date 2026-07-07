"""Clase Libro - representa un ejemplar del catálogo"""
class Libro:
    """Representa un libro en el catálogo de la biblioteca"""

    def __init__(self, isbn: str, titulo: str, autor: str,
                 editorial: str, anio: int, ejemplares: int = 1):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__anio = anio
        self.__ejemplares = ejemplares
        self.__disponibles = ejemplares

    # Getters
    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def autor(self) -> str:
        return self.__autor

    @property
    def editorial(self) -> str:
        return self.__editorial

    @property
    def anio(self) -> int:
        return self.__anio

    @property
    def ejemplares(self) -> int:
        return self.__ejemplares

    @property
    def disponibles(self) -> int:
        return self.__disponibles

    def prestar_ejemplar(self) -> bool:
        """Presta un ejemplar si hay disponibles"""
        if self.__disponibles > 0:
            self.__disponibles -= 1
            return True
        return False

    def devolver_ejemplar(self) -> bool:
        """Devuelve un ejemplar"""
        if self.__disponibles < self.__ejemplares:
            self.__disponibles += 1
            return True
        return False

    def esta_disponible(self) -> bool:
        return self.__disponibles > 0

    def __str__(self) -> str:
        return f"{self.__titulo} - {self.__autor} ({self.__anio}) | Disp: {self.__disponibles}/{self.__ejemplares}"
