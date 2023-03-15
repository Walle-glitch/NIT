ord = input('Vilket ord spelar du? ')
poäng = int(0)
for i in ord:
    if i in 'adeilnrst':
        poäng += 1
    elif i in 'go':
        poäng += 2
    elif i in 'hkmpu':
        poäng += 3
    elif i in 'bfvåäö':
        poäng += 4
    elif i in 'cjy':
        poäng += 8
    elif i in 'qxz':
        poäng += 10
print(f'Ditt ord gav {poäng} poäng!') 
