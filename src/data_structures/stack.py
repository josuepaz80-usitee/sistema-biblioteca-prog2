"""Pila (Stack) - para deshacer operaciones LIFO"""


class Stack:
    """Pila LIFO usando lista enlazada internamente"""

    def __init__(self):
        from src.data_structures.linked_list import LinkedList
        self.__items = LinkedList()

    def push(self, data):
        """Apila un elemento al inicio"""
        self.__items.prepend(data)

    def pop(self):
        """Desapila y retorna el elemento superior"""
        if self.is_empty():
            return None
        items = self.__items.to_list()
        top = items[0]
        self.__items.remove(top)
        return top

    def peek(self):
        """Retorna el elemento superior sin desapilar"""
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
