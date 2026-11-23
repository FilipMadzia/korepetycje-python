pesel = input("Podaj nr PESEL: ")
pesel = pesel.strip()

data = pesel[:6]
plec = pesel[9]

rok = int(data[:2])
miesiac = int(data[2:4])
dzien = int(data[4:6])

if miesiac >= 21 and miesiac <= 32:
    miesiac -= 20
    rok += 2000
else:
    rok += 1900

if int(plec) % 2 == 0:
    plec = "kobieta"
else:
    plec = "mezczyzna"

print(f"Data urodzenia: {dzien:02d}.{miesiac:02d}.{rok}")
print(f"Plec: {plec}")