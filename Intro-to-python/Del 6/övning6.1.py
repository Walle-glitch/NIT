elever = {'Ali', 'Bo', 'Carl', 'David', 'Emma', 'Frida'}
närvarande = {'Carl', 'David'}
ledig = {'Ali', 'Emma'}
sjuk = {'Frida'}
frånvarande = ledig | sjuk
#print(frånvarande)
ogiltig_frånvaro = elever.difference(närvarande, frånvarande)# = närvarande | frånvarande
print(ogiltig_frånvaro)

