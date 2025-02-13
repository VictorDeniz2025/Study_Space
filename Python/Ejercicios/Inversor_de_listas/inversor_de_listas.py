# Este codigo invierte una lista de numeros enteros


lista = [53, 31, 36, 25, 45]

rango = len(lista)
rango2 = rango//2


for i in range(rango2):
    if lista[i] > lista[rango-1-i]:
        lista[i], lista[rango-1-i] = lista[rango-1-i], lista[i]
        print(lista)
