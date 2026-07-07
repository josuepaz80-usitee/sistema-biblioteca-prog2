# ALGORITMOS DE BUSQUEDA
# Investigacion: Joyanes Aguilar, L. (2020). Programacion orientada a objetos
# con Python. McGraw-Hill Interamericana.


# BUSQUEDA LINEAL (O(n))
# Recorre la lista elemento por elemento hasta encontrar el objetivo
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Retorna el indice donde encontro el elemento
    return -1  # No encontrado


# BUSQUEDA BINARIA (O(log n))
# Requiere que la lista este ORDENADA previamente
# Divide el espacio de busqueda a la mitad en cada paso
def busqueda_binaria(lista_ordenada, objetivo):
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista_ordenada[medio] == objetivo:
            return medio  # Encontrado
        elif lista_ordenada[medio] < objetivo:
            izquierda = medio + 1  # Buscar en la mitad derecha
        else:
            derecha = medio - 1  # Buscar en la mitad izquierda

    return -1  # No encontrado
