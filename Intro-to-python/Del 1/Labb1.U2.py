#
#
#
#
#
#
import math
#inmatning av Apparatens Effekt i watt
P = float(input('ange en effekt i Watt: '))
# inmatning av Resistans i kretsen i Ohm
R = float(input('ange resistans i Ohm: '))
#Beräkning av 
U = math.sqrt(P * R)
print(f' spänning i Volt blir {U:.2f}' )
