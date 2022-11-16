lista = [[1, 2, 3],
         [4, 5, 6]]
nowa = []
for i in range(len(lista)):
    for j in range(len(lista[0])):
        nowa[j][i]=lista[i][j]

for i in nowa:
    print(i)