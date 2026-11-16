# Zadanie 1

Napisz funkcję *ocenzuruj*, która przyjmuje tekst oraz listę "słów zakazanych". Funkcja ma zwracać ocenzurowany tekst, w którym każde "zakazane słowo" zostało zamienione na "CENZURA". Wielkość znaków nie powinna mieć znaczenia

### Przykład

```py
print(ocenzuruj("Uwielbiam Koty i moim ulubionym kotem jest kot domowy", ["koty", "kotem", "kot"]))
```

Wynik

```
Uwielbiam CENZURA i moim ulubionym CENZURA jest CENZURA domowy
```

# Zadanie 2

Napisz prosty kalkulator.

1. Wczytaj pierwszą liczbę
2. Wczytaj drugą liczbę
3. Wczytaj operację (+, -, *, /). Gdy użytkownik poda inny znak poproś go ponownie
4. W zależności od wybranej operacji wykonaj odpowiednie działania i wyświetl wynik w formacie liczba1 operacja liczba2 = wynik

### Przykład

```
Podaj liczbe 1: 3
Podaj liczbe 2: 5
Podaj operacje: test
Nieprawidlowa operacja. Sprobuj ponownie
Podaj operacje: *
3 * 5 = 15
```

# Zadanie 3

Napisz funkcję *zamien_polskie_znaki*, która przyjmuje tekst i zwraca go z zamienionymi polskimi znakami na ich angielskie odpowiedniki. Zachowaj wielkość znaków

### Przykład

```py
print(zamien_polskie_znaki("Nazywam się Cezary Baryka i od 20 minut jestem właścicielem tego oto szklanego domu"))
print(zamien_polskie_znaki("Źdźbło"))
```

Wynik

```
Nazywam sie Cezary Baryka i od 20 minut jestem wlascicielem tego oto szklanego domu
Zdzblo
```