def ocenzuruj(zdanie, zakazane_slowa):
    slowa = zdanie.split(" ")
    nowe_zdanie_tablica = []

    for slowo in slowa:
        if slowo.lower() not in zakazane_slowa:
            nowe_zdanie_tablica.append(slowo)
        else:
            nowe_zdanie_tablica.append("CENZURA")

    nowe_zdanie = " ".join(nowe_zdanie_tablica)

    return nowe_zdanie

print(ocenzuruj("Uwielbiam Koty i moim ulubionym kotem jest kot domowy", ["koty", "kotem", "kot"]))