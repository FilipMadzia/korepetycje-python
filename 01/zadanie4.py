liczby = [] # [4, -2, 10]

while True:
    wejscie = input("Podaj liczbe lub wpisz koniec: ")

    if wejscie == "koniec":
        break

    liczby.append(int(wejscie))

ilosc = len(liczby) # length zwraca ilosc elementow
print(ilosc)

suma = 0

for liczba in liczby:
    suma = suma + liczba
