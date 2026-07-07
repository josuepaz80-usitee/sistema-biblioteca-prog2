"""Cola (Queue) - para gestionar reservas en orden de llegada FIFO"""


class Queue:
    """Cola FIFO usando lista enlazada internamente"""

    def __init__(self):
        from src.data_structures.linked_list import LinkedList
        self.__items = LinkedList()

    def enqueue(self, data):
        """Agrega un elemento al final de la cola"""
        self.__items.append(data)

    def dequeue(self):
        """Elimina y retorna el elemento del frente"""
        if self.is_empty():
            return None
        items = self.__items.to_list()
        first = items[0]
        self.__items.remove(first)
        return first

    def peek(self):
        """Retorna el elemento del frente sin eliminarlo"""
        if self.is_empty():
            return None
        return self.__items.to_list()[0]

    def is_empty(self) -> bool:
        return self.__items.is_empty()

    @property
    def size(self) -> int:
        return self.__items.size

    def to_list(self) -> list:
        return self.__items.to_list()

    def __len__(self) -> int:
        return self.__items.size
