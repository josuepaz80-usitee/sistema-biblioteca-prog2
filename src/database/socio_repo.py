"""CRUD para la tabla socios"""
from src.database.db_manager import DatabaseManager


class SocioRepository:
    """Operaciones CRUD para socios"""

    def __init__(self, db: DatabaseManager):
        self.__db = db

    # CREATE
    def insertar(self, cedula: str, nombre: str, apellido: str,
                 tipo: str, carrera_depto: str = "", semestre: int = 0, telefono: str = ""):
        cursor = self.__db.cursor
        cursor.execute(
            """INSERT INTO socios (cedula, nombre, apellido, tipo,
               carrera_departamento, semestre, telefono)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (cedula, nombre, apellido, tipo, carrera_depto, semestre, telefono)
        )
        self.__db.connection.commit()

    # READ
    def obtener_por_cedula(self, cedula: str):
        cursor = self.__db.cursor
        cursor.execute("SELECT * FROM socios WHERE cedula = ?", (cedula,))
        return cursor.fetchone()

    def listar_todos(self):
        cursor = self.__db.cursor
        cursor.execute("SELECT * FROM socios ORDER BY apellido, nombre")
        return cursor.fetchall()

    # UPDATE
    def actualizar_telefono(self, cedula: str, telefono: str):
        cursor = self.__db.cursor
        cursor.execute("UPDATE socios SET telefono = ? WHERE cedula = ?",
                       (telefono, cedula))
        self.__db.connection.commit()

    # DELETE
    def eliminar(self, cedula: str):
        cursor = self.__db.cursor
        cursor.execute("DELETE FROM socios WHERE cedula = ?", (cedula,))
        self.__db.connection.commit()
