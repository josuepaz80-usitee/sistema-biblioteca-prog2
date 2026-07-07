# ALGORITMOS DE ORDENAMIENTO
# Investigacion: Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009).
# Introduction to algorithms (3rd ed.). MIT Press.


# ORDENAMIENTO BASICO 1: Burbuja (O(n^2))
# Compara pares adyacentes y los intercambia si estan en orden incorrecto
def bubble_sort(lista):
    n = len(lista)
    resultado = lista[:]  # Copia de la lista original
    for i in range(n):
        for j in range(0, n - i - 1):
            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
    return resultado


# ORDENAMIENTO BASICO 2: Insercion (O(n^2))
# Inserta cada elemento en su posicion correcta dentro de la parte ordenada
def insertion_sort(lista):
    resultado = lista[:]
    for i in range(1, len(resultado)):
        temp = resultado[i]
        j = i - 1
        while j >= 0 and resultado[j] > temp:
            resultado[j + 1] = resultado[j]
            j -= 1
        resultado[j + 1] = temp
    return resultado


# ORDENAMIENTO AVANZADO 1: Merge Sort (O(n log n))
# Divide la lista en mitades, ordena cada una y las fusiona
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return _merge(izquierda, derecha)


def _merge(izquierda, derecha):
    """Funcion auxiliar que fusiona dos listas ordenadas"""
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agrega los elementos restantes
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado


# ORDENAMIENTO AVANZADO 2: Quick Sort (O(n log n) promedio)
# Selecciona un pivote y particiona en menores y mayores
def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]
    izquierda = []
    centro = []
    derecha = []

    for x in lista:
        if x < pivote:
            izquierda.append(x)
        elif x == pivote:
            centro.append(x)
        else:
            derecha.append(x)

    return quick_sort(izquierda) + centro + quick_sort(derecha)
