def get_col(table, c):
    assert c < len(table[0]), 'För högt kolumnnummer.'
    lst = []
    for k in range(0,len(table)):
              lst.append(table[k][c])
    return lst

def row_tot(table, r):
    assert r < len(table), 'För högt radnummer.'
    x = sum(table[r])
    return x

def col_max(table, c):
    lst = []
    assert c < len(table[0]), 'För högt kolumnnummer.'
    for k in range(0,len(table)):
        lst.append(table[k][c])
    x = max(lst)
    return x

if __name__ == '__main__':

    nästlad_lista = [[1,2,3,4,5],[2,4,6,8,10],[1,2,3,4,5]]
    test = get_col(nästlad_lista, 4)

    test2 = row_tot(nästlad_lista, 2)
    test3 = col_max(nästlad_lista, 4)
    print(test)
    print(test2)
    print(test3)



