# DECLARATORIA DE USO DE IA E INVESTIGACIÓN

**Proyecto:** Sistema de Gestión de Biblioteca Universitaria
**Asignatura:** Lenguaje de Programación 2
**Grupo #1:** Henry Pazmiño, Jodie Parrales, Cindy Ayoví, Cesar Gonzales, Mayra Alejandra Vera Yagual
**Docente:** Ing. Bryan Vélez M.Sc.

---

## 1. Declaración de uso de inteligencia artificial

Declaramos que el presente proyecto fue desarrollado con el apoyo de **inteligencia artificial generativa** como herramienta de apoyo en:

- Sugerencia de estructura del proyecto y organización de archivos.
- Revisión de sintaxis y depuración de errores.
- Redacción de documentación técnica (este documento y referencias APA).
- Asistencia en la explicación conceptual de algoritmos y estructuras de datos.

**No se utilizó IA para generar código sin comprensión previa.** Cada bloque de código fue revisado, modificado y comprendido por los integrantes del grupo, y se ajustó al estilo de programación enseñado en clase por el Ing. Bryan Vélez.

---

## 2. Contenido enseñado en clase (todo el semestre)

Los siguientes temas fueron enseñados por el Ing. Bryan Vélez durante las clases del semestre y constan en los apuntes y materiales del Grupo #1:

### 2.1 Programación Orientada a Objetos (Semanas 8-11)

| Tema | Cubierto en clase | Material de referencia |
|------|:-----------------:|------------------------|
| Clases y objetos (`class`, `__init__`) | ✅ Enseñado | Apuntes de clase — Semana 8 |
| Herencia simple (`class Hija(Padre)`) | ✅ Enseñado | Clase 4-may — `registro-clases/herencia-simple.md` |
| `super()` para constructor del padre | ✅ Enseñado | Clase 4-may — `registro-clases/metodo-super.md` |
| Herencia múltiple y MRO | ✅ Enseñado | Clase 4-may — `registro-clases/herencia-multiple-mro.md` |
| Sobreescritura de métodos | ✅ Enseñado | Clase 4-may — `registro-clases/sobreescritura-metodos.md` |
| Encapsulamiento (`self.__atributo` + getters) | ✅ Enseñado | Clase 11-may — material de la unidad |
| Abstracción (`ABC` / `@abstractmethod` / `raise NotImplementedError`) | ✅ Enseñado | Clase 11-may — material de la unidad |
| Polimorfismo (mismo método, distinto comportamiento) | ✅ Enseñado | Clase 11-may — `capturas/polimorfismo_ejemplo_11may.md` |

### 2.2 Estructuras de Datos (Semana 10)

| Tema | Cubierto en clase | Material de referencia |
|------|:-----------------:|------------------------|
| Pilas (Stack LIFO) — concepto e implementación | ✅ Enseñado | Clase 1-jun — `capturas/pila-stack-python.md` |
| Colas (Queue FIFO) — concepto e implementación | ✅ Enseñado | Clase 1-jun — `capturas/cola-queue-python.md` |
| Aplicaciones de pilas y colas en la vida real | ✅ Enseñado | Clase 1-jun — `capturas/comparacion-aplicaciones.md` |

### 2.3 Algoritmos de Ordenamiento y Búsqueda (Semana 11)

| Tema | Cubierto en clase | Material de referencia |
|------|:-----------------:|------------------------|
| Bubble Sort — traza manual paso a paso | ✅ Enseñado | Clase 3-jul — `resumen-clase-prog2-semana11.md` |
| Selection Sort | ✅ Enseñado | Exposición Grupo #1 |
| Insertion Sort | ✅ Enseñado | Exposición Grupo #1 |
| Búsqueda lineal | ✅ Enseñado | Taller 11 — `resumen-clase-prog2-semana11.md` |
| Búsqueda binaria | ✅ Enseñado | Taller 11 — `resumen-clase-prog2-semana11.md` |

### 2.4 Base de Datos y Proyecto (Semana 12)

| Tema | Cubierto en clase | Material de referencia |
|------|:-----------------:|------------------------|
| Conexión a SQLite (`import sqlite3`, `sqlite3.connect()`) | ✅ Demostración en vivo | Clase 6-jul — video Semana 12 |
| Creación de tablas (`CREATE TABLE IF NOT EXISTS`) | ✅ Demostración en vivo | Clase 6-jul — video Semana 12 |
| Inserción con parámetros posicionales `(?, ?)` | ✅ Demostración en vivo | Clase 6-jul — video Semana 12 |
| Cursor y ejecución de consultas (`cursor.execute()`) | ✅ Demostración en vivo | Clase 6-jul — video Semana 12 |
| Commit y cierre de conexión (`commit()`, `close()`) | ✅ Demostración en vivo | Clase 6-jul — video Semana 12 |
| SELECT y fetchall (`cursor.fetchall()`) | ✅ Demostración en vivo | Clase 6-jul — video Semana 12 |
| Uso de DB Browser for SQLite | ✅ Demostración en vivo | Clase 6-jul — video Semana 12 |
|| Concepto de Tkinter para GUI e importación (`import tkinter as tk`) | ✅ Demostración en vivo | Clase 10-jul — video Semana 12 (timestamp 54:30) |
|| Modelo de desarrollo incremental (3 incrementos) | ✅ Enseñado | Clase 10-jul — video Semana 12 |

