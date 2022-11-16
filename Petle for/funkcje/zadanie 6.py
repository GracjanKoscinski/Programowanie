def czy_wszystkie(napis):
    alfabet = "abcdefghijklmnopqrstuwvxyz"
    bledy = 0
    for i in alfabet:
        if i not in napis:
            bledy = 1
    if bledy == 0:
        return True
    else:
        return False

napis = input("Podaj slowo do sprawdzenia:")

if czy_wszystkie(napis):
    print("TAK")
else:
    print("NIE")
