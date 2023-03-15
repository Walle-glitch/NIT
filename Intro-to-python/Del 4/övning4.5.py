def medelvärde(a):
    summa = sum(a)
    n = len(a)
    return summa / n

mätvärden = input('Mätvärden: ')
lst_data = mätvärden.split()
data = [float(x) for x in lst_data]
mv = medelvärde(data)
print(f'Medelvärdet av de inmatade värdena är {mv}')
