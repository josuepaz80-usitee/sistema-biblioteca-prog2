"""Algoritmos de búsqueda"""


def busqueda_lineal(arr, target, key=None):
    """
    Búsqueda Lineal O(n)
    Recorre la lista elemento por elemento hasta encontrar el objetivo
    """
    if key is None:
        key_func = lambda x: x
    else:
        key_func = key

    for i, item in enumerate(arr):
        if key_func(item) == target:
            return i, item
    return -1, None


def busqueda_binaria(arr, target, key=None):
    """
    Búsqueda Binaria O(log n)
    Requiere que la lista esté ordenada
    """
    if key is None:
        key_func = lambda x: x
    else:
        key_func = key

    # Necesitamos ordenar primero
    from src.algorithms.sorting import merge_sort
    sorted_arr = merge_sort(arr, key=key)

    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = key_func(sorted_arr[mid])
        if mid_val == target:
            return mid, sorted_arr[mid]
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, None
