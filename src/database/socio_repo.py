# ============================================================
# Cindy Ayoví — Repositorio de Socios (CRUD completo)
# CREATE: insertar nuevo socio (estudiante o docente)
# READ: buscar por cédula, listar todos ordenados
# UPDATE: actualizar teléfono
# DELETE: eliminar socio
# ============================================================

# CRUD para la tabla socios (CREATE, READ, UPDATE, DELETE)
from src.database.db_manager import DatabaseManager


class SocioRepository:
    """Operaciones CRUD para la tabla socios"""

    def __init__(self, db):
        self.__db = db

    # CREATE - Insertar un nuevo socio
    def insertar(self, cedula, nombre, apellido, tipo,
                 carrera_depto, semestre, telefono):
        cursor = self.__db.get_cursor()
        cursor.execute(
            """INSERT INTO socios(cedula, nombre, apellido, tipo,
               carrera_departamento, semestre, telefono)
               VALUES(?, ?, ?, ?, ?, ?, ?)""",
            (cedula, nombre, apellido, tipo, carrera_depto, semestre, telefono)
        )
        self.__db.get_connection().commit()

    # READ - Buscar socio por cedula
    def obtener_por_cedula(self, cedula):
        cursor = self.__db.get_cursor()
        cursor.execute("SELECT * FROM socios WHERE cedula = ?", (cedula,))
        return cursor.fetchone()

    # READ - Listar todos los socios
    def listar_todos(self):
        cursor = self.__db.get_cursor()
        cursor.execute("SELECT * FROM socios ORDER BY apellido, nombre")
        return cursor.fetchall()

    # UPDATE - Actualizar telefono
    def actualizar_telefono(self, cedula, telefono):
        cursor = self.__db.get_cursor()
        cursor.execute("UPDATE socios SET telefono = ? WHERE cedula = ?",
                       (telefono, cedula))
        self.__db.get_connection().commit()

    # DELETE - Eliminar socio
    def eliminar(self, cedula):
        cursor = self.__db.get_cursor()
        cursor.execute("DELETE FROM socios WHERE cedula = ?", (cedula,))
        self.__db.get_connection().commit()
