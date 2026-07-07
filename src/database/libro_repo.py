"""CRUD para la tabla libros"""
from src.database.db_manager import DatabaseManager


class LibroRepository:
    """Operaciones CRUD para libros"""

    def __init__(self, db: DatabaseManager):
        self.__db = db

    # CREATE
    def insertar(self, isbn: str, titulo: str, autor: str,
                 editorial: str, anio: int, ejemplares: int = 1):
        cursor = self.__db.cursor
        cursor.execute(
            """INSERT INTO libros (isbn, titulo, autor, editorial, anio, ejemplares, disponibles)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (isbn, titulo, autor, editorial, anio, ejemplares, ejemplares)
        )
        self.__db.connection.commit()

    # READ
    def obtener_por_isbn(self, isbn: str):
        cursor = self.__db.cursor
        cursor.execute("SELECT * FROM libros WHERE isbn = ?", (isbn,))
        return cursor.fetchone()

    def buscar_por_titulo(self, titulo: str):
        cursor = self.__db.cursor
        cursor.execute("SELECT * FROM libros WHERE titulo LIKE ?", (f"%{titulo}%",))
        return cursor.fetchall()

    def listar_todos(self):
        cursor = self.__db.cursor
        cursor.execute("SELECT * FROM libros ORDER BY titulo")
        return cursor.fetchall()

    # UPDATE
    def actualizar_disponibles(self, isbn: str, disponibles: int):
        cursor = self.__db.cursor
        cursor.execute("UPDATE libros SET disponibles = ? WHERE isbn = ?",
                       (disponibles, isbn))
        self.__db.connection.commit()

    # DELETE
    def eliminar(self, isbn: str):
        cursor = self.__db.cursor
        cursor.execute("DELETE FROM libros WHERE isbn = ?", (isbn,))
        self.__db.connection.commit()
