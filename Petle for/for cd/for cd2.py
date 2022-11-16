slowo = input("Podaj slowo: ")
cnt = 0
for znak in slowo:
    if znak == "a" or znak == "e" or znak == "y" or znak == "i" or znak == "o" or znak == "u":
        cnt = cnt + 1
print("Liczba samoglosek w slowie:", slowo, "wynosi:", cnt)

