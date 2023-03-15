

# table[i][c] # J är det som ska rörars
def get_col(table, c):
    f = list()
    assert IndexError, c < len(table[j][0:-1]) ('c är för stort')       
    for k in range(0, len(table)):
        f.append(table[k][c])
    return f


def row_tot(table, r):
    restu = sum(table[r])
    return restu
    

def col_max(table, c):
    f = list()
    assert IndexError, c < len(table[j][0:-1]) ('c är för stort')       
    for k in range(0, len(table)):
        f.append(table[k][c])
    return max(f)

    







if __name__ == '__main__':
    tabellen = [[1, 4, 7, 1, 5], [9, 8, 7, 6], [3, 1, 4, 6]]
    
    col_nr = 3 # C
    hitta = get_col(tabellen, col_nr)
    print(hitta)
    print(max(hitta))

    rader = 2 # R
    sumera_rader = row_tot(tabellen, rader)
    print(sumera_rader)

    h_col = 3 # c
    hög_rader = row_tot(tabellen, h_col)
    print(hög_rader)


    
