def dubbelt_upp(x):                     # funktionsdefinition, x är en parameter
    return 2 * x                        # funktionskropp

tal = int(input('Ange ett tal: '))
dubbla_talet = dubbelt_upp(tal)         # funktionsanrop, tal är ett argument
print(f'Du säger {tal}. Dubbla det: {dubbla_talet}')
