import string


def sprawdz_haslo(haslo):
    def zawiera(znaki):
        # return any(char in znaki for char in haslo)
        for char in haslo:
            if char in znaki:
                return True
        return False

    niespelnione_wymagania = []

    if len(haslo) < 8:
        niespelnione_wymagania.append("za krotkie")

    if not zawiera(string.digits):
        niespelnione_wymagania.append("brak cyfry")

    if not zawiera(string.ascii_uppercase):
        niespelnione_wymagania.append("brak wielkiej litery")

    if not zawiera("!@#$%"):
        niespelnione_wymagania.append("brak znaku specjalnego")

    return niespelnione_wymagania

haslo = input("Podaj haslo: ")

niespelnione_wymagania = sprawdz_haslo(haslo)

if len(niespelnione_wymagania) == 0:
    print("Haslo jest bezpieczne")
else:
    print(f"Problemy: {", ".join(niespelnione_wymagania)}")