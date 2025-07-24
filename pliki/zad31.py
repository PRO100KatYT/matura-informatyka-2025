with open("dron.txt", "r") as temp: plik = temp.readlines()
#with open("dron_przyklad.txt", "r") as temp: plik = temp.readlines()

def NWD(a, b):
    if b == 0:
        return a
    while b > 0:
        a, b = b, a % b
    return a

licznik = 0

for linia in plik:
    linia = linia.strip().split(" ")
    A = int(linia[0])
    B = int(linia[1])
    if NWD(abs(A), abs(B)) > 1:
        licznik += 1

print(licznik)