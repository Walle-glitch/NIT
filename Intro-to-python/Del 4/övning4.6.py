def sänkt_pris(ordinarie_pris, prissänkning_procent):
    return ordinarie_pris * (1 - prissänkning_procent / 100)

ordinarie_pris = float(input('Varans ordinarie pris: '))
prissänkning_procent = float(input('Prissänkning i procent: '))
nytt_pris = sänkt_pris(prissänkning_procent, ordinarie_pris)
print(f'Det sänkta priset blir {nytt_pris}.')
