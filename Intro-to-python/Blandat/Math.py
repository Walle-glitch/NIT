
##
# + addition 9 + 4 = 13
# - Subtracton 9 - 4 = 5
# * Multiplication 9 * 4 = 36
# / divition 9 / 4 = 2.25
# // Floor 9 // 4 = 2   # Avrundning till Heltal!
# % Modulus 9 % 4 = 1 # Vad är kvar efter Divition
# ** Exponent 9 ** 4 = 6561
#
#Prio Ordning: 
#1.   ( )
#2.   **
#3.   *, /, //, %
#4.   +, -
#
# 12 // 4+2 = 3+2 =5
# 12 // (4+2) = 12 // 6 = 2

import math
import random
siffra_a = int(input('var A:  ')) 
siffra_b = int(input('var b:  '))    
    
#print(siffra_a)
#print(siffra_b)
rest = siffra_b ** siffra_a
spq = math.sqrt(rest)

print(f'B upphöjt i A är: {rest} \n och roten ur {rest} är {spq}')
print(f'och som bonus, är kommer ett slumpmesstingt tal : {random.randrange(1,10)}')

