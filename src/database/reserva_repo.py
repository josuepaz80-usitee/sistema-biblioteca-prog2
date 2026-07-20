# ============================================================
# Cindy Ayovi — Repositorio de Reservas (CRUD completo)
# CREATE: nueva reserva (cola de espera)
# READ: listar reservas activas, por socio, por libro
# UPDATE: marcar como inactiva
# DELETE: eliminar reserva
# ============================================================

# CRUD para la tabla reservas (CREATE, READ, UPDATE, DELETE)
from src.database.db_manager import DatabaseManager


class ReservaRepository:
    """Operaciones CRUD para la tabla reservas"""

    def __init__(self, db):
        self.__db = db

    # CREATE - Registrar una nueva reserva
    def insertar(self, cedula_socio, isbn_libro, fecha_reserva):
        cursor = self.__db.get_cursor()
        cursor.execute(
            """INSERT INTO reservas(cedula_socio, isbn_libro, fecha_reserva)
               VALUES(?, ?, ?)""",
            (cedula_socio, isbn_libro, fecha_reserva)
        )
        self.__db.get_connection().commit()
        return cursor.lastrowid

    # READ - Buscar reserva por ID
    def obtener_por_id(self, reserva_id):
        cursor = self.__db.get_cursor()
        cursor.execute("SELECT * FROM reservas WHERE id = ?", (reserva_id,))
        return cursor.fetchone()

    # READ - Listar todas las reservas activas
    def listar_activas(self):
        cursor = self.__db.get_cursor()
        cursor.execute(
            "SELECT * FROM reservas WHERE activa = 1 ORDER BY id ASC"
        )
        return cursor.fetchall()

    # READ - Listar reservas de un socio
    def listar_por_socio(self, cedula_socio):
        cursor = self.__db.get_cursor()
        cursor.execute(
            "SELECT * FROM reservas WHERE cedula_socio = ? ORDER BY id DESC",
            (cedula_socio,)
        )
        return cursor.fetchall()

    # READ - Listar reservas activas de un libro
    def listar_por_libro(self, isbn_libro):
        cursor = self.__db.get_cursor()
        cursor.execute(
            "SELECT * FROM reservas WHERE isbn_libro = ? AND activa = 1 ORDER BY id ASC",
            (isbn_libro,)
        )
        return cursor.fetchall()

    # UPDATE - Cancelar reserva (marcar como inactiva)
    def cancelar(self, reserva_id):
        cursor = self.__db.get_cursor()
        cursor.execute(
            "UPDATE reservas SET activa = 0 WHERE id = ?",
            (reserva_id,)
        )
        self.__db.get_connection().commit()

    # DELETE - Eliminar reserva
    def eliminar(self, reserva_id):
        cursor = self.__db.get_cursor()
        cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
        self.__db.get_connection().commit()
