# CRUD para la tabla libros (CREATE, READ, UPDATE, DELETE)
from src.database.db_manager import DatabaseManager


class LibroRepository:
    """Operaciones CRUD para la tabla libros"""

    def __init__(self, db):
        self.__db = db

    # CREATE - Insertar un nuevo libro
    def insertar(self, isbn, titulo, autor, editorial, anio, ejemplares=1):
        cursor = self.__db.get_cursor()
        cursor.execute(
            """INSERT INTO libros(isbn, titulo, autor, editorial,
               anio, ejemplares, disponibles)
               VALUES(?, ?, ?, ?, ?, ?, ?)""",
            (isbn, titulo, autor, editorial, anio, ejemplares, ejemplares)
        )
        self.__db.get_connection().commit()

    # READ - Buscar libro por ISBN
    def obtener_por_isbn(self, isbn):
        cursor = self.__db.get_cursor()
        cursor.execute("SELECT * FROM libros WHERE isbn = ?", (isbn,))
        return cursor.fetchone()

    # READ - Buscar libros por titulo (busqueda parcial)
    def buscar_por_titulo(self, titulo):
        cursor = self.__db.get_cursor()
        cursor.execute("SELECT * FROM libros WHERE titulo LIKE ?",
                       ("%" + titulo + "%",))
        return cursor.fetchall()

    # READ - Listar todos los libros
    def listar_todos(self):
        cursor = self.__db.get_cursor()
        cursor.execute("SELECT * FROM libros ORDER BY titulo")
        return cursor.fetchall()

    # UPDATE - Actualizar disponibles
    def actualizar_disponibles(self, isbn, disponibles):
        cursor = self.__db.get_cursor()
        cursor.execute("UPDATE libros SET disponibles = ? WHERE isbn = ?",
                       (disponibles, isbn))
        self.__db.get_connection().commit()

    # DELETE - Eliminar libro
    def eliminar(self, isbn):
        cursor = self.__db.get_cursor()
        cursor.execute("DELETE FROM libros WHERE isbn = ?", (isbn,))
        self.__db.get_connection().commit()
