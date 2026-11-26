from biblioteka import Biblioteka
from ksiazka import Ksiazka

b = Biblioteka()
b.dodaj(Ksiazka("Lalka", "B. Prus"))
b.dodaj(Ksiazka("Zbrodnia i kara", "F. Dostojewski"))
b.dodaj(Ksiazka("Portret Doriana Graya", "O. Wilde"))

print("===Dostepne 1===")
b.dostepne()

print(b.wypozycz("Lalka"))
print(b.wypozycz("Lalka"))
print(b.wypozycz("Emma"))

print("===Dostepne 2===")
b.dostepne()