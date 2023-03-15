ft_in = [[f'{round((12 * feet + inches) * 2.54):3}' \
          for inches in range(12)] for feet in range(4)]

print(ft_in)
for i in range(len(ft_in)):            # iterera över varje rad (lista i listan)
  for j in range(len(ft_in[i])):       # iterera över varje kolumn (element i de inre listorna)
    print(f'{ft_in[i][j]:4}', end='')  # reservera ett utrymme på 4 tecken, avsluta utan mellanslag eller ny rad
  print()

print()
print()
print()
alternativ = []
for feeet in range(4):
    row = []
    for inch in range(12):
        row.append(f'{round((12 * feeet + inch) * 2.54):3}')
    alternativ.append(row)
    
print(alternativ)




