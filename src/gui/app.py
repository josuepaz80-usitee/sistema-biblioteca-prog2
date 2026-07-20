# ============================================================
# Jodie Parrales — Interfaz grafica con Tkinter
# Ventana principal, menus desplegables, formularios CRUD
# Conectada a la BD via SocioRepository y LibroRepository
# Tkinter viene por defecto en Python (no requiere instalacion)
# Referencia: Grayson, J. E. (2000). Python and Tkinter programming.
# ============================================================

# PASO #1 IMPORTAR LIBRERIAS
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

# PASO #2 IMPORTAR MODULOS DEL PROYECTO
from src.database.db_manager import DatabaseManager
from src.database.socio_repo import SocioRepository
from src.database.libro_repo import LibroRepository
from src.database.prestamo_repo import PrestamoRepository
from src.database.reserva_repo import ReservaRepository


class BibliotecaApp:
    """Aplicacion principal del Sistema de Biblioteca"""

    # PASO #3 INICIALIZAR LA APLICACION
    def __init__(self):
        # Conectar a la base de datos
        self.__db = DatabaseManager()
        self.__db.connect()
        self.__db.create_tables()
        self.__socio_repo = SocioRepository(self.__db)
        self.__libro_repo = LibroRepository(self.__db)
        self.__prestamo_repo = PrestamoRepository(self.__db)
        self.__reserva_repo = ReservaRepository(self.__db)

        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title("Sistema de Gestion de Biblioteca Universitaria")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f0f0")

        # Crear menu y panel principal
        self._crear_menu()
        self._crear_panel_principal()

    # PASO #4 CERRAR CONEXION AL SALIR
    def __del__(self):
        try:
            self.__db.disconnect()
        except Exception:
            pass

    # PASO #5 CREAR BARRA DE MENU
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

    # PASO #6 CREAR PANEL PRINCIPAL CON BIENVENIDA
    def _crear_panel_principal(self):
        """Crea el contenido principal de la ventana"""
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

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

        # Panel de botones de acceso rapido
        panel_botones = ttk.LabelFrame(frame, text="Acceso Rapido", padding=15)
        panel_botones.pack(pady=20, fill=tk.X)

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

    # ============================================================
    # FORMULARIO: REGISTRAR SOCIO
    # ============================================================

    # PASO #7 VENTANA PARA REGISTRAR UN NUEVO SOCIO
    def registrar_socio(self):
        """Abre formulario para registrar un socio en la BD"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar Socio")
        ventana.geometry("450x400")
        ventana.configure(bg="#f0f0f0")
        ventana.transient(self.root)
        ventana.grab_set()

        # Campos del formulario
        ttk.Label(ventana, text="REGISTRAR SOCIO", font=("Arial", 14, "bold"))\
            .pack(pady=10)

        frame = ttk.Frame(ventana, padding=15)
        frame.pack(fill=tk.BOTH, expand=True)

        # Cedula
        ttk.Label(frame, text="Cedula:").grid(row=0, column=0, sticky="w", pady=3)
        entry_cedula = ttk.Entry(frame, width=30)
        entry_cedula.grid(row=0, column=1, pady=3)

        # Nombre
        ttk.Label(frame, text="Nombre:").grid(row=1, column=0, sticky="w", pady=3)
        entry_nombre = ttk.Entry(frame, width=30)
        entry_nombre.grid(row=1, column=1, pady=3)

        # Apellido
        ttk.Label(frame, text="Apellido:").grid(row=2, column=0, sticky="w", pady=3)
        entry_apellido = ttk.Entry(frame, width=30)
        entry_apellido.grid(row=2, column=1, pady=3)

        # Tipo (combobox: Estudiante o Docente)
        ttk.Label(frame, text="Tipo:").grid(row=3, column=0, sticky="w", pady=3)
        combo_tipo = ttk.Combobox(frame, values=["Estudiante", "Docente"], state="readonly", width=27)
        combo_tipo.set("Estudiante")
        combo_tipo.grid(row=3, column=1, pady=3)

        # Carrera / Departamento
        ttk.Label(frame, text="Carrera / Depto.:").grid(row=4, column=0, sticky="w", pady=3)
        entry_carrera = ttk.Entry(frame, width=30)
        entry_carrera.grid(row=4, column=1, pady=3)

        # Semestre (solo si es Estudiante)
        ttk.Label(frame, text="Semestre:").grid(row=5, column=0, sticky="w", pady=3)
        entry_semestre = ttk.Entry(frame, width=30)
        entry_semestre.grid(row=5, column=1, pady=3)

        # Telefono
        ttk.Label(frame, text="Telefono:").grid(row=6, column=0, sticky="w", pady=3)
        entry_telefono = ttk.Entry(frame, width=30)
        entry_telefono.grid(row=6, column=1, pady=3)

        # PASO #8 FUNCION PARA GUARDAR EL SOCIO
        def guardar():
            cedula = entry_cedula.get().strip()
            nombre = entry_nombre.get().strip()
            apellido = entry_apellido.get().strip()
            tipo = combo_tipo.get()
            carrera = entry_carrera.get().strip()
            semestre_texto = entry_semestre.get().strip()
            telefono = entry_telefono.get().strip()

            # Validar campos obligatorios
            if not cedula or not nombre or not apellido:
                messagebox.showerror("Error", "Cedula, nombre y apellido son obligatorios",
                                     parent=ventana)
                return

            # Convertir semestre a entero si no esta vacio
            try:
                semestre = int(semestre_texto) if semestre_texto else None
            except ValueError:
                messagebox.showerror("Error", "Semestre debe ser un numero entero",
                                     parent=ventana)
                return

            try:
                # Usar SocioRepository para insertar
                self.__socio_repo.insertar(cedula, nombre, apellido, tipo,
                                           carrera, semestre, telefono)
                messagebox.showinfo("Exito", "Socio registrado correctamente",
                                    parent=ventana)
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error BD", str(e), parent=ventana)

        # Boton Guardar
        ttk.Button(frame, text="Guardar Socio", command=guardar)\
            .grid(row=7, column=0, columnspan=2, pady=15)

    # ============================================================
    # FORMULARIO: LISTAR SOCIOS
    # ============================================================

    # PASO #9 VENTANA PARA LISTAR TODOS LOS SOCIOS
    def listar_socios(self):
        """Muestra una tabla con todos los socios registrados"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Lista de Socios")
        ventana.geometry("750x400")
        ventana.transient(self.root)
        ventana.grab_set()

        ttk.Label(ventana, text="LISTA DE SOCIOS", font=("Arial", 14, "bold"))\
            .pack(pady=10)

        # Crear Treeview con scrollbars
        frame = ttk.Frame(ventana, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
        scroll_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)

        tree = ttk.Treeview(frame,
                            columns=("cedula", "nombre", "apellido", "tipo", "carrera", "telefono"),
                            show="headings",
                            yscrollcommand=scroll_y.set,
                            xscrollcommand=scroll_x.set)

        scroll_y.config(command=tree.yview)
        scroll_x.config(command=tree.xview)

        # Definir encabezados
        tree.heading("cedula", text="Cedula")
        tree.heading("nombre", text="Nombre")
        tree.heading("apellido", text="Apellido")
        tree.heading("tipo", text="Tipo")
        tree.heading("carrera", text="Carrera/Depto")
        tree.heading("telefono", text="Telefono")

        tree.column("cedula", width=110)
        tree.column("nombre", width=120)
        tree.column("apellido", width=120)
        tree.column("tipo", width=90)
        tree.column("carrera", width=130)
        tree.column("telefono", width=100)

        tree.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Cargar datos desde la BD
        try:
            socios = self.__socio_repo.listar_todos()
            for socio in socios:
                # socio es una tupla: (cedula, nombre, apellido, tipo, carrera, semestre, telefono)
                tree.insert("", tk.END, values=(
                    socio[0], socio[1], socio[2], socio[3], socio[4], socio[6]
                ))
        except Exception as e:
            messagebox.showerror("Error BD", str(e), parent=ventana)

    # ============================================================
    # FORMULARIO: AGREGAR LIBRO
    # ============================================================

    # PASO #10 VENTANA PARA AGREGAR UN NUEVO LIBRO
    def agregar_libro(self):
        """Abre formulario para agregar un libro al catalogo"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Libro")
        ventana.geometry("450x380")
        ventana.configure(bg="#f0f0f0")
        ventana.transient(self.root)
        ventana.grab_set()

        ttk.Label(ventana, text="AGREGAR LIBRO", font=("Arial", 14, "bold"))\
            .pack(pady=10)

        frame = ttk.Frame(ventana, padding=15)
        frame.pack(fill=tk.BOTH, expand=True)

        # ISBN
        ttk.Label(frame, text="ISBN:").grid(row=0, column=0, sticky="w", pady=3)
        entry_isbn = ttk.Entry(frame, width=30)
        entry_isbn.grid(row=0, column=1, pady=3)

        # Titulo
        ttk.Label(frame, text="Titulo:").grid(row=1, column=0, sticky="w", pady=3)
        entry_titulo = ttk.Entry(frame, width=30)
        entry_titulo.grid(row=1, column=1, pady=3)

        # Autor
        ttk.Label(frame, text="Autor:").grid(row=2, column=0, sticky="w", pady=3)
        entry_autor = ttk.Entry(frame, width=30)
        entry_autor.grid(row=2, column=1, pady=3)

        # Editorial
        ttk.Label(frame, text="Editorial:").grid(row=3, column=0, sticky="w", pady=3)
        entry_editorial = ttk.Entry(frame, width=30)
        entry_editorial.grid(row=3, column=1, pady=3)

        # Anio
        ttk.Label(frame, text="Anio:").grid(row=4, column=0, sticky="w", pady=3)
        entry_anio = ttk.Entry(frame, width=30)
        entry_anio.grid(row=4, column=1, pady=3)

        # Ejemplares
        ttk.Label(frame, text="Ejemplares:").grid(row=5, column=0, sticky="w", pady=3)
        entry_ejemplares = ttk.Entry(frame, width=30)
        entry_ejemplares.grid(row=5, column=1, pady=3)

        # PASO #11 FUNCION PARA GUARDAR EL LIBRO
        def guardar():
            isbn = entry_isbn.get().strip()
            titulo = entry_titulo.get().strip()
            autor = entry_autor.get().strip()
            editorial = entry_editorial.get().strip()
            anio_texto = entry_anio.get().strip()
            ejemplares_texto = entry_ejemplares.get().strip()

            if not isbn or not titulo or not autor:
                messagebox.showerror("Error", "ISBN, titulo y autor son obligatorios",
                                     parent=ventana)
                return

            try:
                anio = int(anio_texto) if anio_texto else None
            except ValueError:
                messagebox.showerror("Error", "Anio debe ser un numero entero",
                                     parent=ventana)
                return

            try:
                ejemplares = int(ejemplares_texto) if ejemplares_texto else 1
            except ValueError:
                messagebox.showerror("Error", "Ejemplares debe ser un numero entero",
                                     parent=ventana)
                return

            try:
                self.__libro_repo.insertar(isbn, titulo, autor, editorial, anio, ejemplares)
                messagebox.showinfo("Exito", "Libro agregado correctamente", parent=ventana)
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error BD", str(e), parent=ventana)

        ttk.Button(frame, text="Guardar Libro", command=guardar)\
            .grid(row=6, column=0, columnspan=2, pady=15)

    # ============================================================
    # FORMULARIO: VER CATALOGO
    # ============================================================

    # PASO #12 VENTANA PARA VER EL CATALOGO DE LIBROS
    def ver_catalogo(self):
        """Muestra una tabla con todos los libros del catalogo"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Catalogo de Libros")
        ventana.geometry("800x400")
        ventana.transient(self.root)
        ventana.grab_set()

        ttk.Label(ventana, text="CATALOGO DE LIBROS", font=("Arial", 14, "bold"))\
            .pack(pady=10)

        frame = ttk.Frame(ventana, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
        scroll_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)

        tree = ttk.Treeview(frame,
                            columns=("isbn", "titulo", "autor", "editorial", "anio",
                                     "ejemplares", "disponibles"),
                            show="headings",
                            yscrollcommand=scroll_y.set,
                            xscrollcommand=scroll_x.set)

        scroll_y.config(command=tree.yview)
        scroll_x.config(command=tree.xview)

        tree.heading("isbn", text="ISBN")
        tree.heading("titulo", text="Titulo")
        tree.heading("autor", text="Autor")
        tree.heading("editorial", text="Editorial")
        tree.heading("anio", text="Anio")
        tree.heading("ejemplares", text="Ejemplares")
        tree.heading("disponibles", text="Disponibles")

        tree.column("isbn", width=120)
        tree.column("titulo", width=200)
        tree.column("autor", width=150)
        tree.column("editorial", width=120)
        tree.column("anio", width=60)
        tree.column("ejemplares", width=80)
        tree.column("disponibles", width=80)

        tree.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        try:
            libros = self.__libro_repo.listar_todos()
            for libro in libros:
                # libro es una tupla: (isbn, titulo, autor, editorial, anio, ejemplares, disponibles)
                tree.insert("", tk.END, values=(
                    libro[0], libro[1], libro[2], libro[3],
                    libro[4], libro[5], libro[6]
                ))
        except Exception as e:
            messagebox.showerror("Error BD", str(e), parent=ventana)

    # ============================================================
    # FORMULARIOS: Prestamos, Devoluciones y Reservas
    # ============================================================

    # PASO #13 REALIZAR PRESTAMO
    def realizar_prestamo(self):
        """Abre formulario para registrar un nuevo prestamo"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Realizar Prestamo")
        ventana.geometry("480x350")
        ventana.configure(bg="#f0f0f0")
        ventana.transient(self.root)
        ventana.grab_set()

        ttk.Label(ventana, text="REALIZAR PRESTAMO", font=("Arial", 14, "bold"))\
            .pack(pady=10)

        frame = ttk.Frame(ventana, padding=15)
        frame.pack(fill=tk.BOTH, expand=True)

        # Cedula del socio
        ttk.Label(frame, text="Cedula del Socio:")\
            .grid(row=0, column=0, sticky="w", pady=3)
        entry_cedula = ttk.Entry(frame, width=30)
        entry_cedula.grid(row=0, column=1, pady=3)

        # ISBN del libro
        ttk.Label(frame, text="ISBN del Libro:")\
            .grid(row=1, column=0, sticky="w", pady=3)
        entry_isbn = ttk.Entry(frame, width=30)
        entry_isbn.grid(row=1, column=1, pady=3)

        ttk.Label(frame, text="", font=("Arial", 8)).grid(row=2, column=0, columnspan=2, pady=2)
        ttk.Label(frame, text="Busque socio y libro en los menus correspondientes", 
                  font=("Arial", 8, "italic"), foreground="gray")\
            .grid(row=3, column=0, columnspan=2, pady=2)

        def guardar_prestamo():
            cedula = entry_cedula.get().strip()
            isbn = entry_isbn.get().strip()

            if not cedula or not isbn:
                messagebox.showerror("Error", "Cedula e ISBN son obligatorios",
                                     parent=ventana)
                return

            # Verificar que el socio existe
            socio = self.__socio_repo.obtener_por_cedula(cedula)
            if not socio:
                messagebox.showerror("Error", "Socio no encontrado. Verifique la cedula",
                                     parent=ventana)
                return

            # Verificar que el libro existe y tiene ejemplares disponibles
            libro = self.__libro_repo.obtener_por_isbn(isbn)
            if not libro:
                messagebox.showerror("Error", "Libro no encontrado. Verifique el ISBN",
                                     parent=ventana)
                return

            if libro[6] < 1:  # disponibles
                messagebox.showerror("Error", "No hay ejemplares disponibles de este libro",
                                     parent=ventana)
                return

            try:
                fecha = str(date.today())
                # Registrar prestamo
                self.__prestamo_repo.insertar(cedula, isbn, fecha)
                # Reducir disponibles
                self.__libro_repo.actualizar_disponibles(isbn, libro[6] - 1)
                messagebox.showinfo("Exito", "Prestamo registrado correctamente",
                                    parent=ventana)
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error BD", str(e), parent=ventana)

        ttk.Button(frame, text="Confirmar Prestamo", command=guardar_prestamo)\
            .grid(row=4, column=0, columnspan=2, pady=15)

    # PASO #14 REGISTRAR DEVOLUCION
    def registrar_devolucion(self):
        """Abre formulario para registrar devolucion de un prestamo"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar Devolucion")
        ventana.geometry("480x350")
        ventana.configure(bg="#f0f0f0")
        ventana.transient(self.root)
        ventana.grab_set()

        ttk.Label(ventana, text="REGISTRAR DEVOLUCION", font=("Arial", 14, "bold"))\
            .pack(pady=10)

        frame = ttk.Frame(ventana, padding=15)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="ID del Prestamo:")\
            .grid(row=0, column=0, sticky="w", pady=3)
        entry_id = ttk.Entry(frame, width=30)
        entry_id.grid(row=0, column=1, pady=3)

        ttk.Label(frame, text="ISBN del Libro:")\
            .grid(row=1, column=0, sticky="w", pady=3)
        entry_isbn = ttk.Entry(frame, width=30)
        entry_isbn.grid(row=1, column=1, pady=3)

        ttk.Label(frame, text="", font=("Arial", 8)).grid(row=2, column=0, columnspan=2, pady=2)
        ttk.Label(frame, text="Ver 'Prestamos' para consultar el ID de cada prestamo",
                  font=("Arial", 8, "italic"), foreground="gray")\
            .grid(row=3, column=0, columnspan=2, pady=2)

        def guardar_devolucion():
            prestamo_id_texto = entry_id.get().strip()
            isbn = entry_isbn.get().strip()

            if not prestamo_id_texto or not isbn:
                messagebox.showerror("Error", "ID del prestamo e ISBN son obligatorios",
                                     parent=ventana)
                return

            try:
                prestamo_id = int(prestamo_id_texto)
            except ValueError:
                messagebox.showerror("Error", "ID debe ser un numero entero",
                                     parent=ventana)
                return

            # Verificar que el prestamo existe y esta pendiente
            prestamo = self.__prestamo_repo.obtener_por_id(prestamo_id)
            if not prestamo:
                messagebox.showerror("Error", "Prestamo no encontrado",
                                     parent=ventana)
                return

            if prestamo[3] is not None:  # fecha_devolucion
                messagebox.showinfo("Info", "Este prestamo ya fue devuelto",
                                    parent=ventana)
                return

            try:
                fecha = str(date.today())
                self.__prestamo_repo.registrar_devolucion(prestamo_id, fecha)
                # Incrementar disponibles del libro
                libro = self.__libro_repo.obtener_por_isbn(isbn)
                if libro:
                    self.__libro_repo.actualizar_disponibles(
                        isbn, libro[6] + 1)
                messagebox.showinfo("Exito", "Devolucion registrada correctamente",
                                    parent=ventana)
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error BD", str(e), parent=ventana)

        ttk.Button(frame, text="Confirmar Devolucion", command=guardar_devolucion)\
            .grid(row=4, column=0, columnspan=2, pady=15)

    # PASO #15 VER PRESTAMOS
    def ver_prestamos(self):
        """Muestra tabla con todos los prestamos"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Lista de Prestamos")
        ventana.geometry("750x400")
        ventana.transient(self.root)
        ventana.grab_set()

        ttk.Label(ventana, text="LISTA DE PRESTAMOS", font=("Arial", 14, "bold"))\
            .pack(pady=10)

        frame = ttk.Frame(ventana, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
        scroll_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)

        tree = ttk.Treeview(frame,
                            columns=("id", "cedula", "isbn", "fecha_prestamo",
                                     "fecha_devolucion"),
                            show="headings",
                            yscrollcommand=scroll_y.set,
                            xscrollcommand=scroll_x.set)

        scroll_y.config(command=tree.yview)
        scroll_x.config(command=tree.xview)

        tree.heading("id", text="ID")
        tree.heading("cedula", text="Cedula Socio")
        tree.heading("isbn", text="ISBN")
        tree.heading("fecha_prestamo", text="Fecha Prestamo")
        tree.heading("fecha_devolucion", text="Fecha Devolucion")

        tree.column("id", width=50)
        tree.column("cedula", width=120)
        tree.column("isbn", width=120)
        tree.column("fecha_prestamo", width=130)
        tree.column("fecha_devolucion", width=130)

        tree.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        try:
            prestamos = self.__prestamo_repo.listar_todos()
            for p in prestamos:
                dev = p[3] if p[3] else "Pendiente"
                tree.insert("", tk.END, values=(p[0], p[1], p[2], p[3], dev))
        except Exception as e:
            messagebox.showerror("Error BD", str(e), parent=ventana)

    # PASO #16 NUEVA RESERVA
    def nueva_reserva(self):
        """Abre formulario para crear una nueva reserva"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Nueva Reserva")
        ventana.geometry("480x300")
        ventana.configure(bg="#f0f0f0")
        ventana.transient(self.root)
        ventana.grab_set()

        ttk.Label(ventana, text="NUEVA RESERVA", font=("Arial", 14, "bold"))\
            .pack(pady=10)

        frame = ttk.Frame(ventana, padding=15)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Cedula del Socio:")\
            .grid(row=0, column=0, sticky="w", pady=3)
        entry_cedula = ttk.Entry(frame, width=30)
        entry_cedula.grid(row=0, column=1, pady=3)

        ttk.Label(frame, text="ISBN del Libro:")\
            .grid(row=1, column=0, sticky="w", pady=3)
        entry_isbn = ttk.Entry(frame, width=30)
        entry_isbn.grid(row=1, column=1, pady=3)

        ttk.Label(frame, text="", font=("Arial", 8)).grid(row=2, column=0, columnspan=2, pady=2)
        ttk.Label(frame, text="Se reserva cuando no hay ejemplares disponibles",
                  font=("Arial", 8, "italic"), foreground="gray")\
            .grid(row=3, column=0, columnspan=2, pady=2)

        def guardar_reserva():
            cedula = entry_cedula.get().strip()
            isbn = entry_isbn.get().strip()

            if not cedula or not isbn:
                messagebox.showerror("Error", "Cedula e ISBN son obligatorios",
                                     parent=ventana)
                return

            try:
                fecha = str(date.today())
                self.__reserva_repo.insertar(cedula, isbn, fecha)
                messagebox.showinfo("Exito", "Reserva registrada correctamente",
                                    parent=ventana)
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error BD", str(e), parent=ventana)

        ttk.Button(frame, text="Guardar Reserva", command=guardar_reserva)\
            .grid(row=4, column=0, columnspan=2, pady=15)

    # PASO #17 VER RESERVAS
    def ver_reservas(self):
        """Muestra tabla con todas las reservas activas"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Lista de Reservas")
        ventana.geometry("600x400")
        ventana.transient(self.root)
        ventana.grab_set()

        ttk.Label(ventana, text="RESERVAS ACTIVAS", font=("Arial", 14, "bold"))\
            .pack(pady=10)

        frame = ttk.Frame(ventana, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
        scroll_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)

        tree = ttk.Treeview(frame,
                            columns=("id", "cedula", "isbn", "fecha", "activa"),
                            show="headings",
                            yscrollcommand=scroll_y.set,
                            xscrollcommand=scroll_x.set)

        scroll_y.config(command=tree.yview)
        scroll_x.config(command=tree.xview)

        tree.heading("id", text="ID")
        tree.heading("cedula", text="Cedula Socio")
        tree.heading("isbn", text="ISBN")
        tree.heading("fecha", text="Fecha Reserva")
        tree.heading("activa", text="Activa")

        tree.column("id", width=50)
        tree.column("cedula", width=120)
        tree.column("isbn", width=120)
        tree.column("fecha", width=130)
        tree.column("activa", width=70)

        tree.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        try:
            reservas = self.__reserva_repo.listar_activas()
            for r in reservas:
                activa_texto = "Si" if r[4] == 1 else "No"
                tree.insert("", tk.END, values=(r[0], r[1], r[2], r[3], activa_texto))
        except Exception as e:
            messagebox.showerror("Error BD", str(e), parent=ventana)

    # PASO #18 INICIAR LA APLICACION
    def run(self):
        """Inicia la aplicacion"""
        self.root.mainloop()
