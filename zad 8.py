def suma_cyfr(liczba):
    if liczba == 0:
        return 0
    return (liczba % 10 + int(suma_cyfr(liczba/10)))


liczba = int(input())
print(suma_cyfr(liczba))
