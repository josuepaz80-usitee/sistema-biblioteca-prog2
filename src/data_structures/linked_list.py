"""Lista enlazada simple - para el catálogo dinámico de libros"""


class Node:
    """Nodo de la lista enlazada"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Lista enlazada simple"""

    def __init__(self):
        self.__head = None
        self.__size = 0

    def is_empty(self) -> bool:
        return self.__head is None

    @property
    def size(self) -> int:
        return self.__size

    def append(self, data):
        """Agrega un elemento al final"""
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = new_node
        self.__size += 1

    def prepend(self, data):
        """Agrega un elemento al inicio"""
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node
        self.__size += 1

    def remove(self, data) -> bool:
        """Elimina un elemento por su valor"""
        if self.is_empty():
            return False
        if self.__head.data == data:
            self.__head = self.__head.next
            self.__size -= 1
            return True
        current = self.__head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.__size -= 1
                return True
            current = current.next
        return False

    def find(self, data):
        """Busca un elemento por su valor (búsqueda lineal)"""
        current = self.__head
        while current:
            if current.data == data:
                return current.data
            current = current.next
        return None

    def to_list(self) -> list:
        """Convierte la lista enlazada a lista de Python"""
        result = []
        current = self.__head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __iter__(self):
        current = self.__head
        while current:
            yield current.data
            current = current.next

    def __len__(self) -> int:
        return self.__size

    def __str__(self) -> str:
        values = [str(d) for d in self.to_list()]
        return "[" + " → ".join(values) + "]"
