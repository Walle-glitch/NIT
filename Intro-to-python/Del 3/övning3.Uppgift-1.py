#År 1898 genomfördes en stavningsreform då
#bokstaven q byttes ut mot k och bokstaven w byttes ut mot v.
#Läs in ett ord från användaren och
#skapa en sträng där gammal stavning ersatts med ny.

user_word = input('Ange ett ord med gammal stavning: ')  # qvinna
q = 'q'
w = 'w'

user_word = list(user_word)
nystavat = []
#loopa över inmatade ordet. 
for i in range(len(user_word)):
    #om i positionen är lika med q
    if q == user_word[i]:
        #ersätt q med k
        user_word[i] = 'k'
        #för in det ny stavade ordet i den tomma listan
        nystavat = user_word
    elif w == user_word[i]:
        nystavat[i] = 'v'
        nystavat = user_word
#formatera listan. 
print(''.join(nystavat))                                         # kvinna
