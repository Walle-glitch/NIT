def nollställ_negativa(*lst):
    for  in lst:
        if item in lst:
            i = 0
            lst[i] = lst[i]*2
            i+=1
    return lst

värden = [4, 0, -3, 5, 1, -1]
nollställ_negativa(värden)
print(värden)                  # [4, 0, 0, 5, 1, 0]
