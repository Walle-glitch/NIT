def med_eftertryck(a):
    for i in range(len(a)):
       a = i + '*' #end='*')
    return a

ett_ord = 'kanon'
nytt_ord = med_eftertryck(ett_ord)
print(nytt_ord)                        # k*a*n*o*n
annat_ord = 'perfekt'
nyare_ord = med_eftertryck(annat_ord)  # p*e*r*f*e*k*t
print(nyare_ord)
