import uuid


def nowe_panstwo(nazwa, liczba_ludnosci, kontynent, stolica_id):
    return {
        "id": str(uuid.uuid4()),
        "nazwa": nazwa,
        "liczba_ludności": liczba_ludnosci,
        "kontynent": kontynent,
        "stolica": stolica_id
    }


def nowe_miasto(nazwa, liczba_ludnosci):
    return {
        "id": str(uuid.uuid4()),
        "nazwa": nazwa,
        "liczba_ludności": liczba_ludnosci,
    }


def ustaw_stolica(nazwa_kraju, nazwa_stolicy, p_db, m_db):
    szukany_kraj = None
    for kraj in p_db:
        if kraj["nazwa"] == nazwa_kraju:
            szukany_kraj = kraj
            break

    szukana_stolica = None

    for miasto in m_db:
        if miasto["nazwa"] == nazwa_stolicy:
            szukana_stolica = miasto
            break

    if szukana_stolica is not None and szukany_kraj is not None:
        szukany_kraj["stolica_id"] = szukana_stolica["id"]
        szukany_kraj['stolica'] = szukana_stolica['nazwa']
        return True

    return False


def najwiekszy_kraj(panstwa_db):
    najwiekszy = 0
    ten_kraj = ""
    for kraj in panstwa_db:
        if kraj['liczba_ludności'] > najwiekszy:
            najwiekszy = kraj['liczba_ludności']
            ten_kraj = kraj['nazwa']
    return ten_kraj, najwiekszy


def najliczniejsza_stolica(miasta_db):
    najliczniejsza = 0
    ta_stolica = ""
    for miasto in miasta_db:
        if miasto['liczba_ludności'] > najliczniejsza:
            najliczniejsza = miasto['liczba_ludności']
            ta_stolica = miasto['nazwa']
    return ta_stolica, najliczniejsza


def najliczniejsza_stolica_kontynent(panstwa_db, miasto_db, kontynent):
    najliczniejsza = 0
    ta_stolica = ""
    for panstwo in panstwa_db:
        for miasto in miasto_db:
            if miasto['id'] == panstwo['stolica_id']:
                if panstwo['kontynent'] == kontynent and miasto['liczba_ludności'] > najliczniejsza:
                    najliczniejsza = miasto['liczba_ludności']
                    ta_stolica = miasto['nazwa']
    return ta_stolica, najliczniejsza


# jezeli kontnent z panstwa rowny i po id musza byc rowne
panstwa_db = []
miasta_db = []

# panstwa
panstwa_db.append(nowe_panstwo('Francja', 68, 'Europa', None))
panstwa_db.append(nowe_panstwo('Włochy', 60, 'Europa', None))
panstwa_db.append(nowe_panstwo('USA', 331, 'Ameryka Północna', None))
panstwa_db.append(nowe_panstwo('Kanada', 38, 'Ameryka Północna', None))
panstwa_db.append(nowe_panstwo('Chiny', 1412, 'Azja', None))
panstwa_db.append(nowe_panstwo('Japonia', 125, 'Azja', None))
panstwa_db.append(nowe_panstwo('Indie', 1339, 'Azja', None))
panstwa_db.append(nowe_panstwo('Etiopia', 113, 'Afryka', None))
panstwa_db.append(nowe_panstwo('Maroko', 34, 'Afryka', None))
panstwa_db.append(nowe_panstwo('Algieria', 42, 'Afryka', None))

# miasta
miasta_db.append(nowe_miasto('Paryż', 12))
miasta_db.append(nowe_miasto('Rzym', 3))
miasta_db.append(nowe_miasto('Waszyngton', 1))
miasta_db.append(nowe_miasto('Ottawa', 1))
miasta_db.append(nowe_miasto('Pekin', 22))
miasta_db.append(nowe_miasto('Tokio', 14))
miasta_db.append(nowe_miasto('Nowe Delhi', 19))
miasta_db.append(nowe_miasto('Addis Abeba', 4))
miasta_db.append(nowe_miasto('Rabat', 1))
miasta_db.append(nowe_miasto('Algier', 5))

# ustawianie stolic
ustaw_stolica('Francja', 'Paryż', panstwa_db, miasta_db)
ustaw_stolica('Włochy', 'Rzym', panstwa_db, miasta_db)
ustaw_stolica('USA', 'Waszyngton', panstwa_db, miasta_db)
ustaw_stolica('Kanada', 'Ottawa', panstwa_db, miasta_db)
ustaw_stolica('Chiny', 'Pekin', panstwa_db, miasta_db)
ustaw_stolica('Japonia', 'Tokio', panstwa_db, miasta_db)
ustaw_stolica('Indie', 'Nowe Delhi', panstwa_db, miasta_db)
ustaw_stolica('Etiopia', 'Addis Abeba', panstwa_db, miasta_db)
ustaw_stolica('Maroko', 'Rabat', panstwa_db, miasta_db)
ustaw_stolica('Algieria', 'Algier', panstwa_db, miasta_db)


# print(najwiekszy_kraj(panstwa_db))
# print(najliczniejsza_stolica(miasta_db))
kontynent = str(input("Podaj kontynent który chcesz zbadać: "))
print(najliczniejsza_stolica_kontynent(panstwa_db, miasta_db, kontynent))
