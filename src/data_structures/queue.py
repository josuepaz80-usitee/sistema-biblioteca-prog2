# COLA (Queue) - Estructura FIFO (First In, First Out)
# El primero en llegar es el primero en ser atendido
# Investigacion: Cairo, O., & Guardati, S. (2006). Estructuras de datos (3a ed.). McGraw-Hill.


class Queue:
    """Cola FIFO: se usa para las reservas (orden de llegada)"""

    def __init__(self):
        from src.data_structures.linked_list import LinkedList
        self.__items = LinkedList()

    # Agrega al final de la cola
    def enqueue(self, data):
        self.__items.append(data)

    # Saca al primero de la cola
    def dequeue(self):
        if self.is_empty():
            return None
        primero = self.__items.to_list()[0]
        self.__items.remove(primero)
        return primero

    # Muestra al primero sin sacarlo
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
