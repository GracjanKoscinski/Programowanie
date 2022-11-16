n = int(input())
a = 0
b = 1
if n == 1 or n == 2 :
    print(b)
else:
    for i in range(2, n):
        c = a+b
        a = b
        b = c
    print(b)
