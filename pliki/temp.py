licznikWywolan = 0

def przestaw(n):
    global licznikWywolan
    licznikWywolan += 1
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100
    if n > 0:
        w = a + 10 * b + 100 * przestaw(n)
    else:
        if a > 0:
            w = a + 10 * b
        else:
            w = b
    return w

def podajLiczbeCyfr(n):
    nKopia = n
    licznik = 0
    while nKopia > 0:
        licznik += 1
        nKopia = nKopia // 10
    return licznik

def dziesiecDoPotegi(n):
    wynik = 1
    while n > 0:
        wynik = wynik * 10
        n -= 1
    return wynik

def przestaw2(n):
    liczbaCyfr = podajLiczbeCyfr(n)
    w = 0
    nKopia = n
    licznikCyfr = 0
    while nKopia > 0:
        cyfra = nKopia % 10
        nKopia = nKopia // 10
        if liczbaCyfr % 2 == 1:
            if licznikCyfr == (liczbaCyfr - 1):
                w += cyfra * dziesiecDoPotegi(licznikCyfr)
                break
        if licznikCyfr % 2 == 0:
            w += cyfra * dziesiecDoPotegi(licznikCyfr + 1)
        else:
            w += cyfra * dziesiecDoPotegi(licznikCyfr - 1)
        licznikCyfr += 1
    return w

liczba = 213245353223

print(przestaw2(liczba))
print(przestaw(liczba))
#print(licznikWywolan)
#print(f"L. cyfr: {len(str(liczba))}")