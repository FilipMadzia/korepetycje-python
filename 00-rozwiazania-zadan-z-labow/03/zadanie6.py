slowo = input("Podaj slowo: ")

samogloski = ['a', 'o', 'e', 'i', 'u', 'y']

ile_samoglosek = 0
ile_spolglosek = 0
bez_samoglosek = ""

for l in slowo:
    if l in samogloski:
        ile_samoglosek += 1
    else:
        bez_samoglosek = bez_samoglosek + l
        ile_spolglosek += 1

print(f"Samogloski: {ile_samoglosek}, spolgloski: {ile_spolglosek}")
print(f"Bez samoglosek: {bez_samoglosek}")