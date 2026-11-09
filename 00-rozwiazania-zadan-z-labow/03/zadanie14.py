def licz_slowa(text):
    slownik = {}

    text = text.lower()

    slowa = text.split()

    for slowo in slowa:
        slownik[slowo] = 0
    for slowo in slowa:
        slownik[slowo] = slownik[slowo] + 1
    
    return slownik

def najczestsze(slownik: dict):
    keys = list(slownik.keys())
    najwieksza = slownik[keys[0]]
    najwiekszy_index = 0

    for i in range(len(keys)):
        if slownik[keys[i]] > najwieksza:
            najwieksza = slownik[keys[i]]
            najwiekszy_index = i

    return keys[najwiekszy_index]

slownik = licz_slowa("kot skoczyl i kot zjadl i bylo ciemno i zimno")

print(slownik)
print(najczestsze(slownik))