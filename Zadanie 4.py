lista = []


def CREATE(imie, nazwisko, pesel):
    return{
        'imie': imie,
        'nazwisko': nazwisko,
        'pesel': pesel
    }


def UPDATE(imie, nazwisko, pesel, lista):
    for i in range(len(lista)):
        if pesel == lista[i]['pesel']:
            lista[i]['imie'] = imie
            lista[i]['nazwisko'] = nazwisko
    return lista


def READ(imie, lista):
    for i in range(len(lista)):
        if imie == lista[i]['imie']:
            print(lista[i])
            return 0
    print("Nie ma takiej osoby na liście")
    return 0

def DELETE(pesel, lista):
    for i in range(len(lista)):
        if pesel == lista[i]['pesel']:
            lista[i].pop('imie')
            lista[i].pop('nazwisko')
            lista[i].pop('pesel')
    return lista


lista.append(CREATE('Gracjan', 'Koscinski', '132313213'))
lista.append(CREATE('Gracjan', 'Koscinski', '1322313213'))

UPDATE('Edward', 'Kos', '132313213', lista)
READ('Gracjan', lista)
DELETE('132313213', lista)
print(lista)
