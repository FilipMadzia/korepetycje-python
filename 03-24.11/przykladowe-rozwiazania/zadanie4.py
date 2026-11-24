def czy_doskonala(n):
    dzielniki = []

    for i in range(1, n):
        if n % i == 0:
            dzielniki.append(i)

    suma_dzielnikow = sum(dzielniki)

    if suma_dzielnikow == n:
        return True
    else:
        return False

    # albo krócej
    # return suma_dzielnikow == n

ile_doskonalych = 0

for n in range(1, 1001):
    if czy_doskonala(n):
        print(n, end=" ")
        ile_doskonalych += 1

print(f"\nLacznie liczb doskonalych (zakres 1-1000): {ile_doskonalych}")