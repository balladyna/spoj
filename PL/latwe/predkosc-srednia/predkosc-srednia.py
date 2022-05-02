# Pociąg z miejscowości A do B jedzie z prędkością v1, a wraca z miejscowości B do A z prędkością v2. Obliczyć średnią prędkość na całej trasie. Uwaga: Dane wejściowe będą tak dobrane, aby wynik był liczba całkowitą.
#
# Wejście
# Na wejściu znajduje się dokładnie jedna liczba całkowita t (1<=t<=1000) oznaczająca liczbę zestawów danych. W wierszach od 2 do t+1 znajdują się dwie liczby całkowite oddzielone spacja v1 oraz v2 (1<=v1,v2<=10000).

t = int(input())

while t > 0:
    t -= 1
    v1, v2 = map(int, input().split())
    vs = int(2*v1*v2/(v1+v2))
    print(vs)

