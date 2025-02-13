def ordenar_por_seleccion(arr):
    n = len(arr)
    for i in range(n):
        # Encuentra el índice del mínimo en la parte no ordenada del array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Intercambia los elementos
        arr[i], arr[min_index] = arr[min_index], arr[i]
        # Mostrar el estado del arreglo después de cada iteración
        print(f"Iteración {i}: {arr}")


# Ejemplo de uso
arr = [64, 25, 12, 22, 11]
print("Arreglo original:")
print(arr)
ordenar_por_seleccion(arr)
print("Arreglo ordenado:")
print(arr)
