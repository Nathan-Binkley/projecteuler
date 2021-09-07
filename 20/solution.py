import sympy
 
sol = 0

for i in str(sympy.factorial(100)):
    sol += int(i)

print(sol)