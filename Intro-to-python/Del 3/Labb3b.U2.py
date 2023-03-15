user_data_a = input('Ange värden: ') # '1 0 2 5' 
user_lst_a = user_data_a.split()
lst_data_a = [int(t) for t in user_lst_a]

user_data_b = input('Ange värden: ') # ' 2 3 0 1'
user_lst_b = user_data_b.split()
lst_data_b = [int(k) for k in user_lst_b]
y = []
x = 0

for i in lst_data_a:
    y.append(lst_data_a[x] * lst_data_b[x])
    x += 1

print(y)
sum(y)
print(sum(y))
