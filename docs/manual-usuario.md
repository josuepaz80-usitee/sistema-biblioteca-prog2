# Manual de Usuario — Sistema de Gestión de Biblioteca Universitaria

**Grupo #1 — Lenguaje de Programación 2**
**Versión:** 1.0 — Borrador inicial
**Última actualización:** Julio 2026

---

> ⚠️ **Documento en construcción.** Este manual se completará en la Semana 14 junto con la entrega final del proyecto.

## 1. Introducción

El Sistema de Gestión de Biblioteca Universitaria es una aplicación de escritorio desarrollada en Python que permite administrar los recursos bibliográficos de una biblioteca física universitaria. El sistema facilita el registro de socios, la gestión del catálogo de libros, el control de préstamos y devoluciones, y la administración de reservas.

## 2. Requisitos del Sistema

### 2.1 Hardware
- Computadora con sistema operativo Windows 10/11, Linux o macOS
- Resolución de pantalla mínima: 1024x768
- Espacio en disco: 50 MB

### 2.2 Software
- Python 3.11 o superior
- SQLite (incluido en Python por defecto)
- Tkinter (incluido en Python por defecto)
- DB Browser for SQLite (opcional, para administración visual de la BD)

## 3. Instalación

*(Pendiente — se completará con capturas de pantalla en la Semana 14)*

Pasos generales:
1. Clonar el repositorio o descargar los archivos del proyecto
2. Ejecutar `main.py` desde la terminal:
   ```
   python main.py
   ```
3. El sistema creará automáticamente la base de datos en `db/biblioteca.db`

## 4. Guía de Uso

### 4.1 Pantalla Principal
Al iniciar el sistema, se muestra la ventana principal con un menú superior que contiene las siguientes secciones:
- **Socios**: registro y consulta de socios
- **Libros**: gestión del catálogo bibliográfico
- **Préstamos**: control de préstamos y devoluciones
- **Reservas**: administración de reservas

### 4.2 Gestión de Socios
- **Registrar Socio**: ingresar datos del nuevo socio (cédula, nombres, tipo: Estudiante/Docente, carrera/departamento, semestre, teléfono)
- **Listar Socios**: visualizar todos los socios registrados en el sistema

### 4.3 Gestión de Libros
- **Agregar Libro**: registrar un nuevo ejemplar en el catálogo
- **Ver Catálogo**: consultar todos los libros disponibles, ordenados por diferentes criterios

### 4.4 Préstamos y Devoluciones
- **Realizar Préstamo**: seleccionar un socio y un libro para realizar el préstamo
- **Registrar Devolución**: registrar la devolución de un libro prestado
- **Ver Préstamos**: consultar el historial de préstamos activos

### 4.5 Reservas
- **Nueva Reserva**: solicitar una reserva cuando un libro no está disponible
- **Ver Reservas**: consultar la cola de espera de reservas

## 5. Estructura de la Base de Datos

El sistema utiliza SQLite con las siguientes tablas:

- **socios**: id, cedula, nombre, apellido, tipo, carrera_departamento, semestre, telefono
- **libros**: id, titulo, autor, isbn, anio, categoria, ejemplares, disponibles
- **prestamos**: id, socio_id (FK), libro_id (FK), fecha_prestamo, fecha_devolucion, estado
- **reservas**: id, socio_id (FK), libro_id (FK), fecha_reserva, posicion

## 6. Solución de Problemas

*(Pendiente — se completará en la Semana 14)*

---
*Documento en construcción — Versión borrador 0.1*
