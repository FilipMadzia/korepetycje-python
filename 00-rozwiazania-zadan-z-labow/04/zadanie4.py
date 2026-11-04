sprzedane = 0

def latte():
    global sprzedane
    print("Podano latte")
    sprzedane += 1 # sprzedane = sprzedane + 1

def espresso():
    global sprzedane
    print("Podano espresso")
    sprzedane += 1

def podsumowanie():
    global sprzedane
    print(f"Sprzedane kawy: {sprzedane}")

latte()
espresso()
latte()
podsumowanie()