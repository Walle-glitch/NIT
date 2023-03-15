mätvärden = input('Mätvärden: ')
lst_data = mätvärden.split()
data = [float(t) for t in lst_data] # använd list comprehension här
summa = sum(data)
print(f'Summan av de inmatade värdena är {summa}')
