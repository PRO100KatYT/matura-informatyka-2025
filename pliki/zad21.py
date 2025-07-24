with open("symbole.txt", "r") as temp: plik = temp.readlines()
#with open("symbole_przyklad.txt", "r") as temp: plik = temp.readlines()

wynik = ""

for linia in plik:
    linia = linia.strip()
    if linia == linia[::-1]:
        wynik += f"{linia}\n"

print(wynik)