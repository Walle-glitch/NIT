def addera_numeriska(lst):
    added = 0
    for item in lst:
        try:
            added += item
        except TypeError:
            pass
    return added
l1 = [1, 2, 3, 4, 5, 'apa', 6.0]
summa = addera_numeriska(l1)
print(summa)                       # 21.0
