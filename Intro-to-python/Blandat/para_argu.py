def f(a, b, c):
    print(a, b, c)

x = 1; y = 2; z = 3
f(y, c=x, b=z)

def f(a, b, c):
    print(a, b, c)

x, y, z = 1, 2, 3
f(y, c=x, b=z)
f(y, x, z)
f(x, y, z)


def f(a, b, c=0):
    print(a, b, c)
f(z, b=y)

def print_last(*people):
    print(f'Last, but not least: {people[-1]}')
print_last('jack', 'Jill')

def sum_separately(*values):
    pos, neg = 0, 0
    for item in values:
        if item < 0:
            neg += item
        else:
            pos += item
    return pos, neg
revenue, expenses = sum_separately(2, 3, -2, -7, 0, 1)
print(f'Revenue: {revenue}, Expenses: {-expenses}')

def sum_separately(*values, limit=0):
    pos, neg = 0, 0
    for item in values:
        if item < limit:
            neg += item
        else:
            pos += item
    return pos, neg
big, small = sum_separately(2, 12, 13, 7, 19, limit=10)
print(f'Small fish: {small}, Big fish: {big}')






