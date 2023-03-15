#Hittills har vi itererat över strängar för att skriva ut dess bokstäver, en i taget. Nu vill vi istället att vår kod resulterar i en modifierad sträng. Följande kod är ett misslyckat försök att byta strängens vokaler mot stora bokstäver och strängens konsonanter mot små bokstäver.

#Kör koden för att se vad som händer.

ord = input('Skriv ett ord: ')
for bokstav in ord:
  if bokstav in 'aouåeiyäö':
    bokstav = bokstav.upper()
  else:
    bokstav = bokstav.lower()
print(ord)
