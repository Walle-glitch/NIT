s = 'initial'
n = len(s)
print(f'{s} starts with {s[0]} and ends with {s[6]}')
print(f'{s} ends with {s[-1]}')
print(n)
print()
print()
s= 'FBI'
for i in range(len(s)):
    print(s[i], end='.')
print()
print()
print()
s = "stressed"
for i in range(len(s)):
    print(s[-i - 1], end='')
print()
print()
print()
s = 'Some seneitive subject'
for c in s:
    if c in 'aeiouy':
        print('*', end='')
    else:
        print(c, end='')
print()
print()
print()
s = 'abcdef'
print(s[3:])
print(s[3])
print()
print()
print()

