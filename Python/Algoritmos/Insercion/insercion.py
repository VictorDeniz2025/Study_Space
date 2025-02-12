
# Algoritmo de ordenamiento por inserción

def ordenar_por_inserción(arr):
    for i in range(1, len(arr)):  # Recorrer el arreglo
        key = arr[i]
        j = i - 1

        # Mover los elementos del arreglo que son mayores que la clave a una posición adelante de su posición actual
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        # Mostrar el estado del arreglo después de cada iteración
        print(f"Iteración {i}: {arr}")

# Ejemplo de uso


arr = [64, 25, 12, 22, 11]

print("Matriz original:")
print(arr)
ordenar_por_inserción(arr)
print("Matriz ordenada:")
print(arr)
