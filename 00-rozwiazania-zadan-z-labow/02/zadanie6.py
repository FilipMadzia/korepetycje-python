cennik = {
    "latte": 10,
    "czarna": 8,
    "cappuccino": 12,
}
print(cennik)

cennik["espresso"] = 6
cennik["cappuccino"] = 14
print(cennik)

cennik.pop("czarna")
print(cennik)

nazwa = input("Podaj nazwe kawy: ")
liczba = int(input("Podaj liczbe kaw: "))

cena = cennik.get(nazwa, 0)
print(f"Do zaplaty: {cena * liczba}")