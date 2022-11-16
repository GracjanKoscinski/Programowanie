slowo1 = input("Podaj slowo nr 1: ")
slowo2 = input("Podaj slowo nr 2: ")

if len(slowo1) > len(slowo2):
    print(slowo1, "To dluzsze slowo")
elif len(slowo1) < len(slowo2):
    print(slowo2, "To dluzsze slowo")
else:
    print("Te slowa sa rownej dlugosci")

if slowo1 != slowo2:
    if slowo1 < slowo2:
        print(slowo1, "to slowo leksykograficznie pierwsze")
    else:
        print(slowo2, "to slowo leksykograficznie pierwsze")
else:
    print("Te slowa sa takie same!")
    