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

sumaLiczb = sum(liczbyDec)

def LiczbaNaTrojkowaEncoded(liczbaDec):
    mapaZnakow = {
        0: "o",
        1: "+",
        2: "*"
    }
    liczbaStrEncoded = ""
    liczbaDecKopia = liczbaDec
    while liczbaDecKopia > 0:
        cyfra = liczbaDecKopia % 3
        liczbaDecKopia = liczbaDecKopia // 3
        liczbaStrEncoded = mapaZnakow[cyfra] + liczbaStrEncoded
    return liczbaStrEncoded

wynik += f"{sumaLiczb} {LiczbaNaTrojkowaEncoded(sumaLiczb)}"

print(wynik)