import listfunk

x = 5
y = 89
resultat = listfunk.addera(x, y)
print(resultat)

for i in range(0, 5):
    for j in range(i, 4):
        print('*', end=' ')
    for k in range(0, i):
        print('-', end=' ')
    print()

nestlist = [[2, 4, 2], [81, 94, 49, 4, 7],[12, 54, 21, 6, 4]]
summarad = listfunk.sumera_radfrad(nestlist)
print(summarad)
nestlist = [[2, 4, 2,], [81, 94, 49, 4, 7],[12, 54, 21, 6, 4]]
summarad2 = listfunk.sumera_alla(nestlist)
print(summarad2)
