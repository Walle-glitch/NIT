# En funktion som dubblerar vart och av elementen i en lista
def dubblera(L):
    # För var och en av positionerna i listan
    for i in range(len(L)): # Vi måste iterera med range och referera till 
# elementen via indexering för att kunna ändra
        L[i] *= 2           # Multiplicera elementet på position i med två
# Skapa en lista
lst = [0, 1, 3, 7, 5]
# Anropa funktionen för att förändra listan
dubblera(lst)
# Skriv ut resultatet
print(lst)
# En funktion som byter tecken på alla negativa element i en lista
def absolutbelopp(L):
    # För var och en av positionerna i listan
    for i in range(len(L)):
        # Om elementet är negativt
        if L[i] < 0:
            # Byt tecken
            L[i] *= -1
# Skapa en lista
lst = [9, -4, 6, -2, 0, 1]
# Anropa funktionen för att förändra listan
absolutbelopp(lst)
# Skriv ut resultatet
print(lst)
# Gör om hela processen med en ny lista, med ett annat variabelnamn
values = [2, -7, -8, -3, 0, 2]
absolutbelopp(values)
print(values)
# Kom ihåg:
# - Vi kan inte använda funktioner för att ändra värden på int, float, str, tuple
# - Vi *kan* använda funktioner för att ändra värden i en lista
# - Inuti funktionen använder vi funktionens parametrar, *inte* variabler som 
#definierats utanför funktionen
