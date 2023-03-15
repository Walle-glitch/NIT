import json

def spell(word):
    
    with  open('alfabet.json') as f:
        data = json.load(f)
    kopia = word
    kopia.split()
    nytt = []
    
    for i in word:
        try:
            nytt.append(data[i])
        except KeyError:
            pass
    return nytt

ordet = input('vilket ord ska översättas? ')
print(spell(ordet))
