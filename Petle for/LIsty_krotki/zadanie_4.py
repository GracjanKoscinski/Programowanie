lista = ["napis", "inny", "jeszcze", "rozny"]
lista2 = []
krotka = ()
for i in range(len(lista)):
    lista2.extend([lista[i], len(lista[i])])
print(lista2)
