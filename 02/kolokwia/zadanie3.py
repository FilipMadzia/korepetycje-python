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

def login_ucznia(imie, nazwisko, rok_rozpoczecia=2026):
    imie = imie.replace(" ", "")
    imie = imie.lower()

    nowe_imie = ""

    for c in imie:
        nowe_imie += zamien_polski_znak(c)

    nazwisko = nazwisko.replace(" ", "")
    nazwisko = nazwisko.lower()

    nowe_nazwisko = ""

    for c in nazwisko:
        nowe_nazwisko += zamien_polski_znak(c)

    login = nowe_imie[0] + nowe_nazwisko + str(rok_rozpoczecia)[2:4]

    return login

print(login_ucznia("An ną", "Ńowak ", ))