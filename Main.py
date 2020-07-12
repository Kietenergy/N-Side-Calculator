#only works when side is more than 4 (5 is minimum)
import math
import numpy
from fractions import Fraction
side = input("Number of sides? ")
length = input("Length of the side? ")
A = int(length) ** 2
B = int(A) * int(side)
C = 180/int(side)
D = math.tan(math.radians(C))
E = D * 4
F = B/E
print("The area is " + str(F))

#All was made by Keith