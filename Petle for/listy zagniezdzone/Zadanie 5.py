lista = [[1, 2, 3],
         [16, 8],
         [-2, 4, 5],
         [5, -22]]
index_max = 0
suma = 0
najwieksza = 0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        suma += lista[i][j]
        if suma > najwieksza:
            najwieksza = suma
            index_max = j
    suma = 0
print("ktory wiersz macierzy:", index_max+1, "Suma:", najwieksza)