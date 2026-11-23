# dystans
dystans = float(input("Podaj dystans (km): "))

while dystans <= 0:
    print("Blad: dystans musi byc dodatni")
    dystans = float(input("Podaj dystans (km): "))

# spalanie
spalanie = float(input("Podaj srednie spalanie na 100 km: "))

while spalanie <= 0:
    print("Blad: spalanie musi byc dodatnie")
    spalanie = float(input("Podaj srednie spalanie na 100 km: "))

# cena za litr paliwa
cena_za_litr = float(input("Podaj cene litru paliwa: "))

while cena_za_litr <= 0:
    print("Blad: cena litru paliwa musi byc dodatnia")
    cena_za_litr = float(input("Podaj cene litru paliwa: "))

# ilość pasażerów
ilosc_pasazerow = int(input("Podaj ilosc pasazerow: "))

while ilosc_pasazerow <= 0:
    print("Blad: ilosc pasazerow musi byc dodatnia")
    ilosc_pasazerow = int(input("Podaj ilosc pasazerow: "))

zuzyte_paliwo = dystans * (spalanie / 100)
koszt_przejazdu = zuzyte_paliwo * cena_za_litr
koszt_na_osobe = koszt_przejazdu / ilosc_pasazerow

print("=" * 15)
print("Koszt podrozy")
print("=" * 15)
print(f"Zuzyte paliwo: {zuzyte_paliwo:.2f} l")
print(f"Calkowity koszt przejazdu: {koszt_przejazdu:.2f} zl")
print(f"Koszt na osobe: {koszt_na_osobe:.2f} zl")