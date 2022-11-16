pierwsza = []
druga = []
mnozenie = 1
iloczyn_skalarny = 0
n = int(input("Ile elementow maja miec tablice: "))

for i in range(n):
    element = int(input("Podaj element pierwszej listy: "))
    pierwsza.append(element)

for i in range(n):
    element = int(input("Podaj element drugiej listy: "))
    druga.append(element)

for i in range(n):
    mnozenie = pierwsza[i] * druga[i]
    iloczyn_skalarny += mnozenie

print(iloczyn_skalarny)
