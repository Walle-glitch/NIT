tabell = [[3, 5, 2],
          [1, 1, 1],
          [2, 1, 4],
          [2, 3, 4]]   # 4 rader, 3 kolumner
radsummor = []
for i in range(0, len(tabell)):
    #skapar 0ch lägger till summering av [[i],] i variabeln radsummor
    radsummor.append(sum(tabell[i])) 
print(radsummor)                                        # [10, 3, 7, 9]
