def dela_med(täljare, nämnare):
    if nämnare == 0:
        raise ZeroDivisionError('kan inte dividera med 0')
    else:
        return täljare / nämnare
print('x delas på y')
x = int(input('välj x värde:  '))
y = int(input('välj y värde:  '))
print(f'svaret är: {dela_med(täljare=x, nämnare=y)} ')
