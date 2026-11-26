from ksiazka import Ksiazka

class Biblioteka:
    def __init__(self):
        self.ksiazki = []

    def dodaj(self, ksiazka):
        self.ksiazki.append(ksiazka)

    def znajdz(self, tytul):
        for ksiazka in self.ksiazki:
            if ksiazka.tytul == tytul:
                return ksiazka
        # jeśli doszliśmy do tego miejsca w programie to znaczy, że nie znaleziono książki
        return None

    def wypozycz(self, tytul):
        ksiazka = self.znajdz(tytul)

        if ksiazka != None: # albo tylko    if ksiazka:
            return ksiazka.wypozycz()
        else:
            return False

    def zwroc(self, tytul):
        ksiazka = self.znajdz(tytul)

        if ksiazka != None:
            return ksiazka.zwroc()
        else:
            return False

    def dostepne(self):
        for ksiazka in self.ksiazki:
            if not ksiazka.wypozyczona:
                print(ksiazka.opis())