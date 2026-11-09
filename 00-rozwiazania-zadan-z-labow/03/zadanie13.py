import string


def szyfruj(text, przesuniecie):
    znaki = list(string.ascii_lowercase)
    rozmiar = len(znaki)

    while przesuniecie > rozmiar:
        przesuniecie -= rozmiar

    zaszyfrowany = ""

    for l in text:
        if l not in znaki:
            zaszyfrowany = zaszyfrowany + l
            continue
        if znaki.index(l) + przesuniecie >= rozmiar:
            zaszyfrowany = zaszyfrowany + znaki[znaki.index(l) + przesuniecie - rozmiar]
        else:
            zaszyfrowany = zaszyfrowany + znaki[znaki.index(l) + przesuniecie]
    
    return zaszyfrowany


text = "hello worldz"
print(text)

text = szyfruj(text, 3)
print(text)

text = szyfruj(text, -3)
print(text)