# Zadanie 1

Napisz program obliczający koszt podróży samochodem oraz wystawiający krótkie podsumowanie.

Wczytaj od użytkownika:
- dystans w kilometrach
- średnie spalanie auta w litrach na 100 km
- cenę jednego litra paliwa
- liczbę pasażerów

Oblicz:
- łączną ilość zużytego paliwa
- całkowity koszt przejazdu
- koszt przypadający na jedną osobę

Wszystkie kwoty i ilości paliwa wyświetl z dokładnością do dwóch miejsc po przecinku za pomocą f-stringów.

Wynik programu powinien wyglądać następująco

```
Podaj dystans w km: 1000
Podaj srednie spalanie na 100 km: 6.5
Podaj cene litru paliwa: 5.9
Podaj ilość pasażerów: 3
===============
Koszt podrozy
===============
Zuzyte paliwo: 65.00 l
Calkowity koszt przejazdu: 382.50 zl
Koszt na osobe: 127.83 zl
```

### Dla chętnych

Dodaj walidację danych: gdy użytkownik poda liczbę niedodatnią wyświetl błąd i poproś o ponowne wprowadzenie

# Zadanie 2
Napisz program dekodujący podstawowe informacje z numeru PESEL (zakładamy poprawny, 11-znakowy ciąg cyfr).

Wczytaj numer PESEL jako tekst, usuwając ewentualne zbędne spacje po bokach.

Wytnij z tekstu pierwsze 6 znaków oznaczających datę urodzenia oraz dziesiątą cyfrę, która określa płeć.

Na podstawie pierwszych 6 znaków zdekoduj datę urodzenie:
- pierwsze 2 cyfry przypisz do roku
- kolejne 2 do miesiąca
- ostatnie 2 do dnia
- gdy miesiąc mieści się w zakresie [21, 32]:
    - od miesiąca odejmij 20
    - do roku dodaj 2000
- w przeciwnym wypadku do roku dodaj 1900

Zamień wyciętą cyfrę płci na liczbę całkowitą i sprawdź, czy jest parzysta (oznacza kobietę) czy nieparzysta (oznacza mężczyznę).

```
Podaj nr PESEL: 71010751747
Data urodzenia: 7.1.1971
Plec: kobieta
```

### Dla chętnych

Wyświel dzień i miesiąc w formacie DD.MM. Gdy są liczbami jednocyfrowymi przed nimi powinno się znaleźć 0.

Przykład

```
Podaj nr PESEL: 71010751747
Data urodzenia: 07.01.1971
Plec: kobieta
```

# Zadanie 3

Napisz prosty system obsługi koszyka w sklepie warzywnym.

Utwórz słownik przechowujący cennik 4 wybranych produktów (kluczem jest nazwa produktu małymi literami, a wartością cena za kilogram).

Wyświetl dostępne produkty i ich ceny.

W pętli pytaj użytkownika o nazwę produktu, który chce kupić, dopóki nie wpisze słowa "koniec". Wielkość liter wpisywanych przez klienta nie powinna mieć znaczenia.

Jeśli produkt znajduje się w cenniku, zapytaj o wagę w kilogramach i dolicz koszt do sumy zamówienia. Wyświetl ile doliczono do sumy

Jeśli produktu nie ma w sklepie wyświetl komunikat o braku towaru.

Po zakończeniu zakupów wyświetl łączną kwotę do zapłaty z dwoma miejscami po przecinku. 

Przykład

```
Cennik
jablka: 4.99 zl/kg
banany: 5.49 zl/kg
ziemniaki: 0.99 zl/kg
marchewki: 1.99 zl/kg
Podaj ktory produkt chcesz kupic: ziemniaki
Podaj ile kg chcesz: 2
2.0 kg * 0.99 zl/kg = 1.98 zl
Podaj ktory produkt chcesz kupic: banany
Podaj ile kg chcesz: 1
1.0 kg * 5.49 zl/kg = 5.49 zl
Podaj ktory produkt chcesz kupic: maslo
Brak takiego produktu
Podaj ktory produkt chcesz kupic: koniec
Laczna kwota do zaplaty: 7.47 zl
```

### Dla chętnych

Popraw wygląd interfejsu wedle uznania aby był bardziej czytelny np. poprzez przerwy między linijkami