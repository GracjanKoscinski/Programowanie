lista = [[1, 2, 3],
         ["abba","aff"],
         [-2, -4, -5]]
lista_nowa = []
for i in range(len(lista)):
    for j in range(len(lista[i])):
        lista_nowa.append(lista[i][j])

print(lista_nowa)