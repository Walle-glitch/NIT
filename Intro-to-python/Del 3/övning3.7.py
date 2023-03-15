ord = input('Skriv ett ord: ')
tom_st = ''                 # lägg till: skapa en ny (tom) sträng
for bokstav in ord:
  if bokstav in 'aouåeiyäö':
    tom_st += bokstav.upper()    # ändra: lägg till i den nya strängen
  else:
    tom_st += bokstav.lower()    # ändra: lägg till i den nya strängen
print(tom_st)                       # ändra: skriv ut den nya strängen
