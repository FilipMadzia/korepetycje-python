def czy_parzysta(n):
    return n % 2 == 0

for i in range(1, 21):
    if czy_parzysta(i):
        print(i)