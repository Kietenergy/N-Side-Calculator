#only works when side is more than 4 (5 is minimum)
import math
from fractions import Fraction
side = input("Number of sides? ")
length = input("Length of the side? ")
def power(value):
    new_value = value ** 2
    return new_value
A = power(int(length))
B = int(A) * int(side)
C = 180/int(side)
def trig(value):
    new_value = math.tan(math.radians(value))
    return new_value
D = trig(C)
E = D * 4
F = B/E
print("The area is " + str(F))

#made by "Keith"
