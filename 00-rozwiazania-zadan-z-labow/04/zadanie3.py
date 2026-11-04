def ciag(n, a1=1, r=1):
    ciag = [a1]
    for i in range(1, n):
        ciag.append(a1 + r*i)

    return ciag

print(ciag(5))
print(ciag(5, r=2)) # zapis ciag(5, 2) oznaczalby, ze a1 = 2
print(ciag(5, 2, 2)) # to samo co ciag(5, a1=2, r=2)
print(ciag(4, 10, -3))