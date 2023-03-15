def division(täljare, nämnare):
    assert nämnare != 0, 'kan inte dividera med 0'
    return täljare / nämnare

print('x delas på y')
x = int(input('välj x värde:  '))
y = int(input('välj y värde:  '))
print(f'svaret är: {division(täljare=x, nämnare=y)} ')
