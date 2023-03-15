lst = [3, 0, -2, 1, 1, -1, -2, 3, 2, 3, 0]
for i in range(0, len(lst)):
    if lst[i] < 0:  #om det aktuella elementet är negativt:
        lst[i] = 0 # sätt elementet till 0
print(lst)
