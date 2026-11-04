liczba = int(input("Podaj liczbę z zakresu 0-15: "))
oryginal = liczba

reszty = []

for i in range(4):
    reszty.append(liczba % 2)
    liczba //= 2 # liczba = liczba // 2

reszty.reverse()

print(reszty)
print(bin(oryginal)[2:]) # [2:] - pomijamy pierwsze dwa znaki '0b' w wyniku funkcji bin()