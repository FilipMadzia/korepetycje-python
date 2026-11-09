a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = b**2 - 4 * a * c

if a == 0:
    print("Rownanie nie jest kwadratowe")

if a != 0:
    if delta > 0:
        x1 = (-b - delta**0.5) / 2 * a
        x2 = (-b + delta**0.5) / 2 * a
        
        print(f"x1: {x1} x2: {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        
        print(f"x: {x}")
    else:
        print("Brak rozwiazan rzeczywistych")