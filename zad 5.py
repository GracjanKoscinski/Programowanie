def sumowanie_rekurencyjne(lista, dlugosc):
    if dlugosc == 0:
        return 0
    return sumowanie_rekurencyjne(lista, dlugosc - 1) + lista[dlugosc - 1]


lista = [1, 2, 3, 4]
dlugosc = len(lista)

print(sumowanie_rekurencyjne(lista, dlugosc))

# def sumowanie(lista):
#     if len(lista) == 0:
#         return 0
#     return sumowanie(lista) + lista[len(lista)-1]
#
#
# lista = [1, 2, 3]
#
# print(sumowanie(lista))
