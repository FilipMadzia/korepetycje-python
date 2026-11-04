a = float(input("Podaj czesc rzeczywista liczby z1: "))
b = float(input("Podaj czesc urojona liczby z1: "))
c = float(input("Podaj czesc rzeczywista liczby z2: "))
d = float(input("Podaj czesc urojona liczby z2: "))

z1 = complex(a, b)
z2 = complex(c, d)

suma = z1 + z2
roznica = z1 - z2
iloczyn = z1 * z2
iloraz = z1 / z2
modulz1 = abs(z1)
sprzezenie = z1.conjugate()
kwadrat = z1 ** 2

print(f"Suma: {str(suma).replace('j', 'i')}")
print(f"Różnica: {str(roznica).replace('j', 'i')}")
print(f"Iloczyn: {str(iloczyn).replace('j', 'i')}")
print(f"Iloraz: {str(iloraz).replace('j', 'i')}")
print(f"Moduł z1: {modulz1}")
print(f"Sprzężenie z1: {str(sprzezenie).replace('j', 'i')}")
print(f"Kwadrat z1: {str(kwadrat).replace('j', 'i')}")