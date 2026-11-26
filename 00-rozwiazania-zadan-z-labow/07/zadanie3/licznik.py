class Licznik:
    def __init__(self, wartosc_poczatkowa = 0):
        self.wartosc_poczatkowa = wartosc_poczatkowa
        self.wartosc = wartosc_poczatkowa

    def zwieksz(self, krok = 1):
        self.wartosc += krok

    def zmniejsz(self, krok = 1):
        self.wartosc -= krok

        if self.wartosc < 0:
            self.wartosc = 0

    def pokaz(self):
        print(self.wartosc)

    def resetuj(self):
        self.wartosc = self.wartosc_poczatkowa