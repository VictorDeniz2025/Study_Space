# Este codigo invierte una lista de numeros enteros
# Toma la lista y la invierte, es decir, el primer elemento pasa a ser el ultimo y el ultimo el primero


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista)

rango = len(lista)
rango2 = rango//2


for i in range(rango2):
    lista[i], lista[rango-1-i] = lista[rango-1-i], lista[i]

print(lista)
