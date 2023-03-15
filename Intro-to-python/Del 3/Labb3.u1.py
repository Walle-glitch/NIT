ord = input('Skriv valfritt ord: ')
for i in ord:
    print('*', end='')
print('')

ord_2 = input('Skriv ett valfritt ord igen: ')
for i in ord_2:
    if i == ord_2[0]:
        print(ord_2[0], end='')
    elif i == ord_2[-1]:
        print(ord_2[-1], end='')
    else:
        print( '*', end='')
print('')

ord_3 = input('Skriv ytterligare ett ord')
for i in ord_3:
    if i in 'aouåeiyäö':
        print('*', end='')
    else:
        print(i, end='')

        
