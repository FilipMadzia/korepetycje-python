def czy_trojkat_istnieje(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            return True

    return False

def wyswietl_typ_trojkata(a, b, c):
    if a == b and b == c:
        print("Rownoboczny")
    elif a == b or a == c or b == c:
        print("Rownoramienny")
    else:
        print("Roznoboczny")

a = int(input("Podaj dlugosc boku a: "))
b = int(input("Podaj dlugosc boku b: "))
c = int(input("Podaj dlugosc boku c: "))

czy_isnieje = czy_trojkat_istnieje(a, b, c)

if czy_isnieje:
    wyswietl_typ_trojkata(a, b, c)
else:
    print("Trojkat nie istnieje")