n = int(input())

for i in range(1, 2*n, 2):
    spacje = n-(i//2)
    print(spacje*" "+"*"*i)

print((n-1)*" "+"|_|")
