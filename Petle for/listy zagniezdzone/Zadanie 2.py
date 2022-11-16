lista = [[1, 2, 3],
         [4, 5, 6]]
k = int(input("Podaj liczbe k:"))

for i in range(2):
    for j in range(3):
        print(lista[i][j]*k, end=" ")
    print()
