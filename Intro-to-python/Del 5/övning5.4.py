
while True:
    try:
        tal = float(input('Ange ett tal: '))
        break
    except ValueError:
        print('Inte ett tal!')
print('då var det färdigt!')
