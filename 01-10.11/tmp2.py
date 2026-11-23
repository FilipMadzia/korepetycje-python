owoce = []

while True:
    wpis_uzytkownika = input("Podaj owoc lub wpisz koniec: ")

    if wpis_uzytkownika == "koniec":
        break

    owoce.append(wpis_uzytkownika)

print(owoce)