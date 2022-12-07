n = int(input("Podaj liczbę dat:"))
lista = []


def sortowanie(lista):
    for i in range(len(lista) - 1):
        if lista[i]['dzien'] > lista[i + 1]['dzien']:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

    for i in range(len(lista) - 1):
        if lista[i]['miesiac'] > lista[i + 1]['miesiac']:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

    for i in range(len(lista) - 1):
        if lista[i]['rok'] > lista[i + 1]['rok']:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


for i in range(n):
    slownik = {
    }
    print("Slownik nr", i+1)
    dzien = int(input("Podaj dzien: "))
    miesiac = int(input("Podaj miesiac: "))
    rok = int(input("Podaj rok: "))
    slownik['dzien'] = dzien
    slownik['miesiac'] = miesiac
    slownik['rok'] = rok
    lista.append(slownik)


print(sortowanie(lista))
