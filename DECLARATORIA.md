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

## 2. Contenido enseñado en clase (Semana 12)

El docente Ing. Bryan Vélez explicó y demostró en vivo los siguientes temas durante la clase del 6 de julio de 2026:

| Tema | Cubierto en clase |
|------|-------------------|
| Conexión a SQLite (`import sqlite3`, `sqlite3.connect()`) | ✅ Demostración en vivo |
| Creación de tablas (`CREATE TABLE IF NOT EXISTS`) | ✅ Demostración en vivo |
| Inserción de datos con parámetros posicionales `(?, ?)` | ✅ Demostración en vivo |
| Cursor y ejecución de consultas (`cursor.execute()`) | ✅ Demostración en vivo |
| Commit y cierre de conexión (`commit()`, `close()`) | ✅ Demostración en vivo |
| SELECT y fetchall (`cursor.fetchall()`) | ✅ Demostración en vivo |
| Uso de DB Browser for SQLite | ✅ Demostración en vivo |
| Concepto de Tkinter para GUI | ✅ Mencionado (no demostrado) |

---

## 3. Contenido investigado por el grupo — con referencias APA

A continuación se detalla cada tema que **no fue demostrado explícitamente en clase** pero que fue requerido por el proyecto y por tanto investigado por el grupo.

### 3.1 Programación Orientada a Objetos (clases, encapsulamiento, herencia, polimorfismo, abstracción)

**Referencia:**
> Joyanes Aguilar, L. (2020). *Programación orientada a objetos con Python*. McGraw-Hill Interamericana. ISBN: 978-607-15-1548-9.

**Lo que dice la referencia:** La POO se basa en cuatro pilares fundamentales: encapsulamiento (ocultar datos mediante atributos privados y métodos de acceso), herencia (crear clases derivadas que reutilizan código de clases base), polimorfismo (un mismo método se comporta distinto según la clase que lo implementa) y abstracción (definir clases abstractas que no pueden instanciarse directamente).

**Aplicación en el proyecto:** Se diseñó una clase abstracta `Persona` de la cual heredan `Estudiante` y `Docente`. El encapsulamiento se aplicó mediante convención de atributos privados (`__atributo`) con métodos getter/setter. El polimorfismo se aplicó mediante el método `tipo_socio()` que retorna distinto valor según la subclase.

### 3.2 Lista enlazada simple

**Referencia:**
> Weiss, M. A. (2013). *Estructuras de datos y algoritmos* (4ª ed.). Pearson Educación. ISBN: 978-0-273-76834-2.

**Lo que dice la referencia:** Una lista enlazada es una estructura de datos lineal donde cada elemento (nodo) contiene un valor y una referencia al siguiente nodo. Permite inserciones y eliminaciones eficientes sin reorganizar la memoria, a diferencia de los arreglos estáticos.

**Aplicación en el proyecto:** Se implementó una lista enlazada simple (`LinkedList`) para el catálogo dinámico de libros. Cada nodo almacena un libro y apunta al siguiente, permitiendo agregar y eliminar libros sin límite de tamaño predefinido.

### 3.3 Cola (Queue) — estructura FIFO

**Referencia:**
> Cairo, O., & Guardati, S. (2006). *Estructuras de datos* (3ª ed.). McGraw-Hill Interamericana. ISBN: 978-970-10-5856-9.

**Lo que dice la referencia:** Una cola es una estructura FIFO (First In, First Out) donde el primer elemento en entrar es el primero en salir. Se usa para gestionar procesos por orden de llegada.

**Aplicación en el proyecto:** Se implementó una cola (`Queue`) para gestionar las reservas de libros no disponibles. Cuando un libro está prestado, los socios pueden reservarlo y se atienden por orden de llegada.

### 3.4 Pila (Stack) — estructura LIFO

**Referencia:**
> Cairo, O., & Guardati, S. (2006). *Estructuras de datos* (3ª ed.). McGraw-Hill Interamericana. ISBN: 978-970-10-5856-9.

**Lo que dice la referencia:** Una pila es una estructura LIFO (Last In, First Out) donde el último elemento en entrar es el primero en salir. Se usa para deshacer operaciones (undo) y para registros de historial.

**Aplicación en el proyecto:** Se implementó una pila (`Stack`) para almacenar el historial de préstamos/devoluciones y permitir deshacer la última operación registrada por el bibliotecario.

### 3.5 Algoritmos de ordenamiento (Burbuja, Inserción, Merge Sort, Quick Sort)

**Referencia:**
> Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to algorithms* (3rd ed.). MIT Press. ISBN: 978-0-262-03384-8.

**Lo que dice la referencia:**
- **Burbuja (O(n²)):** Recorre la lista comparando pares adyacentes e intercambiándolos si están en orden incorrecto. Es el más simple pero ineficiente para grandes volúmenes.
- **Inserción (O(n²)):** Construye la lista ordenada insertando cada elemento en su posición correcta. Eficiente para listas parcialmente ordenadas.
- **Merge Sort (O(n log n)):** Divide la lista en mitades, las ordena recursivamente y las fusiona. Es estable y predecible.
- **Quick Sort (O(n log n) promedio):** Selecciona un pivote y particiona la lista en elementos menores y mayores. Es rápido en la práctica.

**Aplicación en el proyecto:** Se implementaron estos cuatro algoritmos para ordenar el catálogo de libros por título, autor, año, etc. El programa permite al usuario elegir qué algoritmo usar y visualizar las diferencias.

### 3.6 Búsqueda lineal y búsqueda binaria

**Referencia:**
> Joyanes Aguilar, L. (2020). *Programación orientada a objetos con Python*. McGraw-Hill Interamericana. ISBN: 978-607-15-1548-9.

**Lo que dice la referencia:** La búsqueda lineal recorre elemento por elemento (O(n)). La búsqueda binaria divide el espacio de búsqueda a la mitad en cada paso (O(log n)), pero requiere datos ordenados.

**Aplicación en el proyecto:** Se implementaron ambos algoritmos para buscar libros por ISBN, título o autor. La búsqueda binaria se aplica sobre el catálogo previamente ordenado.

### 3.7 Interfaz gráfica con Tkinter

**Referencia:**
> Grayson, J. E. (2000). *Python and Tkinter programming*. Manning Publications. ISBN: 978-1-884777-81-3.

**Lo que dice la referencia:** Tkinter es la biblioteca gráfica estándar de Python. Usa widgets como ventanas, botones, etiquetas, entradas de texto y menús para construir interfaces de usuario. Es multiplataforma y viene incluida con Python sin necesidad de instalación adicional.

**Aplicación en el proyecto:** Se desarrolló la interfaz gráfica del sistema usando Tkinter, con menús desplegables, formularios de entrada, tablas de visualización y cuadros de diálogo.

### 3.8 Operaciones CRUD en SQLite

**Referencia:**
> Kreibich, J. A. (2010). *Using SQLite*. O'Reilly Media. ISBN: 978-0-596-52118-9.

**Lo que dice la referencia:** CRUD (Create, Read, Update, Delete) son las cuatro operaciones básicas de persistencia en bases de datos. SQLite es un motor de base de datos embebido que no requiere servidor, ideal para aplicaciones de escritorio.

**Aplicación en el proyecto:** Se implementaron operaciones CRUD completas para las tablas de socios y libros, siguiendo exactamente el patrón `INSERT → SELECT → UPDATE → DELETE` que el docente demostró en clase.

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
