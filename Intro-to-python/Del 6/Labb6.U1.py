
# text_fil.txt

fil = input('filens nam: ?')
g_ord = input('vilket ord ska bytas ut? ')
nytt_ord =  input('vilket nytt ord ska användas? ')

with open(fil, r+, w+) as f:
    kopia = f.readlines()
    kopia.replace(g_ord, nytt_ord)
    print(kopia, file=f)

# banan
# äpple
