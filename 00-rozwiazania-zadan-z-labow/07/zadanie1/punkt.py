import math


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def wydrukuj_punkt(self):
        print(f"{self.x}, {self.y}")

    def odleglosc(self, p2):
        # ręczne obliczenie ze wzoru
        # return ((self.x - p2.x)**2 + (self.y - p2.y)**2)**0.5

        # użycie metody .dist(punkt1, punkt2) gdzie punkt1 i punkt2 są krotkami (x, y)
        return math.dist((self.x, self.y), (p2.x, p2.y))