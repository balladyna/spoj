# Napisać program do dodawania dwóch liczb całkowitych. Na wejściu podane są w oddzielnych liniach dwie liczby naturalne A oraz B mniejsze od 200. Na wyjściu należy wypisać wartość ich sumy, A + B.

A = input()
B = input()

if 0 <= int(A) < 200 and 0 <= int(B) < 200:
    print(int(A) + int(B))
