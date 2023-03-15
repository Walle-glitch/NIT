import math
talserie = input('Ange heltal skilda med mellanslag: ')
lst_data = talserie.split()
lst = [int(x) for x in lst_data]
for x in range(len(lst)):
    lst[x] *= lst[x]
print(sum(lst))
print(f'{math.sqrt(sum(lst)):.2f}')
