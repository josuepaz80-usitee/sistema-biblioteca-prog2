# Sistema de Gestión de Biblioteca Universitaria

**Proyecto Final — Lenguaje de Programación 2**
**Universidad Agraria del Ecuador**
**Grupo #1**

## Descripción

Sistema para automatizar el control de una biblioteca física universitaria. Gestiona:
- Registro de socios (estudiantes y docentes)
- Catálogo de libros
- Préstamos y devoluciones
- Reservas de ejemplares prestados

## Requisitos Técnicos

- Programación Orientada a Objetos (3+ clases, encapsulamiento, herencia, polimorfismo)
- Estructuras de datos: lista enlazada, cola, pila
- Algoritmos de ordenamiento (burbuja/inserción + merge/quick sort)
- Búsqueda lineal y binaria
- Base de datos SQLite con operaciones CRUD
- Interfaz gráfica con Tkinter

## Documentación

| Documento | Enlace |
|-----------|--------|
| Especificación del Proyecto (visible en GitHub) | [`docs/especificacion-proyecto.md`](docs/especificacion-proyecto.md) |
| Especificación del Proyecto (DOCX para entrega) | [`docs/especificacion-proyecto.docx`](docs/especificacion-proyecto.docx) |
| Manual de Usuario (borrador) | [`docs/manual-usuario.md`](docs/manual-usuario.md) |
| Diagrama de Gantt | [`docs/gantt.png`](docs/gantt.png) |
| Declaratoria de uso de IA | [`DECLARATORIA.md`](DECLARATORIA.md) |

## Miembros del Grupo #1 — Roles

| Integrante | Rol |
|------------|-----|
| Henry Pazmiño | Líder / Integrador |
| Jodie Parrales | Desarrolladora GUI (Tkinter) |
| Cindy Ayoví | Desarrolladora BD (SQLite) — seed.py, CRUD socios/libros |
| Cesar Gonzales | Desarrollador Lógica/Negocio |
| Mayra Vera | Documentación y Pruebas |

## Estructura del Proyecto

```
sistema-biblioteca-prog2/
├── src/                    # Código fuente
│   ├── models/            # Clases del dominio (POO)
│   ├── data_structures/   # Lista, cola, pila
│   ├── algorithms/        # Ordenamiento y búsqueda
│   ├── database/          # Conexión y operaciones BD
│   └── gui/               # Interfaz gráfica Tkinter
├── docs/                  # Documentación del proyecto
├── db/                    # Base de datos SQLite
├── tests/                 # Pruebas unitarias
└── main.py                # Punto de entrada
```

## Documentación Académica

📄 **`DECLARATORIA.md`** — Documento obligatorio que declara:
- Uso de IA como herramienta de apoyo
- Contenido enseñado en clase vs. contenido investigado
- Referencias APA 7ª edición para cada tema investigado

> ⚠️ **Nota:** Todo el código sigue el estilo enseñado por el Ing. Bryan Vélez: comentarios `# PASO #N`, encapsulamiento con getters/setters, herencia simple, polimorfismo, y estructura paso a paso. Los temas no cubiertos en clase están señalados en la DECLARATORIA con sus referencias APA.
