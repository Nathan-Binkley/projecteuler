import sympy

sol = 0
for i in range(2000000):
    if sympy.isprime(i):
        sol += i
print(sol)