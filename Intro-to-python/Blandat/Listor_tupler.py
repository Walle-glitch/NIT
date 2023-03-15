lst = [83, 56, 14, 22, 75, 40]
for item in lst:
    if item % 2 == 0:
        print(item , end=' ')
print()
print()
print()
tlp = (8, -4, 10, 3, -7, -2)
counter = 0
for i in range(len(tlp)):
    if tlp[i] > 0:
        counter +=tlp[i]
print(counter)
print()
print()
print()

# enumerate
fruits =['apple', 'banana', 'cherry']
for i, item in enumerate(fruits):
    print(i, item)
print()
# samma som ovan
for i in range(len(fruits)):
    print(i, fruits[i])
print()
print()
print()


djur = ('beagle', 'siamese')
hund, cat = djur
for i, item in enumerate(djur):
    print(i, item)

print(djur)
print(hund)
print(cat)
print()
print()
print()
mat = [[1, 2],
       [3, 4]]
print(mat)

for row in mat:
    for item in mat:
        print(f'{item:2}',end=' ')
    print()
print()
print()
print()


