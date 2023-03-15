
#översätter till "pig latin"
def pig_latin(word):
    if word[0].lower() in 'aeiouy':
        return word + 'way'
    else:
        for i, letter in enumerate(word):
            if letter.lower() in 'aeiouy':
                return word[i:] + word[:i] + 'ay'
    return word

#tar bort kommentarer markerade med # 
def strip_comment(word):
    for i in range(len(text)):
        if text[i] == '#':
            return text[: i].rstrip() + '\n'
    return text

#tar bort kommentarer markerade med # 
def uncomment(infale, outfile):
    with open(infile) as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if line[0] != '#':
            new_lines.append(strip_comment(line))
    with open(outfile, 'w') as f:
        for line in new_lines:
            f.write(line)

# skriver utt ett ord på rövarspråket
def rövarspråk(ord):
    vokaler = 'aouåeiyäöö'
    översättning = ''
    # för varje bokstav i ordet:
    for i in range(len(ord)):
        if ord[i] in vokaler:
            översättning += ord[i]
        else:
            översättning += (ord[i] + 'o' + ord[i])
    return översättning


def scrabble(ord):
    alfabetet = 'abcdefghijklmnopqrstuvxyzåäö'
    poäng = [1, 4, 8, 1, 1, 3, 2, 2, 1, 7, 2, 1, 2, 1, 2, 4, 1, 1, 1, 4, 3, 8, 7, 10, 4, 3, 3]
    poängtabell = dict(zip(alfabetet, poäng))
    total = 0
    # för varje bokstav i ordet:
    for i in range(len(ord)):
        for key, value in poängtabell.items():
            if key in ord[i]:
                total += value            
    return total

def räkna_röster(röst_lista):
    resultat = {}
    
    # för varje röst i röstlistan:
    try:
        for item in range(len(röst_lista)):
            
    #     lägg till en röst på kandidaten i resultat,
    #     skapa nyckel-värde-par om kandidaten inte redan finns
    
    return resultat


# för tester i denna fil. 
if __name__ == '__main__':
    #val = input('vilket program? \n 1. Pig_latin \n 2. RÖVARSPRÅKET \n 3. Scrabble \n? \n \n: ' )
    #if val == 1:
#test PIG_LATEN
#        eng_ord = input('Skriv ett ord: ')
#        pig_ord = pig_latin(eng_ord)
#        print(f'På Pig Latin blr det {pig_ord}.')
#    elif val == 2:
    # test till RÖVARSPRÅKET
#        svenskt_ord = input('Skriv ett ord: ')
#        översatt_ord = rövarspråk(svenskt_ord)
#        print(f'På rövarspråket blir det {översatt_ord}.')
#    elif val == 3: 
#    användarord = input('Skriv ett ord: ')
#    ordpoäng = scrabble(användarord)
#    print(f'Din ordpoäng är {ordpoäng}.')
    
    data = input('Avgivna röster: ')
    avgivna_röster = data.split()
    sammanställning = räkna_röster(avgivna_röster)
    for kandidat in sammanställning:
        print(f'{kandidat}: {sammanställning[kandidat]} röster')

    
