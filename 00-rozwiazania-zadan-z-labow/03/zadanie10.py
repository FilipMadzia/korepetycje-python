def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(1, 50):
    if czy_pierwsza(i):
        print(i)