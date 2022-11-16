haslo = input("Podaj haslo: ")
cnt = int(input("Podaj ilosc powtorzen: "))
licznik = 0
while licznik != cnt:
    powtorzone=input("Powtorz haslo: ")
    if powtorzone == haslo:
        licznik += 1
    if licznik == cnt:
        print("Dziekuje podales prawidlowe haslo")
