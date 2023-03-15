
def görom(a, största=255):
    ny_lst = a.copy()
    test = största
    k = 0
    for i in range(0, len(ny_lst)):
        if ny_lst[i] < test:
            ny_lst[i] = test
            k += 1
        else:
            continue
    return print(f'{ny_lst} antal ändrade {k}   {a}')

listan = [661, 252, 213, 12, 96, 138]
maxvärde = 100

görom(listan, maxvärde)
görom(listan)
