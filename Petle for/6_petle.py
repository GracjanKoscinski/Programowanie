binarna = int(input())
i = 0
wynik_czastkowy = int(0)
wynik_ogolny = int(0)
while binarna != 0:
        ostatnia_cyfra = binarna % 10
        wynik_czastkowy = ostatnia_cyfra * (2 ** i)
        i = i+1
        wynik_ogolny = wynik_ogolny + wynik_czastkowy
        binarna = binarna//10
print(wynik_ogolny)
