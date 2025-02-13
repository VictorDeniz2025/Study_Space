# Algoritmo de ordenación por fusión (merge sort)

def sort_merge(arr):
    if len(arr) <= 1:
        return arr

    # Divide el array en dos mitades
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    # Ordena recursivamente cada mitad
    left = sort_merge(left)
    right = sort_merge(right)

    # Fusiona las mitades ordenadas
    return fusionar(left, right)


def fusionar(izquierda, derecha):
    result = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            result.append(izquierda[i])
            i += 1
        else:
            result.append(derecha[j])
            j += 1

    result.extend(izquierda[i:])
    result.extend(derecha[j:])
    return result

# Ejemplo de uso


arr = [64, 25, 12, 22, 11]
arr_ordenado = sort_merge(arr)
print("Array ordenado: ", arr_ordenado)
