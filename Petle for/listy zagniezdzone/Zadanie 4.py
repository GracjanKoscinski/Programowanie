tabliczka_mnozenia = [[] for i in range(10)]
# j = 1
# for i in range(10):
#     for g in range(10):
#         tabliczka_mnozenia[i].append((i + 1) * j)
#         j += 1
#     j = 1

j = 1
for i in range(10):
    while j <= 10:
        tabliczka_mnozenia[i].append((i + 1) * j)
        j += 1
    j = 1

for i in range(10):
    print(tabliczka_mnozenia[i])
