matris = [[1, 2, 3, 4, 5],
         [2, 4, 6, 8, 10], 
         [3, 6, 9, 12, 15]]
for i in range(len(matris)):            # iterera över varje rad (lista i listan)
  for j in range(len(matris[i])):       # iterera över varje kolumn (element i de inre listorna)
    print(f'{matris[i][j]:4}', end='')  # reservera ett utrymme på 4 tecken, avsluta utan mellanslag eller ny rad
  print()                               # avsluta den aktuella raden
