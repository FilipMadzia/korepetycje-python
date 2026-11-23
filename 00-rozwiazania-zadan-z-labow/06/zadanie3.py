import random

def rezerwuj(zajete, rzedy=15, miejsca=20, miejsce=None, preferowane=None):
    if rzedy <= 0:
            return "Rzedy musza byc dodatnie"
    if miejsca <= 0:
        return "Miejsca musza byc dodatnie"

    if miejsce:
        if miejsce[0] > rzedy or miejsce[0] <= 0 or miejsce[1] > miejsca or miejsce[1] <= 0:
            return "Podane miejsce jest poza sala"

    if preferowane:
        for x in preferowane:
            if x[0] > rzedy or x[0] <= 0 or x[1] > miejsca or x[1] <= 0:
                return "Podane preferowane miejsce jest poza sala"

    # sprawdza, czy argument "miejsce" został podany
    if miejsce:
        if miejsce in zajete:
            return None
        else:
            zajete.add(miejsce)
            return miejsce

    if preferowane:
        dostepne_preferowane = []

        for m in preferowane:
            if m not in zajete:
                dostepne_preferowane.append(m)

        if len(dostepne_preferowane) > 0:
            wylosowany_index = random.randint(0, len(dostepne_preferowane) - 1)
            wylosowane_miejsce = dostepne_preferowane[wylosowany_index]

            zajete.add(wylosowane_miejsce)
            return wylosowane_miejsce
        else:
            # gdy żadne z preferowanych miejsc nie jest wolne zwracamy False
            return False

    # gdy nie podano miejsca ani preferowanych miejsc losujemy dowolne niezajęte miejsce
    wolne_miejsca = []

    for r in range(1, rzedy + 1):
        for m in range(1, miejsca + 1):
            krotka = (r, m) # tak jak w "zajete" jest (1, 1)

            if krotka not in zajete:
                wolne_miejsca.append(krotka)

    if len(wolne_miejsca) > 0:
        wylosowany_index = random.randint(0, len(wolne_miejsca) - 1)
        wylosowane_miejsce = wolne_miejsca[wylosowany_index]

        zajete.add(wylosowane_miejsce)
        return wylosowane_miejsce
    else:
        return False

zajete = {(1, 1), (5, 10)}

print(rezerwuj(zajete, miejsce=(5, 10)))
print(rezerwuj(zajete, miejsce=(5, 11)))
print(rezerwuj(zajete, preferowane=[(1, 1), (7, 3), (7, 4)]))
print(rezerwuj(zajete, preferowane=[(1, 1), (5, 10)]))
print(rezerwuj(zajete))
print(rezerwuj(zajete, miejsce=(30, 5)))