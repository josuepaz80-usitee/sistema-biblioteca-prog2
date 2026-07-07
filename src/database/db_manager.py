"""Capa de base de datos - SQLite"""
import sqlite3
import os
from datetime import date


class DatabaseManager:
    """Gestiona la conexión y operaciones con SQLite"""

    def __init__(self, db_path: str = "db/biblioteca.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.__db_path = db_path
        self.__conn = None

    def connect(self):
        """Paso 1: Conectar a la base de datos"""
        self.__conn = sqlite3.connect(self.__db_path)
        self.__conn.execute("PRAGMA foreign_keys = ON")
        return self.__conn

    def disconnect(self):
        """Cierra la conexión"""
        if self.__conn:
            self.__conn.close()

    @property
    def connection(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__conn.cursor()

    def create_tables(self):
        """Crea las tablas de la base de datos"""
        cursor = self.cursor

        # Tabla: socios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS socios (
                cedula TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                tipo TEXT NOT NULL CHECK(tipo IN ('Estudiante', 'Docente')),
                carrera_departamento TEXT,
                semestre INTEGER,
                telefono TEXT
            )
        """)

        # Tabla: libros (relacionada con prestamos)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                isbn TEXT PRIMARY KEY,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                editorial TEXT,
                anio INTEGER,
                ejemplares INTEGER DEFAULT 1,
                disponibles INTEGER DEFAULT 1
            )
        """)

        # Tabla: prestamos (relaciona socios y libros)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prestamos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cedula_socio TEXT NOT NULL,
                isbn_libro TEXT NOT NULL,
                fecha_prestamo TEXT NOT NULL,
                fecha_devolucion TEXT,
                FOREIGN KEY (cedula_socio) REFERENCES socios(cedula),
                FOREIGN KEY (isbn_libro) REFERENCES libros(isbn)
            )
        """)

        # Tabla: reservas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reservas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cedula_socio TEXT NOT NULL,
                isbn_libro TEXT NOT NULL,
                fecha_reserva TEXT NOT NULL,
                activa INTEGER DEFAULT 1,
                FOREIGN KEY (cedula_socio) REFERENCES socios(cedula),
                FOREIGN KEY (isbn_libro) REFERENCES libros(isbn)
            )
        """)

        self.__conn.commit()
