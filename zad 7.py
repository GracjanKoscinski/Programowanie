def zamiana_systemow(dziesietna):
    if dziesietna == 0:
        return 0
    # return dziesietna % 2 + 10 * zamiana_systemow(int(dziesietna) // 2)


dziesietna = int(input())
print(zamiana_systemow(dziesietna))
