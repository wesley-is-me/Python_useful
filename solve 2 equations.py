from sympy import symbols, Eq, solve
  
# defining symbols used in equations
# or unknown variables
x, y = symbols('x,y')
  
# defining equations
#0 is what the equation equals
eq1 = Eq((2*x + 4*y), 0)
print("Equation 1:")
print(eq1)
eq2 = Eq((4*x-2*y), 0)
print("Equation 2")
print(eq2)
  
# solving the equation
print("Values of 2 unknown variable are as follows:")
  
print(solve((eq1, eq2), (x, y)))