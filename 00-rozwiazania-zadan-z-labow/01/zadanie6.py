ilosc_kaw = int(input("Podaj ilosc kaw: "))
cena_kawy = 12
koszt_kaw = ilosc_kaw * cena_kawy
sup = 0.25
suma_sup = ilosc_kaw * sup
napiwek = abs(float(input("Podaj wysokosc napiwku: ")))

do_zaplaty = koszt_kaw + suma_sup + napiwek

print("*" * 30)
# RACHUNEK ma 8 znaków, więc 30 - 8 = 22, a 22 / 2 = 11, więc dodajemy 11 spacji z lewej (z prawej nie musimy, bo i tak są niewidoczne)
print(" " * 11, "RACHUNEK")
print("*" * 30)
print(f"Liczba kaw: {ilosc_kaw}")
print(f"Cena jednej kawy: {cena_kawy:.2f} zl")
print(f"Koszt kaw: {koszt_kaw:.2f} zl")
print(f"Oplata SUP: {suma_sup:.2f} zl")
print(f"Napiwek: {napiwek:.2f} zl")
print("*" * 30)
print(f"DO ZAPLATY: {do_zaplaty:.2f} zl")
print("*" * 30)