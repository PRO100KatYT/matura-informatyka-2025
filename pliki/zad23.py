with open("symbole.txt", "r") as temp: plik = temp.readlines()
#with open("symbole_przyklad.txt", "r") as temp: plik = temp.readlines()

znakNaCyfreTrojkowa = {
    "o": "0",
    "+": "1",
    "*": "2"
}

liczbyEncoded = []
liczbyStr = []
liczbyDec = []

wynik = ""

for linia in plik:
    linia = linia.strip()
    liczbyEncoded.append(linia)
    liczbaStr = ""
    for znak in linia:
        liczbaStr += znakNaCyfreTrojkowa[znak]
    liczbyStr.append(liczbaStr)

for liczbaStr in liczbyStr:
    liczbaDec = int(liczbaStr, 3)
    liczbyDec.append(liczbaDec)

maksLiczba = max(liczbyDec)
for i in range(len(liczbyDec)):
    if liczbyDec[i] == maksLiczba:
        wynik += f"{maksLiczba} {liczbyEncoded[i]}"

print(wynik)