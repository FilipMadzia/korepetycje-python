def statystyki(lista):
    ilosc_el = len(lista)
    suma = 0
    najmniejszy = lista[0]
    najwiekszy = lista[0]

    for el in lista:
        suma += el

        if el < najmniejszy:
            najmniejszy = el

        if el > najwiekszy:
            najwiekszy = el

    srednia = suma / ilosc_el

    return najmniejszy, najwiekszy, srednia

mini, maks, sr = statystyki([4, -2, 10, 7])

print(f"Minimum: {mini}, maksimum: {maks}, srednia: {sr}")