#only works when side is more than 4 (5 is minimum)
import math
from fractions import Fraction
side = input("Number of sides? ")
length = input("Length of the side? ")
#Length of each sides
L = int(length)
#Number of sides
S = int(side)
def power(value):
    return value ** 2
def trig(value):
    return math.tan(math.radians(value))
#n = Regular Polygon Area Formula
def n(value):
    return ((power(L) * S) / (4 * trig(180/(S))))
A = n(1)
print('The area of this ' + str(S) + " side polygon is "  + str(A))

# Made by "Keith"
