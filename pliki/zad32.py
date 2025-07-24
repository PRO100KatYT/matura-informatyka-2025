with open("dron.txt", "r") as temp: plik = temp.readlines()
#with open("dron_przyklad.txt", "r") as temp: plik = temp.readlines()

punktyPoPrzesuniesiach = [[0, 0]]
for linia in plik:
    linia = linia.strip().split(" ")
    A = int(linia[0])
    B = int(linia[1])
    noweWsp = punktyPoPrzesuniesiach[-1].copy()
    noweWsp[0] += A
    noweWsp[1] += B
    punktyPoPrzesuniesiach.append(noweWsp)
punktyPoPrzesuniesiach = punktyPoPrzesuniesiach[1::]


licznik = 0

for punkt in punktyPoPrzesuniesiach:
    A = punkt[0]
    B = punkt[1]
    if A > 0 and A < 5000:
        if B > 0 and B < 5000:
            licznik += 1

szukanePunkty = ""

for punkt1 in punktyPoPrzesuniesiach:
    for punkt2 in punktyPoPrzesuniesiach:
        for punkt3 in punktyPoPrzesuniesiach:
            x1 = punkt1[0]
            y1 = punkt1[1]
            x2 = punkt2[0]
            y2 = punkt2[1]
            x3 = punkt3[0]
            y3 = punkt3[1]
            if punkt1 == punkt2:
                continue
            if punkt2 == punkt3:
                continue
            if punkt1 == punkt3:
                continue
            if x1 == (x2 + x3)/2:
                if y1 == (y2 + y3)/2:
                    szukanePunkty = f"{punkt1} {punkt2} {punkt3}".replace("[", "(").replace("]", ")")

print(f"a) {licznik}")
print(f"b) {szukanePunkty}")