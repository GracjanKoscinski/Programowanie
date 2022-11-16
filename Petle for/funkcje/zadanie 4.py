def czy_dodatanie(a,b,c):
    odp = True
    if a <= 0 or b <= 0 or c<= 0:
        odp = False
    return odp

def czy_trojkat(a, b, c):
    if not czy_dodatanie(a,b,c):
        print("Liczby nie sa dodatnie")
        return 0
    else:
        if a+b > c and a+c > b and b+c > a:
            return True
        else:
            return False

a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))
if czy_trojkat(a, b, c):
    print("Mozna stworzyc trojkat")
else:
    print("Nie mozna stworzyc trojkata")
