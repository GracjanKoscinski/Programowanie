lista = [[1, 2, 3],
         [4, 5, 6]]

for i in range(len(lista)):
    for j in range(len(lista[i])):
        print(lista[i][-1-j], end=" ")
    print()
