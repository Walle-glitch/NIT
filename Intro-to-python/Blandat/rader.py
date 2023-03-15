rader = int(input('Hur många rader?'))
minus = 0
tecken = '-'
for i in range (rader,0,-1):
    for j in range (i):        
            print(f'{i:<2}' ,end=' ')
    print(f'{tecken:<2} ' * minus)
    #print()
    minus += 1
    
