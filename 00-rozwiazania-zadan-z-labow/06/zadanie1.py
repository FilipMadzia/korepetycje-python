import random

random.seed(2026)

def rzuc_kostka(n):
    rzuty = [0, 0, 0, 0, 0, 0]

    for i in range(n):
        wylosowana = random.randint(1, 6)

        rzuty[wylosowana - 1] += 1

    return rzuty

print(rzuc_kostka(12))
print(rzuc_kostka(600))
print(rzuc_kostka(60000))