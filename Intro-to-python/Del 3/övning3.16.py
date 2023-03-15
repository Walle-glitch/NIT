tabell_n = [[str(n) + c for c in 'abcde'] for n in range(1, 4)]
#detta blir "värdet" av tabell_n
#[['1a', '1b', '1c', '1d', '1e'],
#['2a', '2b', '2c', '2d', '2e'],
#['3a', '3b', '3c', '3d', '3e']]

for i in range(0, 4):
    t = 0
    for j in range(0, 3):
        print(tabell_n[t][i], end=' ')
        t += 1
    print()

print()
print()
print()
print()
print()

tabell = ['a', 'b', 'c', 'd', 'e',]

for i in range(0, len(tabell)):
    for j in range(0, len(tabell[i])):
        x = 0
        for k in range(1, 4):
            x += 1
            print(f'{x}{tabell[i][j]} ', end=' ')
    print()
