

lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
lista2 = [53, 25, 36, 25, 45]
lista = lista2
rango = len(lista)
rango2 = rango//2


for i in range(rango2):

    if lista[i] > lista[rango-1-i]:
        lista[i], lista[rango-1-i] = lista[rango-1-i], lista[i]
print(lista)
