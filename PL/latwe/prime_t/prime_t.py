# PRIME_T - Liczby Pierwsze
# Sprawdź, które spośród danych liczb są liczbami pierwszymi
#
# Input
# n - liczba testów n<100000, w kolejnych liniach n liczb z przedziału [1..10000]
#
# Output
# Dla każdej liczby słowo TAK, jeśli liczba ta jest pierwsza, słowo: NIE, w przeciwnym wypadku.

from math import sqrt

n = int(input())


def is_prime():
    a = 0
    n = int(input())
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                a += 1
                return "NIE"
        if a == 0:
            return "TAK"
    else:
        return "NIE"


for a in range(n):
    print(is_prime())
