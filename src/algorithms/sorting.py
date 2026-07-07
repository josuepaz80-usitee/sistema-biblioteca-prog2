"""Algoritmos de ordenamiento"""

# Ordenamiento Básico: Burbuja
def bubble_sort(arr, key=None, reverse=False):
    """
    Ordenamiento Burbuja O(n²)
    Intercambia elementos adyacentes si están en orden incorrecto
    """
    n = len(arr)
    if key is None:
        key_func = lambda x: x
    else:
        key_func = key

    result = list(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = key_func(result[j])
            b = key_func(result[j + 1])
            if (a > b) if not reverse else (a < b):
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


# Ordenamiento Básico: Inserción
def insertion_sort(arr, key=None, reverse=False):
    """
    Ordenamiento por Inserción O(n²)
    Construye la salida insertando cada elemento en su posición correcta
    """
    if key is None:
        key_func = lambda x: x
    else:
        key_func = key

    result = list(arr)
    for i in range(1, len(result)):
        temp = result[i]
        j = i - 1
        while j >= 0:
            a = key_func(result[j])
            b = key_func(temp)
            if (a > b) if not reverse else (a < b):
                result[j + 1] = result[j]
                j -= 1
            else:
                break
        result[j + 1] = temp
    return result


# Ordenamiento Avanzado: Merge Sort O(n log n)
def merge_sort(arr, key=None, reverse=False):
    """Merge Sort - Divide y vencerás O(n log n)"""
    if key is None:
        key_func = lambda x: x
    else:
        key_func = key

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if (key_func(left[i]) <= key_func(right[j])) if not reverse else (key_func(left[i]) >= key_func(right[j])):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def msort(items):
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = msort(items[:mid])
        right = msort(items[mid:])
        return merge(left, right)

    return msort(list(arr))


# Ordenamiento Avanzado: Quick Sort O(n log n) promedio
def quick_sort(arr, key=None, reverse=False):
    """Quick Sort - Divide y vencerás con pivote O(n log n) promedio"""
    if key is None:
        key_func = lambda x: x
    else:
        key_func = key

    def qsort(items):
        if len(items) <= 1:
            return items
        pivot = items[len(items) // 2]
        p_val = key_func(pivot)
        if not reverse:
            left = [x for x in items if key_func(x) < p_val]
            right = [x for x in items if key_func(x) > p_val]
        else:
            left = [x for x in items if key_func(x) > p_val]
            right = [x for x in items if key_func(x) < p_val]
        middle = [x for x in items if key_func(x) == p_val]
        return qsort(left) + middle + qsort(right)

    return qsort(list(arr))
