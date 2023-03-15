ord = input('Type in an english word please: ')
b = ''
if ord[0] in 'aouåeiyäö':
    print(ord + 'way')
else:
    for i in ord:
        if i in 'bcdfghjklmnpqrstvwxz':
            b += i
            
        elif i in 'aouåeiyäö':
            print(ord[len(b):] + b + 'ay')
            break

            
            
