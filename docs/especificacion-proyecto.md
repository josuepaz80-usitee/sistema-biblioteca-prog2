# Sistema de Gestión de Biblioteca Universitaria

**Documento de Especificación del Proyecto**

| | |
|---|---|
| **Asignatura** | Lenguaje de Programación 2 |
| **Docente** | Ing. Bryan Vélez M.Sc. |
| **Grupo** | #1 |
| **Semestre** | Tercero — Modalidad en Línea |
| **Universidad** | Universidad Agraria del Ecuador (UAE) |
| **Fecha** | Julio 2026 |

---

## Índice

1. [Introducción](#1-introducción)
2. [Justificación](#2-justificación)
3. [Objetivos](#3-objetivos)
4. [Alcance](#4-alcance)
5. [Marco Teórico](#5-marco-teórico)
6. [Metodología de Desarrollo](#6-metodología-de-desarrollo)
7. [Diseño Preliminar](#7-diseño-preliminar)
8. [Distribución del Trabajo](#8-distribución-del-trabajo)
9. [Repositorio y Control de Versiones](#9-repositorio-y-control-de-versiones)
10. [Plan de Trabajo y Cronograma](#10-plan-de-trabajo-y-cronograma)

---

## 1. Introducción

Las bibliotecas universitarias enfrentan el desafío de gestionar eficientemente sus recursos bibliográficos: registro de socios, control de préstamos, devoluciones y reservas. Actualmente, muchas bibliotecas pequeñas y medianas aún utilizan métodos manuales o sistemas genéricos que no se adaptan a sus necesidades específicas.

El presente proyecto tiene como objetivo desarrollar un **Sistema de Gestión de Biblioteca Universitaria** que automatice los procesos diarios de una biblioteca física. El sistema permitirá registrar socios (estudiantes y docentes), administrar el catálogo de libros, controlar préstamos y devoluciones, y gestionar reservas de ejemplares no disponibles.

El sistema se desarrolla como proyecto final de la asignatura **Lenguaje de Programación 2**, aplicando los conceptos de Programación Orientada a Objetos, estructuras de datos, algoritmos de ordenamiento y búsqueda, bases de datos SQLite e interfaz gráfica con Tkinter, todos enseñados durante el semestre por el Ing. Bryan Vélez.

---

## 2. Justificación

La Universidad Agraria del Ecuador, en su modalidad en línea, requiere que los estudiantes demuestren competencias en el desarrollo de software aplicando los principios de la programación estructurada y orientada a objetos. Este proyecto integra los conocimientos adquiridos durante el semestre en un producto funcional.

La automatización de una biblioteca universitaria permite:

- **Reducir errores humanos** en el registro manual de préstamos y devoluciones
- **Agilizar la búsqueda** de libros en el catálogo
- **Mantener un control preciso** de los ejemplares disponibles
- **Mejorar la experiencia** del usuario (socios y bibliotecarios)

Además, el proyecto permite aplicar conceptos fundamentales de la ingeniería de software como el modelo incremental, el control de versiones con Git/GitHub, y el uso de documentación técnica.

---

## 3. Objetivos

### 3.1 Objetivo General

Desarrollar un sistema de escritorio para la gestión de una biblioteca universitaria que permita administrar socios, libros, préstamos y reservas, aplicando los principios de la Programación Orientada a Objetos, estructuras de datos, algoritmos de búsqueda y ordenamiento, y persistencia en base de datos SQLite.

### 3.2 Objetivos Específicos

1. Implementar un modelo de clases utilizando herencia, encapsulamiento, polimorfismo y abstracción para representar los actores del sistema (Persona → Estudiante/Docente, Libro, Préstamo, Reserva).
2. Utilizar estructuras de datos lineales (lista enlazada, cola FIFO, pila LIFO) para la gestión dinámica de la información en memoria.
3. Implementar algoritmos de ordenamiento (burbuja, inserción, merge sort, quick sort) y búsqueda (lineal, binaria) para la manipulación del catálogo.
4. Persistir los datos en una base de datos SQLite con operaciones CRUD completas y claves foráneas.
5. Desarrollar una interfaz gráfica de usuario (GUI) utilizando Tkinter para la interacción con el sistema.

---

## 4. Alcance

### 4.1 Funcionalidades incluidas

- **Gestión de Socios**: registro, consulta y actualización de datos de estudiantes y docentes
- **Gestión de Libros**: alta, consulta y eliminación de libros en el catálogo
- **Préstamos**: realización de préstamos y registro de devoluciones
- **Reservas**: creación de reservas para libros no disponibles (cola de espera FIFO)
- **Búsqueda**: búsqueda de libros por título, autor, y aplicación de búsqueda binaria
- **Ordenamiento**: ordenamiento del catálogo por diferentes criterios usando múltiples algoritmos

### 4.2 Funcionalidades excluidas

- No incluye módulo de multas o sanciones
- No incluye generación de reportes estadísticos avanzados
- No incluye integración con sistemas externos (API web, RFID, etc.)

### 4.3 Usuarios del sistema

- **Bibliotecario**: usuario principal que opera el sistema para todas las funcionalidades
- **Socio**: estudiante o docente cuyos datos son gestionados en el sistema

---

## 5. Marco Teórico

### 5.1 Programación Orientada a Objetos (POO)

La POO es un paradigma de programación que organiza el código en clases y objetos. Los cuatro pilares fundamentales son:

- **Encapsulamiento**: ocultación de datos mediante atributos privados (`self.__atributo`) y acceso controlado por getters/setters. En el sistema, todos los atributos de las clases del modelo son privados.
- **Herencia**: una clase puede heredar atributos y métodos de otra clase padre. `Estudiante` y `Docente` heredan de `Persona`.
- **Polimorfismo**: el mismo método puede comportarse de manera diferente según la clase que lo implementa. `tipo_socio()` retorna `"Estudiante"` o `"Docente"` según la subclase.
- **Abstracción**: se definen interfaces o métodos abstractos que las subclases deben implementar. `Persona.tipo_socio()` lanza `NotImplementedError` como contrato.

**Referencia:** Joyanes Aguilar, L. (2020). *Programación orientada a objetos con Python*. McGraw-Hill Interamericana.

### 5.2 Estructuras de Datos

#### 5.2.1 Lista Enlazada Simple

Estructura lineal donde cada elemento (nodo) contiene un valor y un puntero al siguiente nodo. Permite inserciones y eliminaciones sin reorganizar memoria. Se implementó `LinkedList` como base para la cola y la pila.

**Referencia:** Weiss, M. A. (2013). *Estructuras de datos y algoritmos* (4ª ed.). Pearson Educación.

#### 5.2.2 Cola (Queue — FIFO)

El primer elemento en entrar es el primero en salir (First In, First Out). Se utiliza para gestionar las reservas de libros en orden de llegada.

#### 5.2.3 Pila (Stack — LIFO)

El último elemento en entrar es el primero en salir (Last In, First Out). Se utiliza para deshacer operaciones (undo) de préstamos y devoluciones.

**Referencia:** Cairo, O., & Guardati, S. (2006). *Estructuras de datos* (3ª ed.). McGraw-Hill.

### 5.3 Algoritmos de Ordenamiento y Búsqueda

#### 5.3.1 Algoritmos de Ordenamiento

| Algoritmo | Complejidad | Descripción |
|-----------|:-----------:|-------------|
| Bubble Sort | O(n²) | Compara pares adyacentes y los intercambia si están en orden incorrecto |
| Insertion Sort | O(n²) | Inserta cada elemento en su posición correcta dentro de la parte ordenada |
| Merge Sort | O(n log n) | Divide la lista en mitades, las ordena recursivamente y las fusiona |
| Quick Sort | O(n log n) promedio | Selecciona un pivote y particiona en menores y mayores |

#### 5.3.2 Algoritmos de Búsqueda

| Algoritmo | Complejidad | Requisito |
|-----------|:-----------:|-----------|
| Búsqueda Lineal | O(n) | Ninguno |
| Búsqueda Binaria | O(log n) | Lista ordenada previamente |

**Referencia:** Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to algorithms* (3rd ed.). MIT Press.

### 5.4 Base de Datos SQLite

SQLite es un motor de base de datos embebido que no requiere servidor, ideal para aplicaciones de escritorio. El sistema utiliza:

- `sqlite3.connect()` para establecer conexión
- `cursor.execute()` con parámetros posicionales `(?, ?)` para consultas seguras
- `PRAGMA foreign_keys = ON` para activar claves foráneas
- Tablas relacionadas: `socios`, `libros`, `prestamos` (FK a socio y libro), `reservas` (FK a socio y libro)

**Referencia:** Kreibich, J. A. (2010). *Using SQLite*. O'Reilly Media.

### 5.5 Interfaz Gráfica con Tkinter

Tkinter es la biblioteca gráfica estándar de Python, incluida por defecto sin necesidad de instalación adicional. Se utiliza para construir la ventana principal, menús desplegables, formularios y cuadros de diálogo.

**Referencia:** Grayson, J. E. (2000). *Python and Tkinter programming*. Manning Publications.

---

## 6. Metodología de Desarrollo

Se utiliza el **Modelo Incremental**, que consiste en desarrollar el sistema por etapas o incrementos, donde cada incremento agrega funcionalidad completa al producto. Este modelo permite:

- Entregar versiones funcionales tempranas
- Obtener retroalimentación continua
- Reducir riesgos de integración
- Adaptarse a cambios durante el desarrollo

### 6.1 Incrementos del Proyecto

| Incremento | Semana | Entregable | Estado |
|:-----------:|:------:|------------|:------:|
| **Incremento 1** | Semana 12 (7-10 jul) | Modelo de clases POO + Estructuras de datos + Algoritmos + Esquema BD + GUI (stubs) + Documento de Especificación (50%) | ✅ Completado |
| **Incremento 2** | Semana 13 (13-17 jul) | GUI funcional completa + BD poblada + CRUD completo + Pruebas unitarias + Manual de Usuario | ⏳ Pendiente |
| **Incremento 3** | Semana 14 (20 jul) | Integración final + Pruebas de sistema + Documento completo (100%) + Defensa oral | ⏳ Pendiente |

### 6.2 Flujo de trabajo

1. **Planificación del incremento**: se definen las funcionalidades a implementar
2. **Diseño**: se actualizan los diagramas si es necesario
3. **Implementación**: cada miembro desarrolla su módulo asignado
4. **Pruebas**: se ejecutan pruebas unitarias y de integración
5. **Revisión**: el líder (Henry) revisa e integra los cambios
6. **Entrega**: se sube a GitHub y se documenta el avance

### 6.3 Herramientas de desarrollo

| Herramienta | Versión | Propósito |
|-------------|:-------:|-----------|
| Python | 3.11+ | Lenguaje de programación |
| Visual Studio Code | Última | Editor de código con extensión Python (Microsoft) y GitLens |
| Tkinter | 8.6 | Biblioteca de interfaz gráfica (incluida en Python) |
| SQLite3 | 3.x | Motor de base de datos embebido |
| DB Browser for SQLite | 3.x | Administración visual de la BD |
| Git | 2.47+ | Control de versiones |
| GitHub | — | Repositorio remoto |

---

## 7. Diseño Preliminar

### 7.1 Diagrama de Clases (UML)

```
┌────────────────────────────────────────┐
│              Persona                    │ ◄── Abstracción
│  - __cedula: str                       │     (raise NotImplementedError)
│  - __nombre: str                       │
│  - __apellido: str                     │
│  - __telefono: str                     │
├────────────────────────────────────────┤
│  + get_cedula(): str                   │
│  + get_nombre_completo(): str          │
│  + tipo_socio(): str                   │ ◄── Polimorfismo
└────────────┬───────────────────────────┘
             │  Herencia
    ┌────────┴────────┐
    ▼                 ▼
┌─────────────┐ ┌─────────────┐
│  Estudiante │ │   Docente   │
├─────────────┤ ├─────────────┤
│ - __carrera │ │ - __depto   │
│ - __semestre│ │             │
├─────────────┤ ├─────────────┤
│ + tipo_socio│ │ + tipo_socio│
│ = Estudiante│ │ = Docente   │
└─────────────┘ └─────────────┘
        │                │
        └───────┬────────┘
                ▼
        ┌──────────────┐
        │    Socio     │ ◄── Wrapper polimórfico
        │ - __persona  │      contiene Estudiante o Docente
        └──────────────┘

┌──────────────────┐      ┌──────────────────┐
│      Libro       │      │    Prestamo      │
├──────────────────┤      ├──────────────────┤
│ - __isbn         │      │ - __socio        │──► Socio
│ - __titulo       │      │ - __libro        │──► Libro
│ - __autor        │      │ - __fecha_prest  │
│ - __ejemplares   │      │ - __fecha_dev    │
│ - __disponibles  │      └──────────────────┘
├──────────────────┤
│ + prestar()      │      ┌──────────────────┐
│ + devolver()     │      │    Reserva       │
│ + esta_disp()    │      ├──────────────────┤
└──────────────────┘      │ - __socio        │──► Socio
                          │ - __libro        │──► Libro
                          │ - __fecha        │
                          │ - __activa       │
                          └──────────────────┘

Estructuras de Datos:
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ LinkedList   │  │    Queue     │  │    Stack     │
│ (Nodo → Nodo)│  │  (FIFO)     │  │  (LIFO)      │
│ append()     │  │ enqueue()   │  │ push()       │
│ prepend()    │  │ dequeue()   │  │ pop()        │
│ remove()     │  │ peek()      │  │ peek()       │
│ find()       │  │             │  │              │
└──────────────┘  └──────────────┘  └──────────────┘

Algoritmos:
┌──────────────────┐  ┌──────────────────────┐
│    Búsqueda      │  │   Ordenamiento       │
│ Lineal (O(n))    │  │ Bubble (O(n²))       │
│ Binaria (O(log n))│  │ Insertion (O(n²))   │
└──────────────────┘  │ Merge (O(n log n))   │
                      │ Quick (O(n log n))   │
                      └──────────────────────┘
```

### 7.2 Modelo Entidad-Relación (Base de Datos)

```
┌────────────────────┐       ┌────────────────────────┐
│      socios        │       │       libros           │
├────────────────────┤       ├────────────────────────┤
│ PK  cedula: TEXT   │       │ PK  isbn: TEXT         │
│     nombre: TEXT   │       │     titulo: TEXT       │
│     apellido: TEXT │       │     autor: TEXT        │
│     tipo: TEXT     │       │     editorial: TEXT    │
│     carrera: TEXT  │       │     anio: INTEGER      │
│     semestre: INT  │       │     ejemplares: INT    │
│     telefono: TEXT │       │     disponibles: INT   │
└────────┬───────────┘       └──────────┬─────────────┘
         │                              │
         │  ┌───────────────────────────┘
         │  │
         ▼  ▼
┌────────────────────┐       ┌────────────────────────┐
│     prestamos      │       │       reservas          │
├────────────────────┤       ├────────────────────────┤
│ PK  id: INTEGER    │       │ PK  id: INTEGER        │
│ FK  cedula_socio   │──►    │ FK  cedula_socio       │──► socios
│ FK  isbn_libro     │──►    │ FK  isbn_libro         │──► libros
│     fecha_prestamo │       │     fecha_reserva      │
│     fecha_devuelto │       │     activa: INTEGER    │
└────────────────────┘       └────────────────────────┘
```

---

## 8. Distribución del Trabajo

### 8.1 Roles del equipo

| Integrante | Rol | Módulo | Archivos |
|------------|-----|--------|----------|
| **Henry Pazmiño** | Líder / Integrador | Modelos POO + Integración | `main.py`, `src/models/*`, coordinación general |
| **Jodie Parrales** | Desarrolladora GUI | Interfaz gráfica Tkinter | `src/gui/app.py` |
| **Cindy Ayoví** | Desarrolladora BD | Base de datos SQLite | `src/database/*` |
| **Cesar Gonzales** | Desarrollador Lógica | Algoritmos + Estructuras | `src/algorithms/*`, `src/data_structures/*` |
| **Mayra Vera** | Documentación y Pruebas | Pruebas + Documentación | `tests/*`, `docs/*` |

### 8.2 Distribución por módulo

| Módulo | Desarrollador | Tareas específicas |
|--------|---------------|-------------------|
| Modelos POO | Henry Pazmiño | Clases Persona, Estudiante, Docente, Libro, Socio, Prestamo, Reserva. Encapsulamiento, herencia, polimorfismo, abstracción |
| GUI Tkinter | Jodie Parrales | Ventana principal, menús, formularios, tablas, cuadros de diálogo. Integración con los repositorios de datos |
| Base de Datos | Cindy Ayoví | Conexión SQLite, creación de tablas, CRUD completo para socios y libros, consultas con joins, **seed.py con datos de prueba (7 socios + 8 libros)** |
| Algoritmos y Estructuras | Cesar Gonzales | Merge Sort, Quick Sort, Bubble Sort, Insertion Sort, búsqueda lineal y binaria, lista enlazada, cola FIFO, pila LIFO |
| Pruebas y Documentación | Mayra Vera | Pruebas unitarias, manual de usuario, validación de funcionalidades, casos de prueba |

---

## 9. Repositorio y Control de Versiones

### 9.1 Repositorio

El proyecto se aloja en GitHub bajo el control de versiones Git.

- **URL:** [https://github.com/josuepaz80-usitee/sistema-biblioteca-prog2](https://github.com/josuepaz80-usitee/sistema-biblioteca-prog2)
- **Rama principal:** `main`
- **Flujo:** commits directos a `main` con mensajes descriptivos

### 9.2 Historial de Commits

| # | Fecha | Hash | Mensaje |
|:-:|:-----:|:----:|---------|
| 1 | 7 jul | `0e78b3a` | `Initial commit` |
| 2 | 7 jul | `b31c6bd` | `feat: estructura inicial del Sistema de Gestion de Biblioteca Universitaria` |
| 3 | 8 jul | `eaf6cae` | `refactor: estilo nivel 3er semestre segun lo ensenado por Ing. Bryan Velez + DECLARATORIA` |
| 4 | 9 jul | `7f9e535` | `fix: DECLARATORIA actualizada tras revision completa del material del semestre` |
| 5 | 9 jul | `d388507` | `fix: referencias genericas sin nombres individuales en DECLARATORIA` |
|| 6 | 11 jul | `ac193dd` | `docs: agregar documentacion del proyecto (especificacion, manual, Gantt, README con roles)` |
|| 7 | 11 jul | `6cf6167` | `docs: especificacion visible en markdown + creditos de autoría por integrante en cada archivo` |
|| 8 | 11 jul | `2d1e028` | `fix: formato limpio del credito de Mayra en manual-usuario.md` |
|| 9 | 11 jul | `e8ce1b1` | `fix: actualizar historial de commits y DECLARATORIA (Tkinter + incremental)` |
|| 10 | 11 jul | `165d556` | `docs: restaurar formato original con logo UAE + commits hasta #10` |
|| 11 | 11 jul | `8b01d20` | `docs: sincronizar historial de commits en markdown hasta #10` |
|| 12 | 11 jul | `ee37e02` | `feat: seed de base de datos con datos de prueba (Cindy Ayoví - BD)` |

### 9.3 Stack Tecnológico del Desarrollo

- **Editor:** VS Code con extensión Python (Microsoft)
- **Control de versiones:** Git + GitLens
- **Lenguaje:** Python 3.11+
- **GUI:** Tkinter (libería estándar)
- **BD:** SQLite3
- **Documentación:** Markdown + DOCX + PDF

---

## 10. Plan de Trabajo y Cronograma

### 10.1 Diagrama de Gantt

```
Julio 2026
───────────────────────────────────────────────────────
Actividad              | Lun 7 | Sem 12 | Sem 13 | Sem 14
                       | a jue 10| 10 jul| 13-17  | 20 jul
───────────────────────────────────────────────────────
Inicio del proyecto    | ████  |        |        |
(planificación, repo)  |       |        |        |
                       |       |        |        |
Modelos POO            |  ████ |        |        |
(clases, herencia,     |       |        |        |
encapsulamiento)       |       |        |        |
                       |       |        |        |
Estructuras de datos   |   ████|        |        |
(lista, cola, pila)    |       |        |        |
                       |       |        |        |
Algoritmos             |    ███|        |        |
(búsqueda, ordenamiento)|       |       |        |
                       |       |        |        |
Base de datos SQLite   |     ██|        |        |
(tablas, CRUD)         |       |        |        |
                       |       |        |        |
GUI Tkinter (stubs)    |      █|        |        |
                       |       |        |        |
Documento Especificación|      █|   █    |        |
(50%)                  |       |        |        |
                       |       |        |        |
─── ENTREGA TAREA 12 ──|       |   ●    |        |
                       |       | 11 jul |        |
                       |       |        |        |
GUI funcional completa |       |        | ██████ |
(formularios CRUD)     |       |        |        |
                       |       |        |        |
BD poblada + reports   |       |        |  ████  |
(socios, libros)       |       |        |        |
                       |       |        |        |
Pruebas unitarias      |       |        |   ███  |
                       |       |        |        |
Manual de usuario      |       |        |    ██  |
(capturas de pantalla) |       |        |        |
                       |       |        |        |
─── ENTREGA FINAL ──── |       |        |        |   ●
                       |       |        |        | 20 jul
                       |       |        |        |
Defensa oral           |       |        |        |   ●
(Semana 15)            |       |        |        | 27 jul
───────────────────────────────────────────────────────
```

### 10.2 Prioridades para la Semana 13 (13-17 julio)

| Prioridad | Tarea | Responsable |
|:---------:|-------|-------------|
| 🔴 Alta | Implementar formularios CRUD en GUI (Registrar Socio, Agregar Libro) | Jodie Parrales |
| ✅ Completado | Poblar la base de datos con datos de prueba (seed.py — 7 socios + 8 libros) | Cindy Ayoví |
| 🟡 Media | Completar lógica de préstamos y devoluciones en GUI | Jodie + Cesar |
| 🟡 Media | Pruebas de integración módulo BD + GUI | Mayra Vera |
| 🟢 Baja | Manual de usuario con capturas de pantalla | Mayra Vera |

---

> **Documento de Especificación — Avance 50%**
> *Grupo #1 — Lenguaje de Programación 2 — UAE*
> *Última actualización: 11 de julio de 2026*
