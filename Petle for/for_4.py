n = int(input())
for i in range(0, n):
    for j in range(0, i):
        print('*', end="")
    print("")
print("")
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print('*', end="")
    print("")