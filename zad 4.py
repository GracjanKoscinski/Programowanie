def dwumian_newtona(n, k):
    if k == 0 or k == n:
        return 1
    return dwumian_newtona(n-1, k-1) + dwumian_newtona(n-1, k)


n = int(input())
k = int(input())

print(dwumian_newtona(n, k))

