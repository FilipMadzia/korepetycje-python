[Jak czytać kod Python - prezentacja](https://docs.google.com/presentation/d/1tUdkb3t-uPTPWnd-zdjbp6pNon1WbZ5MAyQEG0DWCd0/edit?usp=sharing)

[Operacje na zmiennych - prezentacja](https://docs.google.com/presentation/d/1wY3r7DJ23NscZ8FA0mwBcwoioAbelIF6AZ0cQGtFUgA/edit?usp=sharing)

[Tutorial na YT](https://youtu.be/kqtD5dpn9C8?t=330)

# String (tekst) formatowany

String formatowany służy do łatwiejszego łączenia zmiennych z tekstem. Tworzymy go poprzedzając cudzysłów literką "f" a wewnątrz niego możemy używać zmiennych za pomocą nawiasów klamrowych {nazwa_zmiennej}. Zamiast:

```py
imie = "Nastazja"
wiek = 23

tekst = "Nazywasz się " + imie + " i masz " + wiek + " lata."
```

możemy użyć stringa formatowanego

```py
tekst_formatowany = f"Nazywasz się {imie} i masz {wiek} lata."
```

Używamy go dla ułatwienia sobie życia, korzystanie z niego nie jest wymagane (no chyba że w treści zadania jest taki wymóg)

# Funkcja print() i input()

## print()

print() przyjmuje co najmniej jeden argument i wyświetla go w konsoli wraz z "enterem" na końcu

```py
print("Hello world")
print(12)
```

wynik

```
Hello world
12
```

### end="" i sep=""
end="" i sep="" modyfikują działanie funkcji print(). Muszą być ostatnimi argumentami funkcji


Argument end="" mówi funkcji print() co ma się znaleźć na końcu wyświetlonego tekstu. Domyślnie jest to znak nowej linii \n

```py
print("Welcome") <=> print("Welcome", end="\n")
```

```py
print("Czekaj", end="...")
print("Gotowy")
```

wynik

```
Czekaj...Gotowy
```

Argument sep="" mówi funkcji print() czym mają być rozdzielone poszczególne argumenty do wyświetlenia. Domyślnie jest to pusty string: ""

```py
imie = "Rodion"

print("Witaj", imie, "w moim domu", sep=" ")
```

wynik

```
Witaj Rodion w moim domu

# bez sep=" " wynik byłby:
# WitajRodionw moim domu
```

Warto zauważyć, że bez sep=" " tekst jest sklejony TYLKO pomiędzy poszczególnymi argumentami funkcji, spacje wewnątrz stringa "w moim domu" pozostały bez zmian

end="" i sep="" można używać jednocześnie. Muszą być ostatnimi argumentami ale kolejność między nimi nie ma znaczenia

```py
imie = "Agłaja"
wiek = 21
print("Nazywasz się", imie, "i masz", wiek, "lat", end="!", sep=" ")
```

wynik

```
Nazywasz się Agłaja i masz 21 lat!
```

## input()

Funkcja input() czyta, co użytkownik wpisał do konsoli i gdy kliknie "enter" zapisuje tekst do zmiennej. Funkcja zawsze zwraca tekst, więc w przypadku zmiennych liczbowych należy pamiętać o int() lub float()

```py
print("Podaj imie")
imie = input()
print("Witaj, ", imie)
```

wynik (znak ">" oznacza, że jest to tekst wpisany przez użytkownika. Zapis wymyślony przeze mnie by było wiadomo że to coś wpisane przez użytkownika, normalnie w konsoli nic nie jest wyświetlane)

```
Podaj imie
>Eugeniusz
Witaj, Eugeniusz
```

```py
print("Podaj swoj wiek")
wiek = int(input())
print(f"Masz {wiek} lat")
```

wynik

```
Podaj swoj wiek
>20
Masz 20 lat
```

Do funkcji input() możemy podać jako argument tekst do wyświetlenia. Działa to jak print() bez "entera" na końcu

```py
ulubione_zwierze = input("Podaj swoje ulubione zwierze: ")
print(f"Twoim ulubionym zwierzeciem jest {ulubione_zwierze}")
```

wynik

```
Podaj swoje ulubione zwierze: >kot
Twoim ulubionym zwierzeciem jest kot
```

# Zamiana typów danych

Gdy chcemy zamienić daną typu tekstowego na liczbową możemy skorzystać z jednej z dwóch funkcji: int() albo float(). W rezultacie otrzymamy do zmiennej liczbę

```py
tekst = "12"
liczba_calkowita = int(tekst) # 12
liczba_zmiennoprzecinkowa = float(tekst) # 12.0
```

Możemy również w drugą stronę zamieniać zmienne liczbowe na tekst

```py
liczba = 10.3
tekst = str(liczba) # "10.3"
```

Albo z liczby całkowitej zrobić zmiennoprzecinkową i na odwrót. W przypadku zamiany na liczbę całkowitą stracimy część po przecinku, zostanie ona zupełnie "odcięta"

```py
calkowita = 3
zmiennoprzecinkowa = float(calkowita) # 3.0

zmiennoprzecinkowa2 = 3.14
calkowita2 = int(zmiennoprzecinkowa) # 3
```

# Instrukcja warunkowa if, elif i else

## if

Instrukcje warunkowe pozwalają nam na wykonywanie części kodu tylko gdy zostanie spełniony dany warunek

```py
wiek = input("Podaj swoj wiek: ")

if wiek >= 18:
    print("Mozesz wejsc do klubu")
```

Po słowie kluczowym "if" podajemy warunek, który będzie sprawdzany i kończymy linię dwukropkiem. Instrukcje "wewnątrz" if-a zostaną wykonane tylko, gdy warunek zostanie spełniony

## else

Instrukcji warunkowej else można używać tylko razem z instrukcją if i służy do określania działania w przypadku niespełnienia warunku

```py
saldo = 10
cena = 100

if saldo >= cena:
    print("Mozesz kupic ten przedmiot")
else:
    print("Nie mozesz kupic tego przedmioty, brak wystarczajacych srodkow")
```

## elif

Sklejenie słów "else if" używane poy if-ie do określania alternatyw

```py
ksztalt = input("Podaj ksztalt: ")

if imie == "kwadrat":
    #cos sie dzieje
elif imie == "kolo":
    #cos innego sie dzieje
elif imie == "trojkat":
    # jeszcze cos innego sie dzieje
else:
    # w przypadku, gdy zaden poprzedni warunek nie zostal spelniony zostanie wykonany kod wewnatrz else-a np.
    print("Blad: nie znaleziono takiego ksztaltu")
```

Warto pamiętać, że else po elif-ie nie jest obowiązkowy, lecz gdy go używamy to musi być na końcu. Bez else-a jeśli żaden z warunków nie zostanie spełniony Python przejdzie do kolejnej instrukcji w kodzie

# Tablice (listy)

Lista w Pythonie jest zmienną mogącą przechować wiele danych tego samego typu. Np. lista wszystkich miast na Śląsku, lista liczba parzystych do 100. Tworzymy ją z użyciem kwadratowych nawiasów

```py
owoce = [] # pusta lista niewiadomego typu
zwierzeta = ["papuga"] # lista stringów zawierająca jeden element
parzyste = [0, 2, 4, 6] # lista liczb całkowitych
```

## Indexy

Każdy element w tablicy ma index (identyfikator) po którym można się do niego odwołać. Index zaczyna się od 0

```py
owoce = ["jablko", "gruszka", "banan"]
        #   0          1         2

print(owoce[1])
print(owoce[-1]) # owoce[-1] zwroci ostatni element, owoce[-2] przedostatni itd.
```

wynik

```
gruszka
banan
```

## Modyfikacja

Poszczególne elementy możemy zmieniać w następujący sposób

```py
imiona = ["Agłaja", "Awdotia", "Aleksandra"]

imiona[0] = "Sonia"

print(imiona)
```

wynik

```
["Sonia", "Awdotia", "Aleksandra"]
```

## Dodawanie

Do listy dodajemy elementy za pomocą metody (coś jak funkcja) .append(element). Element zostanie dodany na końcu

```py
liczby = [1, 2, 3, 4]
liczby.append(-12)

print(liczby)
```

wynik

```
[1, 2, 3, 4, -12]
```

Aby dodać element w dowolnym miejscu używamy metody .insert(index, element)

```py
kawy = ["latte", "cappucino", "czarna"]
kawy.insert(1, "Pumpkin spice latte")

print(kawy)
```

wynik

```
["latte", "Pumpkin spice latte", "cappucino", "czarna"]
```

Element zostanie dodany w miejscu podanego index a reszta elementów "przesunie się" o 1 w prawo

## Usuwanie

### Po wartości

Metoda .remove(element) usuwa pierwsze wystąpienie podanego elementu

```py
liczby_pierwsze = [2, 3, 5, 7, 3]
liczby_pierwsze.remove(3)

print(liczby_pierwsze)
```

wynik


```
[2, 5, 7, 3]
```

Warto zauważyć, że usunięta została tylko pierwsza trójka

### Po indexie

Gdy znamy index elementu, który chcemy usunąć używamy metody .pop(index)

```py
warzywa = ["ziemniak", "cebula", "marchew"]
warzywa.pop(0)

print(warzywa)
```

wynik

```
["cebula", "marchew"]
```

Bez podania indexu metoda .pop() usunie ostatni element listy

## Odwracanie kolejności

Aby odwrócić kolejność listy używamy metody .reverse()

```py
binarna = [0, 1, 0, 1, 1, 1]
binarna.reverse()

print(binarna)
```

wynik

```
[1, 1, 1, 0, 1, 0]
```

## Odczytywanie ilości elementów

Funkcja len() zwraca ilość elementów wewnątrz listy w momencie w którym jest użyty len()

```py
owoce = ["jablko", "banan"]
x = len(owoce) # 2

owoce.append("gruszka")
y = len(owoce) # 3
```

# Pętle

## Pętla for

Pętla for służy do wykonania danego zestawu instrukcji określoną ilość razy albo dla każdego elementu listy

### Pętla for po liczbach

```py
for i in range(10): # range(10) oznacza przedział liczb całkowitych [0, 10)
    print(i, end=", ")
```

wynik

```
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

Przedział i skok możemy określić bardziej dokładnie

```py
for i in range(5, 10, 2): # range(od, do, skok)
    print(i, end=", ")
```

wynik

```
5, 7, 9
```

### Pętla for po elementach listy

```py
obiady = ["schabowy", "rosół", "spaghetti"]

for obiad in obiady: # dla każdego elementu listy "obiady" wykonaj instrukcję
    print(obiad)
```

wynik

```
schabowy
rosół
spaghetti
```

## Pętla while

Pętli while używamy, gdy nie znamy ilości operacji, które chcemy wykonać np. chcemy wczytywać od użytkownika liczbę dopóki nie napisze "koniec" albo chcemy dzielić daną liczbę przez 2 dopóki nie będzie równa 1

```py
liczba = 8
ilosc_iteracji = 0
while liczba > 1:
    liczba = liczba / 2
    ilosc_iteracji = ilosc_iteracji + 1
    print(liczba)

print(f"Ilosc iteracji: {ilosc_iteracji}")
```

wynik

```
4.0 # przy dzieleniu Python automatycznie zapisuje liczbę jako zmiennoprzecinkową
2.0
1.0
Ilosc iteracji: 3
```

### Instrukcje break i continue

Instrukcji tych można używać w przypadku obu typów pętli

Instrukcja break natychmiast przerywa pętlę i przechodzi do następnych linijek kodu

```py
for i in range(10):
    if i == 4:
        break

    print(i)

print("Kolejna instrukcja w kodzie")
```

wynik

```
0
1
2
3
Kolejna instrukcja w kodzie
```

Instrukcja continue przerywa obecną iterację pętli i przechodzi do następnej

```py
for i in range(10):
    if i == 4:
        continue

    print(i)

print("Kolejna instrukcja w kodzie")
```

wynik

```
0
1
2
3
5 # Gdy i było równe 4 przeszliśmy do kolejnej iteracji więc 4 nie zostało wyświetlone
6
7
8
9
Kolejna instrukcja w kodzie
```

Analogicznie działają w przypadku pętli while

```py
imiona = []
while True:
    imie = input("Podaj imie: ")

    if imie == "koniec":
        break

print(imiona)
```

wynik

```
Podaj imie: >Damian
Podaj imie: >Tadek
Podaj imie: >Krzysiek
Podaj imie: >koniec
["Damian", "Tadek", "Krzysiek"]
```