class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2 * self.a + 2 * self.b

    def czy_kwadrat(self):
        if self.a == self.b:
            return True
        else:
            return False
        # krótszy i schludniejszy zapis
        # return self.a == self.b

    def skaluj(self, k):
        self.a *= k
        self.b *= k