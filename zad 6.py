def czy_najwiekszy(el, lista):
    if len(lista) == 0:
        return True
    if el >= lista[-1]:
        lista.pop(-1)
        return czy_najwiekszy(el, lista)
    if el < lista[-1]:
        return False


el = int(input())

lista = [1, 2, 10, 11, 14, 4]

if czy_najwiekszy(el, lista):
    print("Tak")
else:
    print("Nie")