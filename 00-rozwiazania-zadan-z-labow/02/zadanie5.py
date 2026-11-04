c = 3e5
sekund_w_roku = 365 * 24 * 60 * 60
rok_swietlny_km = c * sekund_w_roku

odleglosc_km = float(input("Podaj odleglosc gwiazdy w latach swietlnych: ")) * rok_swietlny_km

predkosc_sondy = 6.1e4
czas_godz = odleglosc_km / predkosc_sondy
dni = int(czas_godz // 24)
lat = dni // 365
pozostalych_dni = dni % 365

print(f"Odleglosc: {odleglosc_km:.2e} km")
print(f"Czas lotu w h: {czas_godz:.2e} h")
print(f"Czas lotu w dniach: {dni:.2e} dni")
print(f"Czas lotu w latach: {lat:.2e} lat i {pozostalych_dni} pozostalych dni")