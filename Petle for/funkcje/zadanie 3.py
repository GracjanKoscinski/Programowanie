def min_i_max(a, b, c):
    maksymalna = a
    minimalna = a
    if a < b:
        maksymalna = b
    elif a < c:
        maksymalna = c

    if b < a:
        minimalna = b
    elif c < a:
        minimalna = c

    return minimalna, maksymalna

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
print("Wynik w postaci: minimalna,maksymalna",min_i_max(a, b, c))

