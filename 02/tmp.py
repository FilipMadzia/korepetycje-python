# zamiana tekstu na tablicę słów

tekst = "Zielony liść spadł z drzewa"
slowa = tekst.split(" ") # dzieli string na podstawie spacji
# ["Zielony", "liść", "spadł", "z", "drzewa"]
print(slowa)

# operator "in" oraz "not in"

if "drzewa" in slowa:
    print('W tekscie jest slowo "drzewa"')

if "kot" not in slowa:
    print('W tekscie nie ma slowa "kot"')

# zamiana stringów

zakupy = ["jablko", "banan", "gruszka"]
tekst = "Lubie jesc jablko i banan" # pokaż działanie w przypadku "banany"

for element in zakupy:
    if element in tekst:
        tekst = tekst.replace(element, "OWOC")

print(tekst)

tekst2 = "Lubie jesc jablko i banany"
slowa = tekst2.split(" ")

nowy_tekst_slowa = []

for slowo in slowa:
    if slowo in zakupy:
        nowy_tekst_slowa.append("OWOC")
    else:
        nowy_tekst_slowa.append(slowo)

nowy_tekst = " ".join(nowy_tekst_slowa)
print(nowy_tekst)

# wyświetlanie argumentów nazwanych
def podpis_zeszytu(przedmiot, imie, nazwisko, klasa="1a", **dodatkowe_informacje):
    print(przedmiot.upper())
    print(f"{imie} {nazwisko}")
    print(klasa)

    for klucz, wartosc in dodatkowe_informacje.items():
        print(f"{klucz}: {wartosc}")

    # for x in dodatkowe_informacje:
    #     print(f"{x}: {dodatkowe_informacje[x]}")

podpis_zeszytu("religia", "Ola", "Nowak", szkola="SP 5")