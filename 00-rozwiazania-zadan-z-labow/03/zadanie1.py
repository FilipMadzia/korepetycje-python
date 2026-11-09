liczba = int(input("Podaj liczbe calkowita: "))

if liczba % 2 == 0:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")

if liczba > 0:
    print("Liczba jest dodatnia")
elif liczba < 0:
    print("Liczba jest ujemna")
else:
    print("Liczba jest rowna 0")