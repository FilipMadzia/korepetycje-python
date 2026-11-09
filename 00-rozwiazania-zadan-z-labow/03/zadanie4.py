liczby = []

while True:
    user_input = input("Podaj liczbe lub wpisz koniec: ")

    if user_input == "koniec":
        break
    else:
        liczby.append(int(user_input))

suma = 0

for liczba in liczby:
    suma += liczba

print(f"Liczba: {len(liczby)}, suma: {suma}, srednia: {suma / len(liczby)}, minimum: {min(liczby)}, maximum: {max(liczby)}")