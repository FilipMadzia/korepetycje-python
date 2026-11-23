cennik = {
    "jablka": 4.99,
    "banany": 5.49,
    "ziemniaki": 0.99,
    "marchewki": 1.99
}

print("Cennik")
for klucz, wartosc in cennik.items():
    print(f"{klucz}: {wartosc} zl/kg")

do_zaplaty = 0

while True:
    produkt = input("Podaj ktory produkt chcesz kupic: ")

    if produkt == "koniec":
        break

    if produkt.lower() in cennik:
        ile_kg = float(input("Podaj ile kg chcesz: "))
        suma = ile_kg * cennik[produkt]

        print(f"{ile_kg} kg * {cennik[produkt]} zl/kg = {suma} zl")

        do_zaplaty += suma
    else:
        print("Brak takiego produktu")

print(f"Laczna kwota do zaplaty: {do_zaplaty:.2f} zl")