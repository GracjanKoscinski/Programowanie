def fibonacci(liczba):
    if liczba <= 1:
        return liczba
    return fibonacci(liczba-1) + fibonacci(liczba-2)


liczba = int(input())

print(fibonacci(liczba))