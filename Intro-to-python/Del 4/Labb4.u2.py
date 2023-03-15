def nästlare(lst):
    lst_2 = []                              #Skapa tom lista att fylla med tupler.
    for rad in lst:                         #Iterera över raderna. Oändliga rader är möjligt. 
        lst_2.append((len(rad), min(rad)))  #Skapa tupler med () 
    return print(lst_2)                     #Returnera en utskrift av färdig lista med tupler.


nästlad_lista = [[1, 2, 3, 4, 5],[2, 4, 8, 16, 32], [100, 200, 300]]
nästlare(nästlad_lista)         
