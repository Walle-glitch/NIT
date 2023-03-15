
def addera(a, b):
    rest = 0
    rest += a+b
    return rest

def sumera_radfrad(lst):
    restu = 0
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            restu += sum(lst[i])
            print()
        print(restu) # end=' ')
    print()


def sumera_alla(lst):
    restu1 = 0
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            restu1 += sum(lst[i])
    return restu1
        

    

if __name__ == '__main__':
    x = 2
    y = 8
    summa = addera(x, y)
    print(summa)
