def ocena(punkty):
    if punkty >= 0 and punkty <= 40:
        return 2.0
    if punkty >= 41 and punkty <= 55:
        return 3.0
    if punkty >= 56 and punkty <= 70:
        return 3.5
    if punkty >= 71 and punkty <= 80:
        return 4.0
    if punkty >= 81 and punkty <= 90:
        return 4.5
    if punkty >= 91 and punkty <= 100:
        return 5.0

    # przypadku, gdy podana ilosc pkt. jest spoza zakresu 0-100
    return -1

print(ocena(32))
print(ocena(80))
print(ocena(100))