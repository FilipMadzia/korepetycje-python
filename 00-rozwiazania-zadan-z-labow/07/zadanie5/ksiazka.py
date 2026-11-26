class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor
        self.wypozyczona = False

    def opis(self):
        if self.wypozyczona:
            return f"{self.tytul} - {self.autor} (wypozyczona)"
        else:
            return f"{self.tytul} - {self.autor} (dostepna)"
        # w jednej linii
        # return f"{self.tytul} - {self.autor} ({"wypozyczona" if self.wypozyczona else "dostepna"})"
    
    def wypozycz(self):
        if self.wypozyczona:
            return False
        else:
            self.wypozyczona = True
            return True

    def zwroc(self):
        if self.wypozyczona:
            self.wypozyczona = False
            return True
        else:
            return False