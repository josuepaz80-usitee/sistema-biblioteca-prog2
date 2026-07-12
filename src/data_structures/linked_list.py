# ============================================================
# Cesar Gonzales — Lista Enlazada Simple
# Cada nodo: dato + puntero al siguiente nodo
# Operaciones: append, prepend, remove, find
# Referencia: Weiss, M. A. (2013). Estructuras de datos y algoritmos.
# ============================================================

# PASO 1: CREAR LA LISTA ENLAZADA
# Cada nodo tiene un dato y un puntero al siguiente nodo
# Investigacion: Weiss, M. A. (2013). Estructuras de datos y algoritmos (4a ed.). Pearson.


class Nodo:
    """Nodo de la lista enlazada"""
    def __init__(self, data):
        self.data = data
        self.next = None  # Apunta al siguiente nodo (None si es el ultimo)


class LinkedList:
    """Lista enlazada simple"""

    def __init__(self):
        self.__head = None  # Primer nodo de la lista
        self.__tamano = 0

    def is_empty(self):
        return self.__head is None

    def get_tamano(self):
        return self.__tamano

    def append(self, data):
        """Agrega un elemento al final de la lista"""
        nuevo = Nodo(data)
        if self.is_empty():
            self.__head = nuevo
        else:
            actual = self.__head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo
        self.__tamano += 1

    def prepend(self, data):
        """Agrega un elemento al inicio de la lista"""
        nuevo = Nodo(data)
        nuevo.next = self.__head
        self.__head = nuevo
        self.__tamano += 1

    def remove(self, data):
        """Elimina un elemento de la lista"""
        if self.is_empty():
            return False
        if self.__head.data == data:
            self.__head = self.__head.next
            self.__tamano -= 1
            return True
        actual = self.__head
        while actual.next is not None:
            if actual.next.data == data:
                actual.next = actual.next.next
                self.__tamano -= 1
                return True
            actual = actual.next
        return False

    # Busqueda lineal: recorre nodo por nodo (O(n))
    def find(self, data):
        actual = self.__head
        while actual is not None:
            if actual.data == data:
                return actual.data
            actual = actual.next
        return None

    def to_list(self):
        """Convierte la lista enlazada a lista normal de Python"""
        resultado = []
        actual = self.__head
        while actual is not None:
            resultado.append(actual.data)
            actual = actual.next
        return resultado

    def __iter__(self):
        actual = self.__head
        while actual is not None:
            yield actual.data
            actual = actual.next

    def __len__(self):
        return self.__tamano

    def __str__(self):
        valores = []
        actual = self.__head
        while actual is not None:
            valores.append(str(actual.data))
            actual = actual.next
        return "[" + " → ".join(valores) + "]"
