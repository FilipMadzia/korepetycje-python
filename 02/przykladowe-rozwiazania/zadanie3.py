def zamien_polskie_znaki(tekst):
    tekst = tekst.replace("ą", "a")
    tekst = tekst.replace("Ą", "A")
    tekst = tekst.replace("ć", "c")
    tekst = tekst.replace("Ć", "C")
    tekst = tekst.replace("ę", "e")
    tekst = tekst.replace("Ę", "E")
    tekst = tekst.replace("ł", "l")
    tekst = tekst.replace("Ł", "L")
    tekst = tekst.replace("ń", "n")
    tekst = tekst.replace("Ń", "N")
    tekst = tekst.replace("ó", "o")
    tekst = tekst.replace("Ó", "O")
    tekst = tekst.replace("ś", "s")
    tekst = tekst.replace("Ś", "S")
    tekst = tekst.replace("ź", "z")
    tekst = tekst.replace("Ź", "Z")
    tekst = tekst.replace("ż", "z")
    tekst = tekst.replace("Ż", "Z")

    return tekst

    # alternatywnie
    # mapa_znakow = str.maketrans(
    #     "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ",
    #     "acelnoszzACELNOSZZ"
    # )
    # return tekst.translate(mapa_znakow)

print(zamien_polskie_znaki("Nazywam się Cezary Baryka i od 20 minut jestem właścicielem tego oto szklanego domu"))
print(zamien_polskie_znaki("Źdźbło"))