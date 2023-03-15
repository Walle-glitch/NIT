user_data = input('Ange värden: ')
user_lst = user_data.split()
lst_data = [int(t) for t in user_lst]
f_l = [float(t) for t in lst_data]
for item in f_l:
    if item >0:
        print(item, end=' ')
