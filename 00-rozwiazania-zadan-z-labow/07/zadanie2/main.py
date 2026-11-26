from prostokat import Prostokat

p1 = Prostokat(3, 4)
print(p1.pole(), p1.obwod(), p1.czy_kwadrat())

p2 = Prostokat(10, 10)
print(p2.pole(), p2.obwod(), p2.czy_kwadrat())

p2.skaluj(2)
print(p2.pole(), p2.obwod(), p2.czy_kwadrat())
