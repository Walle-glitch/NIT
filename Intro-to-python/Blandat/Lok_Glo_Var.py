x, y, z = 1, 2, 4

def f(x):
    x += y
    z = 8
    return x

y = f(x)
print(x, y, z)


x, y, z = 1, 2, 4

def f(x):
    x += y
    global z
    z = 8
    return x

y = f(x)
print(x, y, z)


def flip(lst):
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n -1 -i] = lst[n -1 -i], lst[i]
L = [1, 2, 3, 4, 5]
print(L)
flip(L)
print(L)
