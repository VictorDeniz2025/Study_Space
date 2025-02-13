# Algoritmo de ordenación de elementos por burbuja

def burbuja(arr):
    n = len(arr)
    print(n)  # Mostrar el número de elementos en el arreglo

    for i in range(n):              # Iterar sobre todos los elementos del arreglo
        for j in range(0, n-i-1):   # Iterar sobre los elementos restantes

            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Mostrar el estado del arreglo después de cada intercambio
                print(f"Intercambiando {arr[j]} y {arr[j+1]}: {arr}")
    return arr

# Ejemplo de uso


arr = [64, 34, 25, 12, 22, 11, 90]
print("El arreglo original es:")
print(arr)
ordenado = burbuja(arr)
print("El arreglo ordenado es:")
print(ordenado)

# Complejidad del algoritmo de ordenación por burbuja:
# En el peor de los casos (cuando el arreglo está ordenado en orden inverso),
# el algoritmo realiza n*(n-1)/2 comparaciones e intercambios, donde n es el número de elementos en el arreglo.
# Por lo tanto, la complejidad temporal en el peor de los casos es O(n^2).
# En el mejor de los casos (cuando el arreglo ya está ordenado), el algoritmo realiza n-1 comparaciones,
# por lo que la complejidad temporal en el mejor de los casos es O(n).
# La complejidad espacial del algoritmo es O(1) ya que solo utiliza una cantidad constante de espacio adicional.
