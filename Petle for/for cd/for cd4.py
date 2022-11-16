napis = input()
# for i in range(len(napis)//2):
#     if napis[i] != napis[len(napis)-1]:
#         exit(1)
odwrocony = ""

for znak in napis:
    odwrocony = znak + odwrocony
if odwrocony == napis:
    print("To palindrom")
else:
    print("To nie jest palindrom")
