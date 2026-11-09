def podziel(lista):
    parzyste = []
    nieparzyste = []

    for i in lista:
        if i % 2 == 0:
            parzyste.append(i)
        else:
            nieparzyste.append(i)
    
    return parzyste, nieparzyste

lista = range(1, 11)

parzyste, nieparzyste = podziel(lista)

print(parzyste, len(parzyste))
print(nieparzyste, len(nieparzyste))