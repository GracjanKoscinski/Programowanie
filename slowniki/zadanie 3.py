import math
lista = []

n = int(input("Podaj n:"))


def policz_odleglosc(lista):
    lista_wynikow = []
    min = 10000
    min_x = 0
    min_x2 = 0
    min_y = 0
    min_y2 = 0
    for i in range(n):
        for j in range(n):
            wynik_1 = (lista[i]['x'] - lista[j]['x']) ** 2
            wynik_2 = (lista[i]['y'] - lista[j]['y']) ** 2
            wynik = math.sqrt(wynik_1 + wynik_2)
            if i != j:
                if wynik < min:
                    min = wynik
                    min_x = lista[i]['x']
                    min_x2 = lista[j]['x']
                    min_y = lista[i]['y']
                    min_y2 = lista[j]['y']
                    lista_wynikow.append(wynik)
    return lista_wynikow, min_x, min_y, min_x2, min_y2


for i in range(n):
    slownik = {}
    wspolrzedna_x = int(input("Podaj wspolrzedna x: "))
    wspolrzedna_y = int(input("Podaj wspolrzedna y: "))
    slownik['x'] = wspolrzedna_x
    slownik['y'] = wspolrzedna_y
    lista.append(slownik)
print(lista)
print(policz_odleglosc(lista))
