# Twoim zadaniem jest dodać wszystkie liczby całkowite podane na wejściu.
#
# Wejście
# W pierwszym wierszu znajduje się liczba t testów (0 < t < 100) Każdy test opisany jest w następujący sposób. W pierwszym wierszu dana jest liczba n - liczba liczb do zsumowania. Następnie podanych jest n liczb pooddzielanych spacją.

t = int(input())

while t > 0:
    a = 0
    n = int(input())
    numbers = list(map(int, input().split()))
    for line in range(n):
        for number in numbers:
            a += number
        print(a)
        break
    t -= 1
