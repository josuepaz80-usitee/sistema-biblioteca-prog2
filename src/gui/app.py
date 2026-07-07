"""Interfaz gráfica con Tkinter"""
import tkinter as tk
from tkinter import ttk, messagebox


class BibliotecaApp:
    """Aplicación principal de la Biblioteca"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión de Biblioteca Universitaria")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f0f0")

        # Configurar estilos
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self._crear_menu()
        self._crear_contenido()

    def _crear_menu(self):
        """Crea la barra de menú"""
        menubar = tk.Menu(self.root)

        # Menú Socios
        menu_socios = tk.Menu(menubar, tearoff=0)
        menu_socios.add_command(label="Registrar Socio", command=self.registrar_socio)
        menu_socios.add_command(label="Listar Socios", command=self.listar_socios)
        menubar.add_cascade(label="Socios", menu=menu_socios)

        # Menú Libros
        menu_libros = tk.Menu(menubar, tearoff=0)
        menu_libros.add_command(label="Agregar Libro", command=self.agregar_libro)
        menu_libros.add_command(label="Catálogo", command=self.catalogo_libros)
        menubar.add_cascade(label="Libros", menu=menu_libros)

        # Menú Préstamos
        menu_prestamos = tk.Menu(menubar, tearoff=0)
        menu_prestamos.add_command(label="Realizar Préstamo", command=self.realizar_prestamo)
        menu_prestamos.add_command(label="Registrar Devolución", command=self.registrar_devolucion)
        menu_prestamos.add_command(label="Listar Préstamos", command=self.listar_prestamos)
        menubar.add_cascade(label="Préstamos", menu=menu_prestamos)

        # Menú Reservas
        menu_reservas = tk.Menu(menubar, tearoff=0)
        menu_reservas.add_command(label="Nueva Reserva", command=self.nueva_reserva)
        menu_reservas.add_command(label="Ver Reservas", command=self.ver_reservas)
        menubar.add_cascade(label="Reservas", menu=menu_reservas)

        # Menú Ayuda
        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.acerca_de)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.root.config(menu=menubar)

    def _crear_contenido(self):
        """Crea el contenido principal"""
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Sistema de Gestión de Biblioteca",
                  font=("Arial", 18, "bold")).pack(pady=10)
        ttk.Label(frame, text="Universidad Agraria del Ecuador",
                  font=("Arial", 12)).pack()
        ttk.Label(frame, text="Grupo #1 - Programación 2",
                  font=("Arial", 10)).pack(pady=5)

        # Panel de acceso rápido
        panel = ttk.LabelFrame(frame, text="Acceso Rápido", padding=15)
        panel.pack(pady=20, fill=tk.X)

        btn_frame = ttk.Frame(panel)
        btn_frame.pack()

        ttk.Button(btn_frame, text="📚 Registrar Socio",
                   command=self.registrar_socio, width=25).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="📖 Agregar Libro",
                   command=self.agregar_libro, width=25).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text="🔄 Realizar Préstamo",
                   command=self.realizar_prestamo, width=25).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="✅ Registrar Devolución",
                   command=self.registrar_devolucion, width=25).grid(row=1, column=1, padx=5, pady=5)

    # --- Métodos stub para cada funcionalidad ---
    def registrar_socio(self):
        messagebox.showinfo("Registrar Socio", "Funcionalidad en construcción")

    def listar_socios(self):
        messagebox.showinfo("Listar Socios", "Funcionalidad en construcción")

    def agregar_libro(self):
        messagebox.showinfo("Agregar Libro", "Funcionalidad en construcción")

    def catalogo_libros(self):
        messagebox.showinfo("Catálogo", "Funcionalidad en construcción")

    def realizar_prestamo(self):
        messagebox.showinfo("Préstamo", "Funcionalidad en construcción")

    def registrar_devolucion(self):
        messagebox.showinfo("Devolución", "Funcionalidad en construcción")

    def listar_prestamos(self):
        messagebox.showinfo("Préstamos", "Funcionalidad en construcción")

    def nueva_reserva(self):
        messagebox.showinfo("Reserva", "Funcionalidad en construcción")

    def ver_reservas(self):
        messagebox.showinfo("Reservas", "Funcionalidad en construcción")

    def acerca_de(self):
        messagebox.showinfo(
            "Acerca de",
            "Sistema de Gestión de Biblioteca Universitaria\n"
            "Programación 2 - UAE\n"
            "Grupo #1\n"
            "Semestre 3 - 2026"
        )

    def run(self):
        self.root.mainloop()
