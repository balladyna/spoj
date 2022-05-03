# Napisz program, który oblicza sumę trzech liczb całkowitych.
#
# Wejście
# Na wejście programu podane zostaną trzy liczby całkowite (nieprzekraczające 100) rozdzielone znakiem nowej linii.

a = int(input())
b = int(input())
c = int(input())

if a <= 100 and b <= 100 and c <= 100:
    d = a + b + c
    print(d)