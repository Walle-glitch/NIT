# En funktion som adderar två till ett givet tal
def add_two(tal):
    # Returnera resultatet
    return tal + 2
# Läs in ett tal från användaren och gör om det till int
user_number = int(input('Skriv ett tal: '))
# Anropa funktionen och lagra resultatet i variabeln resultat
resultat = add_two(user_number)
# Skriv ut värdet på variabeln resultat
print(f'Resultatet blev: {resultat}')
# En funktion som *försöker* ändra värdet på ett givet tal
def add_three(tal):
    # Addera tre till tal
    tal += 3
# Läs in ett tal från användaren och gör om det till int
user_number2 = int(input('Ett tal till: '))
# Anropa funktionen med målet att ändra värdet på user_number2
add_three(user_number2)
# Skriv ut värdet på variabeln user_number2
print(f'Resultatet blev: {user_number2}')
# Slutsats:
# - En funktion kan användas för att utföra en beräkning och returnera ett resultat
# - En funktion kan *inte* användas för att ändra värdet på ett heltal
