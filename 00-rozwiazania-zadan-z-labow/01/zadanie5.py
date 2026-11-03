ilosc_kaw = int(input("Podaj ilosc kaw: "))
cena_kawy = 12
sup = 0.25

do_zaplaty = ilosc_kaw * cena_kawy + ilosc_kaw * sup
print(f"Do zaplaty: {do_zaplaty:.2f} zl")

napiwek = abs(float(input("Podaj wysokosc napiwku: ")))

print(f"Do zaplaty z napiwkiem: {(do_zaplaty + napiwek):.2f} zl")