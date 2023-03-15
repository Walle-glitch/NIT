


def räkna_röster(röst_lista):
    resultat = {}
#       för varje tecken i variabeln röst_lista
    for i in range(len(röst_lista)):
#       nyckel identiferas genom positionen " i " i röst_lista.         
        key = röst_lista[i]
#       Setdefalut OM nyckeln inte finns skapas den och får värdet 0 tilldelat.         
        resultat.setdefault(key, 0)
#       nyckelns värde adderas med ett(1)
        resultat[key] += 1
    return resultat

data = input('Avgivna röster: ')
avgivna_röster = data.split()
sammanställning = räkna_röster(avgivna_röster)
for kandidat in sammanställning:
    print(f'{kandidat}: {sammanställning[kandidat]} röster')
d
