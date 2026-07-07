"""Pruebas básicas del modelo"""
import sys
sys.path.insert(0, '.')
from src.models.estudiante import Estudiante
from src.models.docente import Docente
from src.models.libro import Libro
from src.models.socio import Socio


def test_personas():
    est = Estudiante("1234567890", "Juan", "Pérez", "Computación", 3)
    doc = Docente("0987654321", "María", "Gómez", "Ciencias")

    socio_est = Socio(est)
    socio_doc = Socio(doc)

    assert socio_est.tipo_socio() == "Estudiante"
    assert socio_doc.tipo_socio() == "Docente"
    assert socio_est.nombre_completo == "Juan Pérez"
    print("✅ Test personas OK")


def test_libro():
    libro = Libro("978-3-16-148410-0", "Python para Todos",
                  "John Doe", "O'Reilly", 2024, 3)

    assert libro.ejemplares == 3
    assert libro.disponibles == 3
    assert libro.esta_disponible()

    libro.prestar_ejemplar()
    assert libro.disponibles == 2

    libro.devolver_ejemplar()
    assert libro.disponibles == 3

    print("✅ Test libro OK")


def test_algoritmos():
    from src.algorithms.sorting import bubble_sort, merge_sort, quick_sort
    from src.algorithms.search import busqueda_lineal, busqueda_binaria

    datos = [5, 3, 8, 1, 9, 2]
    assert bubble_sort(datos) == [1, 2, 3, 5, 8, 9]
    assert merge_sort(datos) == [1, 2, 3, 5, 8, 9]
    assert quick_sort(datos) == [1, 2, 3, 5, 8, 9]

    idx, val = busqueda_lineal(datos, 8)
    assert val == 8

    idx2, val2 = busqueda_binaria(sorted(datos), 8)
    assert val2 == 8

    print("✅ Test algoritmos OK")


def test_estructuras():
    from src.data_structures.linked_list import LinkedList
    from src.data_structures.queue import Queue
    from src.data_structures.stack import Stack

    # Lista enlazada
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.size == 3
    assert ll.to_list() == [1, 2, 3]
    print("✅ Test LinkedList OK")

    # Cola
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    assert q.dequeue() == "A"
    assert q.peek() == "B"
    print("✅ Test Queue OK")

    # Pila
    s = Stack()
    s.push("X")
    s.push("Y")
    assert s.pop() == "Y"
    assert s.peek() == "X"
    print("✅ Test Stack OK")


if __name__ == "__main__":
    test_personas()
    test_libro()
    test_algoritmos()
    test_estructuras()
    print("\n🎉 Todas las pruebas pasaron")
