from ksiazka import Ksiazka

k = Ksiazka("Lalka", "B. Prus")
print(k.wypozycz(), k.wypozycz(), k.opis())

k2 = Ksiazka("Zbrodnia i kara", "F. Dostojewski")
print(k2.zwroc(), k2.wypozycz(), k2.zwroc(), k2.opis())