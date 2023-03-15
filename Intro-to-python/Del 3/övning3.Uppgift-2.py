#Multiplicera alla tal i en tupel och skriv ut resultatet.

data = (3, 1, 4, 3, 2, 2, 1)
mat = [int(e) for e in data]
mat.insert(0, 1)
res = [1, ]
for i in range(0, 6):
    res.append(res[0] * mat[1])
    del mat[0]
    del res[0]
print(res)



