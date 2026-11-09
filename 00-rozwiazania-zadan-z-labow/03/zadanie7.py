liczba = -1

while liczba < 0:
    liczba = int(input("Podaj nieujemna liczbe calkowita: "))
    if liczba < 0:
        print("Blad, liczba nie moze byc ujemna")

testowa = bin(liczba)[2:]
reszty = []

while True:
    if liczba == 0:
        if len(reszty) == 0:
            reszty.append("0")
        break
    reszty.append(str(liczba % 2))
    liczba = liczba // 2

reszty.reverse()
binarna = "".join(reszty)

print(binarna)

if binarna == testowa:
    print("Sa zgodne")