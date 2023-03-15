ft_in = []
inches = 0
feet = 0
p = int(12)
for inches in range(0, 4):
    t = 0
    x = 0
    print(round(p * feet + inches * 2.54))
    for feet in range(0, 12):
        print(float(ft_in[x][t], end=' '))
        t += 1
    print()
