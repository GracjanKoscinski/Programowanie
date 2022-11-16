n = 10
dodatnie = 0
ujemne = 0


while n != 0:
    n = float(input(n))
    if n >= 0:
            dodatnie+=1
    else:
            ujemne+=1

print("Ilosc liczb dodatnich:",dodatnie-1,"Ilosc liczb ujemnych:",ujemne)