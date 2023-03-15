ord = input('Skriv ett ord: ')
första = ord[0]          # strängens första tecken
sista = ord[-1]          # strängens sista tecken: kom ihåg att vi inte vet hur lång strängen är!
baklänges = ord[::-1]       # använd slicing för att vända på strängen
print(f'Ordet börjar på {första} och slutar på {sista}.')
print(f'Baklänges blir det {baklänges}.')
#for i in range(len(ord)):
    #baklänges = (ord[-i -1], end='')
 #   print(ord[-i -1], end='')
