# k = int(10)
# m = int(50)
# while k != 0:
#     if k < 5:
#         k=k-1
#         m=m+k
#     else:
#         k=k-2
#         m=m-k
#
# print(m)

#2 czesc

k = 10
m = 50

while True:
    if k <5:
        k=k-1
        m=m+k
    else:
        k=k-2
        m=m-k
    if  not k != 0:
        break
print(m)