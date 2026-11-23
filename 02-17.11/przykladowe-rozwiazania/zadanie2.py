liczba1 = int(input("Podaj liczbe 1: "))
liczba2 = int(input("Podaj liczbe 2: "))

dozwolone_operacje = ["+", "-", "*", "/"]

operacja = input("Podaj operacje: ")

while operacja not in dozwolone_operacje:
    operacja = input("Podaj operacje: ")

    if operacja not in dozwolone_operacje:
        print("Nieprawidlowa operacja. Sprobuj ponownie")

wynik = 0

if operacja == "+":
    wynik = liczba1 + liczba2
elif operacja == "-":
    wynik = liczba1 - liczba2
elif operacja == "*":
    wynik = liczba1 * liczba2
elif operacja == "/":
    # w przypadku, gdy liczba2 będzie równa 0 wyskoczy błąd, jak go uniknąć?
    wynik = liczba1 / liczba2

print(f"{liczba1} {operacja} {liczba2} = {wynik}")