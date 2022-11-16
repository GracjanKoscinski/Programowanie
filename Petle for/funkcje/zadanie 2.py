# def funkcja():
#     odp = input("Czy chcesz zakonczyc program?(t/n) ")
#     if odp == 't':
#         return 0
#     else:
#         funkcja()

def funkcja():
    odp=input("Czy chcesz zakonczyc program?(t/n) ")
    funkcja2(odp)
    return odp

def funkcja2(odp):
    if odp == 't':
        return 0
    else:
        funkcja()

funkcja()
