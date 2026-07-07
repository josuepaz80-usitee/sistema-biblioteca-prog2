# PILA (Stack) - Estructura LIFO (Last In, First Out)
# El ultimo en entrar es el primero en salir
# Sirve para deshacer operaciones (undo)
# Investigacion: Cairo, O., & Guardati, S. (2006). Estructuras de datos (3a ed.). McGraw-Hill.


class Stack:
    """Pila LIFO: se usa para deshacer prestamos/devoluciones"""

    def __init__(self):
        from src.data_structures.linked_list import LinkedList
        self.__items = LinkedList()

    # Apila al inicio
    def push(self, data):
        self.__items.prepend(data)

    # Desapila el ultimo ingresado
    def pop(self):
        if self.is_empty():
            return None
        ultimo = self.__items.to_list()[0]
        self.__items.remove(ultimo)
        return ultimo

    # Muestra el tope sin desapilar
    def peek(self):
        if self.is_empty():
            return None
        return self.__items.to_list()[0]

    def is_empty(self):
        return self.__items.is_empty()

    def get_tamano(self):
        return len(self.__items)

    def to_list(self):
        return self.__items.to_list()
