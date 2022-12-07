lista = []


def CREATE(imie,nazwisko,pesel):
    return{
        'imie': imie,
        'nazwisko': nazwisko,
        'pesel': pesel
    }


def UPDATE(imie,nazwisko,pesel,lista):
    for i in range(len(lista)):
        if pesel == lista[i]['pesel']:
            lista[i]['imie'] = imie
            lista[i]['nazwisko'] = nazwisko
    return lista


lista.append(CREATE('Gracjan', 'Koscinski', '132313213'))
lista.append(CREATE('Gracjan', 'Koscinski', '1322313213'))

UPDATE('Edward', 'Kos', '132313213', lista)

print(lista)