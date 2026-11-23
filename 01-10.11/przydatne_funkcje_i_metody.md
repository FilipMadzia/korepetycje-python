# Podstawowe

```py
print(argument) # wyświetla w konsoli
print(argument1, argument2) # wyświetla oba argumenty "sklejone"
print(argument1, argument2, sep=", ") # oddziela argumenty przecinkiem i spacją
print(argument, end="") # nie daje "entera" na końcu

tekst = input() # wczytuje co wpisał użytkownik i zapisuje do zmiennej w postaci tekstu
tekst2 = input(argument) # analogicznie ale najpierw wyświetla podany argument

liczba_calkowita = int(argument) # zamienia tekst lub float-a na int-a
liczba_zmiennoprzecinkowa = float(argument) # zamienia tekst lub int-a na float-a
tekst = str(argument) # "str" od "string", zamienia liczbę na tekst
```

# Listy

```py
len(lista) # zwraca ilość elementów wewnątrz listy
lista.append(element) # dodaje element na koniec listy o nazwie "lista"
lista.insert(index, element) # dodaje element na miejsce podanego indexu
lista.pop() # usuwa ostatni element
lista.pop(index) # usuwa element o podanym indexie
lista.remove(element) # usuwa TYLKO pierwsze wystąpienie podanego elementu
lista.reverse() # odwraca kolejność elementów
```