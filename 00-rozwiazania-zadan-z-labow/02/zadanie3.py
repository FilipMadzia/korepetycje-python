kolor = input("Podaj kolor w formacie #RRGGBB: ")

r16 = kolor[1:3]
g16 = kolor[3:5]
b16 = kolor[5:7]

print(f"{r16}, {g16}, {b16}")

r = int(r16, 16)
g = int(g16, 16)
b = int(b16, 16)

print(f"RGB({r}, {g}, {b})")