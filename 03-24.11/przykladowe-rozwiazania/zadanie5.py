def lista_ocen(tekst):
    oceny_stringowo = tekst.split(", ")
    oceny_liczbowo = []

    for ocena_string in oceny_stringowo:
        ocena = float(ocena_string)
        oceny_liczbowo.append(ocena)

    return oceny_liczbowo

def podsumowanie(lista_ocen):
    suma = sum(lista_ocen)
    ilosc_ocen = len(lista_ocen)

    if ilosc_ocen == 0:
        return 0, 0, 0

    srednia = suma / ilosc_ocen

    najnizsza = min(lista_ocen)
    najwyzsza = max(lista_ocen)

    return srednia, najnizsza, najwyzsza

oceny_string = input("Podaj oceny oddzielone przecinkiem i spacja: ")
oceny = lista_ocen(oceny_string)

sr, najn, najw = podsumowanie(oceny)

print(f"Srednia: {sr}, najnizsza: {najn}, najwyzsza: {najw}")

if sr >= 3.0:
    print("Przedmiot zaliczony")
else:
    print("Przedmiot niezaliczony")