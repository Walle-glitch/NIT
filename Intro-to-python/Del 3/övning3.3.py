ord = input('Skriv ett ord som innehåller bokstaven x: ')
låg = ord.lower()
test = 'x' in låg

if test == True:
    print('rätt')
# om bokstaven x inte finns i ordet
# skriv ut felmeddelande
else:
    print('Det finns inget x i ordet')
