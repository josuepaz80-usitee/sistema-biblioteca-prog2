# seed.py — Poblar la base de datos con datos de prueba
# Desarrollado por: Cindy Ayoví (Desarrolladora BD - Grupo #1)

import sqlite3
import os

# PASO #1: CREAR CARPETA db SI NO EXISTE
os.makedirs("db", exist_ok=True)

# PASO #2: CONECTAR BASE DE DATOS (crea biblioteca.db automáticamente)
conexion = sqlite3.connect("db/biblioteca.db")
cursor = conexion.cursor()

# PASO #3: CREAR TABLAS
cursor.execute("""CREATE TABLE IF NOT EXISTS socios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    cedula TEXT UNIQUE NOT NULL,
    tipo TEXT NOT NULL,
    telefono TEXT,
    correo TEXT
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    isbn TEXT UNIQUE NOT NULL,
    editorial TEXT,
    anio INTEGER,
    ejemplares INTEGER DEFAULT 1
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS prestamos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    socio_id INTEGER NOT NULL,
    libro_id INTEGER NOT NULL,
    fecha_prestamo TEXT NOT NULL,
    fecha_devolucion TEXT,
    FOREIGN KEY (socio_id) REFERENCES socios(id),
    FOREIGN KEY (libro_id) REFERENCES libros(id)
)""")

# PASO #4: INSERTAR DATOS DE PRUEBA — SOCIOS
socios = [
    ("Henry Pazmiño", "0956789012", "Estudiante", "0999999999", "henry@email.com"),
    ("Jodie Parrales", "0956789013", "Estudiante", "0999999998", "jodie@email.com"),
    ("Cindy Ayoví", "0956789014", "Estudiante", "0999999997", "cindy@email.com"),
    ("Cesar Gonzales", "0956789015", "Estudiante", "0999999996", "cesar@email.com"),
    ("Mayra Vera", "0956789016", "Estudiante", "0999999995", "mayra@email.com"),
    ("Dr. Miguel Vélez", "0912345678", "Docente", "0999999994", "mvelez@uagraria.edu.ec"),
    ("Ing. Bryan Vélez", "0912345679", "Docente", "0999999993", "bvelez@uagraria.edu.ec"),
]

cursor.executemany(
    "INSERT INTO socios (nombre, cedula, tipo, telefono, correo) VALUES (?, ?, ?, ?, ?)",
    socios
)

# PASO #5: INSERTAR DATOS DE PRUEBA — LIBROS
libros = [
    ("Cien Años de Soledad", "Gabriel García Márquez", "978-0307474728", "Diana", 1967, 3),
    ("El Principito", "Antoine de Saint-Exupéry", "978-0156012195", "Harcourt", 1943, 5),
    ("Don Quijote de la Mancha", "Miguel de Cervantes", "978-8420412146", "Alfaguara", 1605, 2),
    ("Introducción a la Programación con Python", "Luis Joyanes", "978-8415552024", "Marcombo", 2020, 4),
    ("Estructuras de Datos y Algoritmos", "Alfred V. Aho", "978-0201000238", "Pearson", 1983, 2),
    ("Base de Datos SQL", "C. J. Date", "978-8478290855", "Addison-Wesley", 2004, 3),
    ("Redes de Computadoras", "Andrew S. Tanenbaum", "978-6073205337", "Pearson", 2012, 2),
    ("Ingeniería del Software", "Ian Sommerville", "978-6073206037", "Pearson", 2010, 2),
]

cursor.executemany(
    "INSERT INTO libros (titulo, autor, isbn, editorial, anio, ejemplares) VALUES (?, ?, ?, ?, ?, ?)",
    libros
)

# PASO #6: GUARDAR CAMBIOS
conexion.commit()

# PASO #7: VERIFICAR
cursor.execute("SELECT COUNT(*) FROM socios")
total_socios = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM libros")
total_libros = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM prestamos")
total_prestamos = cursor.fetchone()[0]

print(f"=== BASE DE DATOS CREADA ===")
print(f"✓ {total_socios} socios insertados")
print(f"✓ {total_libros} libros insertados")
print(f"✓ {total_prestamos} préstamos registrados")
print(f"\n📁 Archivo: db/biblioteca.db")

# PASO #8: CERRAR CONEXIÓN
conexion.close()
