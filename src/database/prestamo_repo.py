# ============================================================
# Cindy Ayovi — Repositorio de Prestamos (CRUD completo)
# CREATE: registrar prestamo
# READ: buscar por ID, listar todos, listar por socio
# UPDATE: registrar devolucion (fecha_devolucion)
# DELETE: eliminar prestamo
# ============================================================

# CRUD para la tabla prestamos (CREATE, READ, UPDATE, DELETE)
from src.database.db_manager import DatabaseManager


class PrestamoRepository:
    """Operaciones CRUD para la tabla prestamos"""

    def __init__(self, db):
        self.__db = db

    # CREATE - Registrar un nuevo prestamo
    def insertar(self, cedula_socio, isbn_libro, fecha_prestamo):
        cursor = self.__db.get_cursor()
        cursor.execute(
            """INSERT INTO prestamos(cedula_socio, isbn_libro, fecha_prestamo)
               VALUES(?, ?, ?)""",
            (cedula_socio, isbn_libro, fecha_prestamo)
        )
        self.__db.get_connection().commit()
        return cursor.lastrowid

    # READ - Buscar prestamo por ID
    def obtener_por_id(self, prestamo_id):
        cursor = self.__db.get_cursor()
        cursor.execute("SELECT * FROM prestamos WHERE id = ?", (prestamo_id,))
        return cursor.fetchone()

    # READ - Listar todos los prestamos (ordenados del mas reciente)
    def listar_todos(self):
        cursor = self.__db.get_cursor()
        cursor.execute("SELECT * FROM prestamos ORDER BY id DESC")
        return cursor.fetchall()

    # READ - Listar prestamos de un socio
    def listar_por_socio(self, cedula_socio):
        cursor = self.__db.get_cursor()
        cursor.execute(
            "SELECT * FROM prestamos WHERE cedula_socio = ? ORDER BY id DESC",
            (cedula_socio,)
        )
        return cursor.fetchall()

    # READ - Listar prestamos pendientes (sin devolucion)
    def listar_pendientes(self):
        cursor = self.__db.get_cursor()
        cursor.execute(
            "SELECT * FROM prestamos WHERE fecha_devolucion IS NULL ORDER BY id DESC"
        )
        return cursor.fetchall()

    # UPDATE - Registrar devolucion
    def registrar_devolucion(self, prestamo_id, fecha_devolucion):
        cursor = self.__db.get_cursor()
        cursor.execute(
            "UPDATE prestamos SET fecha_devolucion = ? WHERE id = ?",
            (fecha_devolucion, prestamo_id)
        )
        self.__db.get_connection().commit()

    # DELETE - Eliminar prestamo
    def eliminar(self, prestamo_id):
        cursor = self.__db.get_cursor()
        cursor.execute("DELETE FROM prestamos WHERE id = ?", (prestamo_id,))
        self.__db.get_connection().commit()
