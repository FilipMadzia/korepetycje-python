import string

alfabet = string.ascii_lowercase

for litera in alfabet:
    kod_malej = ord(litera)
    kod_duzej = ord(litera.capitalize())
    print(f"{litera.capitalize()}: {kod_duzej} {litera}: {kod_malej} roznica: {kod_malej - kod_duzej}")