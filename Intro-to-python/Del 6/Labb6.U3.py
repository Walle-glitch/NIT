import json

def räkna_röster(file_name):
    try:
        with open(file_name, 'r') as f:
            filen = json.load(f)
    except FileNotFoundError:
        filen = dict()
    data = input('Avgivna röster: ')
    angivna_röster = data.split()
    for ordx in angivna_röster:
        if ordx in filen.keys():
            filen[ordx] += 1
        else: 
            filen.setdefault(ordx, 1)
    
    with open(file_name, 'w') as f:
        json.dump(filen, f)
    return filen

if __name__ == '__main__':
    
    fil = input('Vilken fil vill du öppna? ')
    sammanställning = räkna_röster(fil)
    for kandidat in sammanställning:
        print(f'{kandidat}: {sammanställning[kandidat]} röster')
