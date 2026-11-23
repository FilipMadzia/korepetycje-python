counter = 0

for i in range(32, 127):
    print(f"{i}:{chr(i)}", end="\t")
    counter += 1

    if counter >= 8:
        print()
        counter = 0