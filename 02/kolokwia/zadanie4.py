def zamien_polski_znak(znak):
    if znak == "ą":
        return "a"
    elif znak == "ć":
        return "c"
    elif znak == "ę":
        return "e"
    elif znak == "ó":
        return "o"
    elif znak == "ł":
        return "l"
    elif znak == "ż" or znak == "ź":
        return "z"
    elif znak == "ś":
        return "s"
    elif znak == "ń":
        return "n"
    else:
        return znak

def liczba_przeznaczenia(imie_i_nazwisko):
    imie_i_nazwisko = imie_i_nazwisko.lower()
    suma = 0

    nowe_imie_i_nazwisko = ""

    for c in imie_i_nazwisko:
        nowe_imie_i_nazwisko += zamien_polski_znak(c)

    for c in nowe_imie_i_nazwisko:
        if c in " -":
            continue
        
        if c == 'a' or c == 'j' or c == 's':
            suma += 1
        elif c == 'b' or c == 'k' or c == 't':
            suma += 2
        elif c == 'c' or c == 'l' or c == 'u':
            suma += 3
        elif c == 'd' or c == 'm' or c == 'v':
            suma += 4
        elif c == 'e' or c == 'n' or c == 'w':
            suma += 5
        elif c == 'f' or c == 'o' or c == 'x':
            suma += 6
        elif c == 'g' or c == 'p' or c == 'y':
            suma += 7
        elif c == 'h' or c == 'q' or c == 'z':
            suma += 8
        elif c == 'i' or c == 'r':
            suma += 9

    if suma >= 10 and suma != 11 and suma != 22 and suma != 33:
        nowa_suma = 0
        tmp = str(suma)

        for c in tmp:
            nowa_suma += int(c)
        
        return nowa_suma

    return suma

print(liczba_przeznaczenia("Kr-yśtyna Ńowak"))
print(liczba_przeznaczenia("Anna Kowalska"))