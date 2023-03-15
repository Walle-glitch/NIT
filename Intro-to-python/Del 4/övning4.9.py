def summera_positiva(värden):
    summa = 0
    for item in värden:
        if item > 0:
            summa += item
    return summa

print(summera_positiva(2, 5, -3, 1, -2))
print(summera_positiva(-1, 1, -1))
