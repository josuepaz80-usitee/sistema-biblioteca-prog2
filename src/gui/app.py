# INTERFAZ GRAFICA CON TKINTER
# Tkinter viene por defecto en Python (no requiere instalacion)
# Investigacion: Grayson, J. E. (2000). Python and Tkinter programming. Manning.

import tkinter as tk
from tkinter import ttk, messagebox


class BibliotecaApp:
    """Aplicacion principal del Sistema de Biblioteca"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestion de Biblioteca Universitaria")
        self.root.geometry("900x600")

        # Color de fondo para distinguir secciones
        self.root.configure(bg="#f0f0f0")

        # Crea la barra de menu
        self._crear_menu()

        # Crea el panel principal
        self._crear_panel_principal()

    def _crear_menu(self):
        """Crea la barra de menu del sistema"""
        menubar = tk.Menu(self.root)

        # Menu Socios
        menu_socios = tk.Menu(menubar, tearoff=0)
        menu_socios.add_command(label="Registrar Socio", command=self.registrar_socio)
        menu_socios.add_command(label="Listar Socios", command=self.listar_socios)
        menubar.add_cascade(label="Socios", menu=menu_socios)

        # Menu Libros
        menu_libros = tk.Menu(menubar, tearoff=0)
        menu_libros.add_command(label="Agregar Libro", command=self.agregar_libro)
        menu_libros.add_command(label="Ver Catalogo", command=self.ver_catalogo)
        menubar.add_cascade(label="Libros", menu=menu_libros)

        # Menu Prestamos
        menu_prestamos = tk.Menu(menubar, tearoff=0)
        menu_prestamos.add_command(label="Realizar Prestamo", command=self.realizar_prestamo)
        menu_prestamos.add_command(label="Registrar Devolucion", command=self.registrar_devolucion)
        menu_prestamos.add_command(label="Ver Prestamos", command=self.ver_prestamos)
        menubar.add_cascade(label="Prestamos", menu=menu_prestamos)

        # Menu Reservas
        menu_reservas = tk.Menu(menubar, tearoff=0)
        menu_reservas.add_command(label="Nueva Reserva", command=self.nueva_reserva)
        menu_reservas.add_command(label="Ver Reservas", command=self.ver_reservas)
        menubar.add_cascade(label="Reservas", menu=menu_reservas)

        self.root.config(menu=menubar)

    def _crear_panel_principal(self):
        """Crea el contenido principal de la ventana"""
        # Frame principal con padding
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        # === SECCION: INFORMACION DEL SISTEMA ===
        # Titulo
        label_titulo = ttk.Label(frame, text="Sistema de Gestion de Biblioteca",
                                  font=("Arial", 18, "bold"))
        label_titulo.pack(pady=10)

        # Subtitulo
        label_sub = ttk.Label(frame, text="Universidad Agraria del Ecuador",
                               font=("Arial", 12))
        label_sub.pack()

        # Grupo
        label_grupo = ttk.Label(frame, text="Grupo #1 - Programacion 2 - 3er Semestre",
                                 font=("Arial", 10))
        label_grupo.pack(pady=5)

        # === SECCION: BOTONES DE ACCESO RAPIDO ===
        panel_botones = ttk.LabelFrame(frame, text="Acceso Rapido", padding=15)
        panel_botones.pack(pady=20, fill=tk.X)

        # Crear una cuadricula de botones
        btn_frame = ttk.Frame(panel_botones)
        btn_frame.pack()

        ttk.Button(btn_frame, text="Registrar Socio",
                   command=self.registrar_socio, width=25).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Agregar Libro",
                   command=self.agregar_libro, width=25).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text="Realizar Prestamo",
                   command=self.realizar_prestamo, width=25).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Registrar Devolucion",
                   command=self.registrar_devolucion, width=25).grid(row=1, column=1, padx=5, pady=5)

    # === FUNCIONALIDADES (stubs listos para implementar) ===
    def registrar_socio(self):
        messagebox.showinfo("Registrar Socio", "Funcionalidad en construccion")

    def listar_socios(self):
        messagebox.showinfo("Listar Socios", "Funcionalidad en construccion")

    def agregar_libro(self):
        messagebox.showinfo("Agregar Libro", "Funcionalidad en construccion")

    def ver_catalogo(self):
        messagebox.showinfo("Catalogo", "Funcionalidad en construccion")

    def realizar_prestamo(self):
        messagebox.showinfo("Prestamo", "Funcionalidad en construccion")

    def registrar_devolucion(self):
        messagebox.showinfo("Devolucion", "Funcionalidad en construccion")

    def ver_prestamos(self):
        messagebox.showinfo("Prestamos", "Funcionalidad en construccion")

    def nueva_reserva(self):
        messagebox.showinfo("Reserva", "Funcionalidad en construccion")

    def ver_reservas(self):
        messagebox.showinfo("Reservas", "Funcionalidad en construccion")

    def run(self):
        """Inicia la aplicacion"""
        self.root.mainloop()
