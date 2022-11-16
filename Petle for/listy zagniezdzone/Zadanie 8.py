lista = [[1, 2, 3, 0],
         [4, 5, 6, 0],
         [7, 8, 9, 0],
         [2, 0, 0, 0]]
suma = 0
#od lewej gory  do prawej dol
for i in range(len(lista)):
     for j in range(len(lista[i])):
         if i == j:
             suma += lista[i][j]

#od prawej gory do lewej dol
suma_2 = 0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if j == len(lista)-i-1:
            suma_2 += lista[i][j]


#jezeli macierz ma n nieparzyste
if len(lista) % 2 == 1:
    srodek_wiersze = len(lista) // 2
    suma += suma_2
    suma -= lista[srodek_wiersze][srodek_wiersze]
    print(suma)
#jezeli macierz ma n parzyste
else:
    suma += suma_2
    print(suma)



