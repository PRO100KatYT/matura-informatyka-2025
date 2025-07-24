with open("symbole.txt", "r") as temp: plik = temp.readlines()
#with open("symbole_przyklad.txt", "r") as temp: plik = temp.readlines()

macierz = []

wynik = ""
liczbaKwadratow = 0

for linia in plik:
    linia = linia.strip()
    lista = []
    for znak in linia:
        lista.append(znak)
    macierz.append(lista)

def czySasiedziTacySami(i, j, macierz):
    a = macierz[i-1][j-1]
    b = macierz[i-1][j]
    c = macierz[i-1][j+1]
    d = macierz[i][j-1]
    e = macierz[i][j]
    f = macierz[i][j+1]
    g = macierz[i+1][j-1]
    h = macierz[i+1][j]
    i = macierz[i+1][j+1]
    if a == b and a == c and a == d and a == e and a == f and a == g and a == h and a == i:
        return True
    return False

for i in range(1, len(macierz) - 1):
    for j in range(1, len(macierz[i]) - 1):
        if czySasiedziTacySami(i, j, macierz):
            wynik += f"{i+1} {j+1}\n"
            liczbaKwadratow += 1

print(f"Liczba kwadratow: {liczbaKwadratow}")
print(wynik)