---

## 3. Contenido investigado por el grupo — con referencias APA

A continuación se detalla cada tema que **no fue demostrado explícitamente en clase** pero que fue requerido por el proyecto y por tanto investigado por el grupo.

### 3.1 Lista enlazada simple

**Referencia:**
> Weiss, M. A. (2013). *Estructuras de datos y algoritmos* (4ª ed.). Pearson Educación. ISBN: 978-0-273-76834-2.

**Lo que dice la referencia:** Una lista enlazada es una estructura de datos lineal donde cada elemento (nodo) contiene un valor y una referencia al siguiente nodo. Permite inserciones y eliminaciones eficientes sin reorganizar la memoria, a diferencia de los arreglos estáticos.

**Aplicación en el proyecto:** Se implementó una lista enlazada simple (`LinkedList`) para el catálogo dinámico de libros. Cada nodo almacena un libro y apunta al siguiente, permitiendo agregar y eliminar libros sin límite de tamaño predefinido.

### 3.2 Algoritmos de ordenamiento avanzados (Merge Sort, Quick Sort)

**Referencia:**
> Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to algorithms* (3rd ed.). MIT Press. ISBN: 978-0-262-03384-8.

**Lo que dice la referencia:**
- **Merge Sort (O(n log n)):** Divide la lista en mitades, las ordena recursivamente y las fusiona. Es estable y predecible.
- **Quick Sort (O(n log n) promedio):** Selecciona un pivote y particiona la lista en elementos menores y mayores. Es rápido en la práctica.

**Aplicación en el proyecto:** Se implementaron ambos algoritmos para ordenar el catálogo de libros por título, autor, año, etc. El programa permite al usuario elegir qué algoritmo usar.

*Nota: Los algoritmos básicos (Burbuja, Selección, Inserción) y de búsqueda (lineal, binaria) fueron enseñados en clase durante la Semana 11 y la exposición del Grupo #1.*

### 3.3 Interfaz gráfica con Tkinter

**Referencia:**
> Grayson, J. E. (2000). *Python and Tkinter programming*. Manning Publications. ISBN: 978-1-884777-81-3.

**Lo que dice la referencia:** Tkinter es la biblioteca gráfica estándar de Python. Usa widgets como ventanas, botones, etiquetas, entradas de texto y menús para construir interfaces de usuario. Es multiplataforma y viene incluida con Python sin necesidad de instalación adicional.

**Aplicación en el proyecto:** Se desarrolló la interfaz gráfica del sistema usando Tkinter, con menús desplegables, formularios de entrada, tablas de visualización y cuadros de diálogo.

### 3.4 Operaciones CRUD completas en SQLite (UPDATE, DELETE)

**Referencia:**
> Kreibich, J. A. (2010). *Using SQLite*. O'Reilly Media. ISBN: 978-0-596-52118-9.

**Lo que dice la referencia:** CRUD (Create, Read, Update, Delete) son las cuatro operaciones básicas de persistencia en bases de datos. SQLite es un motor de base de datos embebido que no requiere servidor, ideal para aplicaciones de escritorio.

**Aplicación en el proyecto:** Se implementaron operaciones CRUD completas para las tablas de socios y libros.
*Nota: Las operaciones INSERT y SELECT fueron enseñadas en clase. UPDATE y DELETE fueron investigadas para completar el CRUD.*

---

## 4. Herramientas y tecnologías utilizadas

| Herramienta | Versión | Propósito |
|-------------|---------|-----------|
| Python | 3.11.15 | Lenguaje de programación |
| SQLite3 | 3.x | Motor de base de datos embebido |
| DB Browser for SQLite | 3.x | Administración visual de la BD |
| Tkinter | 8.6 | Interfaz gráfica de usuario |
| Git | 2.47.3 | Control de versiones |
| GitHub | — | Repositorio remoto |
| VS Code / IDLE | — | Entorno de desarrollo |

---

## 5. Nota final

Todo el código presentado fue desarrollado con fines académicos para la asignatura **Lenguaje de Programación 2** de la **Universidad Agraria del Ecuador**, cursando el **Tercer Semestre** de la carrera **Ciencias de la Computación — Modalidad en Línea**.

Las referencias bibliográficas citadas en este documento siguen el **formato APA 7ª edición** y corresponden a fuentes académicas verificables. Los integrantes del grupo declaramos haber comprendido y adaptado cada concepto al contexto del proyecto antes de su implementación.

---
**Fecha:** Julio 2026
**Repositorio:** https://github.com/josuepaz80-usitee/sistema-biblioteca-prog2
