import math

# Enter your code here. Read input from STDIN. Print output to STDOUT

AB = int(input())
BC = int(input())

AC = ((AB ** 2) + (BC ** 2)) ** (1/2)
MC = AC/2
MCB = math.atan(AB/BC)

# The law of cosines
BM = ((BC ** 2) + (MC ** 2) - (2 * BC * MC * math.cos(MCB))) ** (1/2)

# Tha law of sines
Tetha = round(math.degrees(math.asin(MC * math.sin(MCB) / BM)))
print(Tetha, '\u00b0', sep='')
