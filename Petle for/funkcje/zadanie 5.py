import random

def funkcja(n, z1, z2):
    lista = []
    for i in range(n):
        lista.append(random.randint(z1, z2))
    return lista


n = int(input("Podaj dlugosc tablicy:"))
z1 = int(input("Podaj minimalny zakres liczb losowych:"))
z2 = int(input("Podaj maksymalny zakres liczb losowych:"))

print(funkcja(n, z1, z2))
