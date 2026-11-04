imie_i_nazwisko = input("Podaj swoje imie i nazwisko: ")
imie_i_nazwisko = imie_i_nazwisko.strip()
imie_i_nazwisko = imie_i_nazwisko.upper()

print(imie_i_nazwisko)

email = input("Podaj swoj email: ")
ile_znakow_at = email.count('@')
print(f"Ile znakow @ w emailu: {ile_znakow_at}")

nr_telefonu = input("Podaj swoj numer telefonu: ")
nowy_nr_telefonu = nr_telefonu.replace(" ", "").replace("-", "")
print(nowy_nr_telefonu)

for char in nowy_nr_telefonu:
    if not char.isdigit():
        print("W nr telefonu nie ma samych cyfr")
        break