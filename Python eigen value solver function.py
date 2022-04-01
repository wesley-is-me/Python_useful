from sympy import *
from numpy import round
  
# Use sympy.eigenvals() method
#This is the matrix, just put in line by line.
mat = Matrix([[(6 * (4 / 3)), 4], [4, (-6 * (-4 / 3))]])
d = mat.eigenvals()
print(d)