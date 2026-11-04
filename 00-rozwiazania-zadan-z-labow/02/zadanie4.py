import turtle


kolor = input("Podaj kolor w formacie #RRGGBB: ")
r = int(kolor[1:3], 16)
g = int(kolor[3:5], 16)
b = int(kolor[5:7], 16)

kolor2 = input("Podaj drugi kolor w formacie #RRGGBB: ")
r2 = int(kolor2[1:3], 16)
g2 = int(kolor2[3:5], 16)
b2 = int(kolor2[5:7], 16)

rozmiar_czcionki = int(input("Podaj rozmiar czcionki: "))

turtle.colormode(255)
turtle.bgcolor((r, g, b))
turtle.pencolor((r2, g2, b2))
turtle.write(f"RGB({r}, {g}, {b})", font=("Arial", rozmiar_czcionki))
turtle.done()