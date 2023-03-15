import json

fil = input('Vilken fil vill du öppna? ')

try:
    with open(fil, 'r') as f:
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

with open(fil, 'w') as f:
    json.dump(filen, f)


for kandidat in filen:
    print(f'{kandidat}: {filen[kandidat]} röster')

