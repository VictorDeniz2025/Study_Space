# Algortimo de ordenacion rapida (Quicksort)

def ordenacion_rapida(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr)//2]
    elementos_inf = [x for x in arr if x < pivote]
    elementos_eq = [x for x in arr if x == pivote]
    elementos_sup = [x for x in arr if x > pivote]

    return ordenacion_rapida(elementos_inf)+elementos_eq+ordenacion_rapida(elementos_sup)


# Ejemplo de uso
arr = [3, 6, 8, 10, 1, 2, 1]
print(" Array original: ", arr)
print(" Array ordenado: ", ordenacion_rapida(arr))  # [1, 1, 2, 3, 6, 8, 10]
