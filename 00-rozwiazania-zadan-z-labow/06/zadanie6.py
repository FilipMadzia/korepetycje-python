import string


def moje_upper(tekst):
    nowy_tekst = ""

    for c in tekst:
        if ord(c) >= 97 and ord(c) <= 97 + 26: # 97 + 26 bo jest 26 liter. Można też od razu podać 123
            nowy_tekst += chr(ord(c) - 32)
        else:
            nowy_tekst += c
        
    return nowy_tekst

# alternatywnie bez korzystania z kodów znaków ASCII
def moje_upper2(tekst):
    maly_alfabet = string.ascii_lowercase

    for litera in maly_alfabet:
        tekst = tekst.replace(litera, litera.capitalize())

    return tekst

def moje_lower(tekst):
    nowy_tekst = ""

    for c in tekst:
        if ord(c) >= 65 and ord(c) <= 65 + 26:
            nowy_tekst += chr(ord(c) + 32)
        else:
            nowy_tekst += c
        
    return nowy_tekst

print(moje_upper("Ala ma 2 koty!"))
print(moje_upper2("Ala ma 2 koty!"))

print(moje_lower("Ala ma 2 KOTY!"))