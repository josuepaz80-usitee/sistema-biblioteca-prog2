# ============================================================
# Cindy Ayovi — Poblar la base de datos con datos de prueba
# seed.py ejecutable desde la raiz del proyecto
# Crea db/biblioteca.db con el mismo esquema de db_manager.py
# ============================================================

# PASO #1 IMPORTAR LIBRERIAS
import sqlite3
import os

# PASO #2 CREAR CARPETA db SI NO EXISTE
os.makedirs("db", exist_ok=True)

# PASO #3 CONECTAR BASE DE DATOS (crea biblioteca.db automaticamente)
conexion = sqlite3.connect("db/biblioteca.db")
cursor = conexion.cursor()

# Activa las claves foraneas (importante para integridad referencial)
cursor.execute("PRAGMA foreign_keys = ON")

# PASO #4 CREAR TABLA SOCIOS
# Cedula es TEXT porque puede tener ceros a la izquierda y no se opera
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

# PASO #5 CREAR TABLA LIBROS
# ISBN como TEXT porque no se realizan operaciones matematicas
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

# PASO #6 CREAR TABLA PRESTAMOS (relaciona socios con libros)
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

# PASO #7 CREAR TABLA RESERVAS (cola de espera)
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

# PASO #8 INSERTAR DATOS DE PRUEBA — SOCIOS
# 5 estudiantes (integrantes) + 2 docentes
socios = [
    ("0956789012", "Henry", "Pazmino", "Estudiante", "Computacion", 3, "0999999999"),
    ("0956789013", "Jodie", "Parrales", "Estudiante", "Computacion", 3, "0999999998"),
    ("0956789014", "Cindy", "Ayovi", "Estudiante", "Computacion", 3, "0999999997"),
    ("0956789015", "Cesar", "Gonzales", "Estudiante", "Computacion", 3, "0999999996"),
    ("0956789016", "Mayra", "Vera", "Estudiante", "Computacion", 3, "0999999995"),
    ("0912345678", "Miguel", "Velez", "Docente", "Sistemas", None, "0999999994"),
    ("0912345679", "Bryan", "Velez", "Docente", "Computacion", None, "0999999993"),
]

cursor.executemany(
    "INSERT INTO socios(cedula, nombre, apellido, tipo, carrera_departamento, semestre, telefono) "
    "VALUES(?, ?, ?, ?, ?, ?, ?)",
    socios
)

# PASO #9 INSERTAR DATOS DE PRUEBA — LIBROS
libros = [
    ("978-0307474728", "Cien Anios de Soledad", "Gabriel Garcia Marquez", "Diana", 1967, 3, 3),
    ("978-0156012195", "El Principito", "Antoine de Saint-Exupery", "Harcourt", 1943, 5, 5),
    ("978-8420412146", "Don Quijote de la Mancha", "Miguel de Cervantes", "Alfaguara", 1605, 2, 2),
    ("978-8415552024", "Introduccion a la Programacion con Python", "Luis Joyanes", "Marcombo", 2020, 4, 4),
    ("978-0201000238", "Estructuras de Datos y Algoritmos", "Alfred V. Aho", "Pearson", 1983, 2, 2),
    ("978-8478290855", "Base de Datos SQL", "C. J. Date", "Addison-Wesley", 2004, 3, 3),
    ("978-6073205337", "Redes de Computadoras", "Andrew S. Tanenbaum", "Pearson", 2012, 2, 2),
    ("978-6073206037", "Ingenieria del Software", "Ian Sommerville", "Pearson", 2010, 2, 2),
]

cursor.executemany(
    "INSERT INTO libros(isbn, titulo, autor, editorial, anio, ejemplares, disponibles) "
    "VALUES(?, ?, ?, ?, ?, ?, ?)",
    libros
)

# PASO #10 GUARDAR CAMBIOS (COMMIT)
conexion.commit()

# PASO #11 VERIFICAR DATOS INSERTADOS
cursor.execute("SELECT COUNT(*) FROM socios")
total_socios = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM libros")
total_libros = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM prestamos")
total_prestamos = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM reservas")
total_reservas = cursor.fetchone()[0]

print("=== BASE DE DATOS CREADA ===")
print(f"✓ {total_socios} socios insertados")
print(f"✓ {total_libros} libros insertados")
print(f"✓ {total_prestamos} prestamos registrados")
print(f"✓ {total_reservas} reservas registradas")
print(f"\n📁 Archivo: db/biblioteca.db")
print(f"📋 Esquema compatible con db_manager.py (Cindy Ayovi)")

# PASO #12 CERRAR CONEXION
conexion.close()
