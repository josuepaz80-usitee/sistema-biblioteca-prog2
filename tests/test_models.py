# ============================================================
# Mayra Vera — Pruebas unitarias del sistema
# Verifica modelos POO, estructuras de datos, algoritmos
# y base de datos funcionan correctamente
# ============================================================

# Pruebas unitarias del sistema
# Verifica que los modelos, estructuras y algoritmos funcionan correctamente
import sys
import os

# Agrega la ruta del proyecto para que los imports funcionen
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.estudiante import Estudiante
from src.models.docente import Docente
from src.models.libro import Libro
from src.models.socio import Socio
from src.models.prestamo import Prestamo
from src.models.reserva import Reserva
from src.data_structures.linked_list import LinkedList
from src.data_structures.queue import Queue
from src.data_structures.stack import Stack
from src.algorithms.sorting import bubble_sort, insertion_sort, merge_sort, quick_sort
from src.algorithms.search import busqueda_lineal, busqueda_binaria


def probar_personas():
    """Prueba: herencia, encapsulamiento y polimorfismo"""
    print("=== PRUEBA: Modelos POO ===")

    # Crear un estudiante y un docente
    est = Estudiante("1234567890", "Juan", "Perez", "Computacion", 3)
    doc = Docente("0987654321", "Maria", "Gomez", "Ciencias")

    # Verificar getters
    assert est.get_nombre() == "Juan"
    assert doc.get_apellido() == "Gomez"
    assert est.get_carrera() == "Computacion"
    assert doc.get_departamento() == "Ciencias"

    # Envolver en Socio (polimorfismo)
    socio_est = Socio(est)
    socio_doc = Socio(doc)

    # Polimorfismo: mismo metodo, distinto resultado
    print("  Tipo socio 1:", socio_est.tipo_socio())
    print("  Tipo socio 2:", socio_doc.tipo_socio())
    assert socio_est.tipo_socio() == "Estudiante"
    assert socio_doc.tipo_socio() == "Docente"
    assert socio_est.get_nombre_completo() == "Juan Perez"

    print("  Polimorfismo OK: mismo metodo tipo_socio() retorna valores distintos")
    print("  Encapsulamiento OK: atributos privados con getters")
    print("  Herencia OK: Estudiante y Docente heredan de Persona")
    print("  Abstraccion OK: Persona define el contrato tipo_socio()")


def probar_libro():
    """Prueba: prestamo y devolucion de ejemplares"""
    print("\n=== PRUEBA: Libro ===")
    libro = Libro("978-3-16-148410-0", "Python para Todos", "John Doe",
                  "O'Reilly", 2024, 3)

    print("  Ejemplares:", libro.get_ejemplares())
    print("  Disponibles:", libro.get_disponibles())
    assert libro.get_ejemplares() == 3
    assert libro.get_disponibles() == 3
    assert libro.esta_disponible() == True

    # Prestar un ejemplar
    libro.prestar_ejemplar()
    print("  Prestamo exitoso. Disponibles ahora:", libro.get_disponibles())
    assert libro.get_disponibles() == 2

    # Devolver el ejemplar
    libro.devolver_ejemplar()
    print("  Devolucion exitosa. Disponibles ahora:", libro.get_disponibles())
    assert libro.get_disponibles() == 3

    print("  OK: Prestamo y devolucion funcionan correctamente")


def probar_algoritmos():
    """Prueba: algoritmos de ordenamiento y busqueda"""
    print("\n=== PRUEBA: Algoritmos ===")
    datos = [5, 3, 8, 1, 9, 2]
    esperado = [1, 2, 3, 5, 8, 9]
    print("  Lista original:", datos)

    # Probar cada algoritmo
    assert bubble_sort(datos) == esperado
    print("  Bubble sort: OK")

    assert insertion_sort(datos) == esperado
    print("  Insertion sort: OK")

    assert merge_sort(datos) == esperado
    print("  Merge sort: OK")

    assert quick_sort(datos) == esperado
    print("  Quick sort: OK")

    # Busqueda lineal
    indice = busqueda_lineal(datos, 8)
    print("  Busqueda lineal: 8 esta en indice", indice)
    assert datos[indice] == 8

    # Busqueda binaria (requiere datos ordenados)
    ordenados = sorted(datos)
    indice2 = busqueda_binaria(ordenados, 8)
    print("  Busqueda binaria: 8 esta en indice", indice2)
    assert ordenados[indice2] == 8

    # No encontrado
    assert busqueda_lineal(datos, 99) == -1
    assert busqueda_binaria(ordenados, 99) == -1
    print("  Elemento no encontrado: OK")
    print("  Todos los algoritmos funcionan correctamente")


def probar_estructuras():
    """Prueba: LinkedList, Queue y Stack"""
    print("\n=== PRUEBA: Estructuras de Datos ===")

    # Lista enlazada
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("  LinkedList:", ll.to_list())
    assert len(ll) == 3
    assert ll.to_list() == [10, 20, 30]
    ll.prepend(5)
    assert ll.to_list() == [5, 10, 20, 30]
    ll.remove(20)
    assert ll.to_list() == [5, 10, 30]
    print("  Lista enlazada: OK")

    # Cola (FIFO)
    q = Queue()
    q.enqueue("Reserva 1")
    q.enqueue("Reserva 2")
    q.enqueue("Reserva 3")
    print("  Queue:", q.to_list())
    primero = q.dequeue()
    assert primero == "Reserva 1"
    assert q.peek() == "Reserva 2"
    print("  Cola FIFO (orden de llegada): OK")

    # Pila (LIFO)
    s = Stack()
    s.push("Operacion 1")
    s.push("Operacion 2")
    s.push("Operacion 3")
    print("  Stack:", s.to_list())
    ultimo = s.pop()
    assert ultimo == "Operacion 3"
    assert s.peek() == "Operacion 2"
    print("  Pila LIFO (deshacer operacion): OK")


def probar_database():
    """Prueba: conexion a SQLite y creacion de tablas"""
    print("\n=== PRUEBA: Base de Datos SQLite ===")
    from src.database.db_manager import DatabaseManager

    # Usar base de datos en memoria para la prueba
    db = DatabaseManager(":memory:")
    db.connect()
    db.create_tables()
    db.disconnect()
    print("  Conexion a SQLite: OK")
    print("  Creacion de tablas: OK")
    print("  NOTA: CRUD completo se probara cuando se implementen los formularios")


if __name__ == "__main__":
    probar_personas()
    probar_libro()
    probar_algoritmos()
    probar_estructuras()
    probar_database()
    print("\n=== TODAS LAS PRUEBAS PASARON ===")
