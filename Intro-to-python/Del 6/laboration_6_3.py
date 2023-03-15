import json


def räkna_röster(file_name):
    try:
        with open(file_name, 'r') as f:
            filen = json.load(f)
    except FileNotFoundError:
        filen = dict()
    data = input('Avgivna röster: ')
    angivna_röster = data.split()
    for ord in angivna_röster:
        if ord in filen.keys():
            filen[ord] += 1
        else: 
            filen.setdefault(ord, 1)    
    with open(file_name, 'w') as f:
        json.dump(filen, f)
    return filen




fil = input('Vilken fil vill du öppna? ')
sammanställning = räkna_röster(fil)
for kandidat in sammanställning:
    print(f'{kandidat}: {sammanställning[kandidat]} röster')


