def ordenar_por_inserción(arr):

    for i in range(1, len(arr)):
        cle = arr[i]
        j = i - 1

        while j >= 0 and cle < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = cle


# Ejemplo de uso

arr = [64, 25, 12, 22, 11]

print("Matriz original:")
print(arr)
ordenar_por_inserción(arr)
print("Matriz ordenada:")
print(arr)
