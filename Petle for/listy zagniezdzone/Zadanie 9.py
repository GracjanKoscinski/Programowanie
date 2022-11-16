plansza = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]


print("Poczatkowy wyglad planszy: (0) - pole puste ")

for i in range(len(plansza)):
    print(plansza[i])

# kh1-kolumna hetman 1 itd
kh1 = 0
kh2 = 5
kh3 = 7
kp = 3
rh1 = 5
rh2 = 6
rh3 = 1
rp = 3

plansza[0][5] = 9
plansza[5][6] = 9
plansza[7][1] = 9
plansza[3][3] = 1
print("Wyglad planszy po umieszczeniu hetmanow(9) oraz pionka(1)")
for i in range(len(plansza)):
    print(plansza[i])

if kh1 == kp or kh2 == kp or kh3 == kp:
    print("Hetman moze zaatakowac")
elif rh1 == rp or rh2 == rp or rh3 == rp:
    print("Hetman moze zaatakowac")
elif abs(rh1-rp) == abs(kh1-kp) or abs(rh2-rp) == abs(kh2-kp) or abs(rh3-rp) == abs(kh3-kp):
    print("Hetman moze zaatakowac")
else:
    print("Hetman nie moze zaatakowac")
