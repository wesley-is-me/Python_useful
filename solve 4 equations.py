from sympy import symbols, Eq, solve
  
# defining symbols used in equations
# or unknown variables
t, h, l, r = symbols('t, h, l, r')
  
# defining equations
eq1 = Eq((t + h - 5), 0)
print("Equation 1:")
print(eq1)
eq2 = Eq((l + r - 10), 0)
print("Equation 2")
print(eq2)
eq3 = Eq((((l * h)/ 2) - (r * h) - ((r * t)/ 2)), 0)
print("Equation 3")
print(eq3)
eq4 = Eq((((l * h)/ 2) + (r * h) + ((r * t)/ 2) - 25), 0)
print("Equation 4")
print(eq4)

  
# solving the equation
print("Values of 2 unknown variable are as follows:")
  
print(solve((eq1, eq2, eq3, eq4), (t, h, l, r)))