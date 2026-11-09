n = int(input("Podaj n: "))

for i in range(1, 11):
    print(n*i, end=" ")
print()

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()