lista1 = [[1, 2, 3],
          [4, 5, 6]]
lista2 = [[8, 7, 5],
          [3, 4, 1]]

for i in range(2):
    for j in range(3):
        print(lista1[i][j]+lista2[i][j], end=" ")
    print()
