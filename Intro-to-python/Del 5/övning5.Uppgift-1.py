def addera_elementvis(lista1, lista2):
    temp = []
    k = 0
    if len(lista1) == len(lista2):
        for i in range(0, len(lista1)):
            temp.append(lista1[k] + lista2[k])
            k += 1
        return print(temp)
    else:
        print('nu blev det fel')
        raise 'listronra är inte lika långa'
        
lst1 = [1, 1, 2, 2, 3, 3]
lst2 = [0, 1, 2, 3, 4, 5]
addera_elementvis(lst1, lst2)
#print(summa)                           # [1, 2, 4, 5, 7, 8]
L1 = [1, 1, 1, 4, 4]
L2 = [3, 5, 6, 0]
addera_elementvis(L1, L2)      # Listorna är inte lika långa!
