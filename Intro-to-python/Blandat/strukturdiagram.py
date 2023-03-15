# Funktionen implementerar det givna strukturdiagrammet rakt av
# Idén är att avgöra om en lista är sorterad genom att titta på varje par av 
# närliggande element (grannar).
# Om vi hittar ett par i fel ordning så är listan osorterad, annars är den sorterad.
def is_sorted(L):
    # Skapa och initialisera variabler
    res = True       # slutresultatet: vi utgår från att resultatet är True
    k = 0            # räknare som används för positionerna i listan
    n = len(L) - 1   # antalet värden på räknaren: lika många som antalet par av grannar i listan
    # Så länge vi inte har hunnit till sista paret
    while k < n:
        # Om det aktuella elementet är större än det som kommer efter
        if L[k] > L[k + 1]:
            res = False      # listan är inte sorterad
            break            # avsluta while-loopen
        else:
            k += 1           # gå vidare till nästa position
    # Returnera resultatet: True eller False
    return res
# En mer kompakt variant som gör samma sak
def is_sorted2(L):
    # För alla positioner i listan - utom den sista
    for k in range(len(L) - 1):
        # Titta på elementet på den aktuella positionen och på nästa:
        # Om de är i fel ordning är listan inte sorterad
        if L[k] > L[k + 1]:
            # Returnera resultatet False - avslutar funktionsanropet
            return False
    # Om vi inte hittat något par av närliggande element som är i fel ordning:
    # Listan är sorterad: Returnera resultatet True
    return True
l1 = [4, 2, 6, 8, 3, 2, 0, 7]
svar1 = is_sorted2(l1)
print(svar1)
l2 = [0, 4, 12, 28]
svar2 = is_sorted2(l2)
print(svar2)

svar1 = is_sorted(l1)
print(svar1)
l2 = [0, 4, 12, 28]
svar2 = is_sorted(l2)
print(svar2)
