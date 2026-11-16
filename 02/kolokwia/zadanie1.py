plecak_cena = 120
ksiazka_cena = 45
zeszyt_cena = 6
dlugopis_cena = 3

print(f"Plecak - {plecak_cena} zl")
print(f"Ksiazka - {ksiazka_cena} zl")
print(f"Zeszyt - {zeszyt_cena} zl")
print(f"Dlugopis - {dlugopis_cena} zl")

plecak_ilosc = 0
ksiazka_ilosc = 0
zeszyt_ilosc = 0
dlugopis_ilosc = 0

while True:
    plecak_ilosc = int(input("Podaj ilosc plecakow: "))

    if plecak_ilosc < 0:
        print("Nie mozna podac liczby ujemnej. Sproboj ponownie")
    else:
        break

while True:
    ksiazka_ilosc = int(input("Podaj ilosc ksiazek: "))

    if ksiazka_ilosc < 0:
        print("Nie mozna podac liczby ujemnej. Sproboj ponownie")
    else:
        break

while True:
    zeszyt_ilosc = int(input("Podaj ilosc zeszytow: "))

    if zeszyt_ilosc < 0:
        print("Nie mozna podac liczby ujemnej. Sprubój ponownie")
    else:
        break

while True:
    dlugopis_ilosc = int(input("Podaj ilosc dlugopisow: "))

    if dlugopis_ilosc < 0:
        print("Nie mozna podac liczby ujemnej. Sproboj ponownie")
    else:
        break

suma = (plecak_cena * plecak_ilosc) + (ksiazka_cena * ksiazka_ilosc) + (zeszyt_cena * zeszyt_ilosc) + (dlugopis_cena * dlugopis_ilosc)

dostawa_platna = False
ile_brakuje = 0

if suma < 199:
    ile_brakuje = 199 - suma
    dostawa_platna = True

if dostawa_platna:
    print(f"Suma: {suma} zl + 15 zl za dostawe. Lacznie {suma + 15} zl. Do darmowej dostawy brakuje {ile_brakuje} zl")
else:
    print(f"Suma: {suma} zl. Darmowa dostawa")