# ============================================================
# Cindy Ayoví — Gestión de base de datos SQLite
# Conexión, creación de tablas (4 tablas relacionadas con FK)
# Sigue los pasos enseñados en clase por Ing. Bryan Vélez
# ============================================================

# PASO #1 CONECTAR LA BASE DE DATOS
# PASO #2 CREAR EL CURSOR
# PASO #3 CREAR LAS TABLAS
# PASO #4 INSERTAR DATOS
# PASO #5 GUARDAR CAMBIOS (COMMIT)
# PASO #6 CONSULTAR DATOS
# PASO #7 CERRAR CONEXION

import sqlite3
import os


class DatabaseManager:
    """Gestiona la conexion y operaciones con SQLite"""

    def __init__(self, db_path="db/biblioteca.db"):
        self.__db_path = db_path
        self.__conn = None

        # Crea la carpeta db/ si no existe
        carpeta = os.path.dirname(db_path)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)

    # PASO #1 CONECTAR LA BASE DE DATOS
    def connect(self):
        """Establece la conexion al archivo .db"""
        self.__conn = sqlite3.connect(self.__db_path)
        # Activa las claves foraneas
        self.__conn.execute("PRAGMA foreign_keys = ON")

    # PASO #7 CERRAR CONEXION
    def disconnect(self):
        """Cierra la conexion a la base de datos"""
        if self.__conn:
            self.__conn.close()

    def get_connection(self):
        return self.__conn

    def get_cursor(self):
        return self.__conn.cursor()

    # PASO #3 CREAR LAS TABLAS
    def create_tables(self):
        """Crea las tablas de la base de datos (minimo 2 relacionadas)"""
        cursor = self.get_cursor()

        # Tabla 1: socios (estudiantes y docentes)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS socios(
                cedula TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                tipo TEXT NOT NULL CHECK(tipo IN ('Estudiante', 'Docente')),
                carrera_departamento TEXT,
                semestre INTEGER,
                telefono TEXT
            )
        """)

        # Tabla 2: libros (catalogo)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros(
                isbn TEXT PRIMARY KEY,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                editorial TEXT,
                anio INTEGER,
                ejemplares INTEGER DEFAULT 1,
                disponibles INTEGER DEFAULT 1
            )
        """)

        # Tabla 3: prestamos (relaciona socios y libros - clave foranea)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prestamos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cedula_socio TEXT NOT NULL,
                isbn_libro TEXT NOT NULL,
                fecha_prestamo TEXT NOT NULL,
                fecha_devolucion TEXT,
                FOREIGN KEY(cedula_socio) REFERENCES socios(cedula),
                FOREIGN KEY(isbn_libro) REFERENCES libros(isbn)
            )
        """)

        # Tabla 4: reservas (cola de espera)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reservas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cedula_socio TEXT NOT NULL,
                isbn_libro TEXT NOT NULL,
                fecha_reserva TEXT NOT NULL,
                activa INTEGER DEFAULT 1,
                FOREIGN KEY(cedula_socio) REFERENCES socios(cedula),
                FOREIGN KEY(isbn_libro) REFERENCES libros(isbn)
            )
        """)

        # PASO #5 GUARDAR CAMBIOS
        self.__conn.commit()
