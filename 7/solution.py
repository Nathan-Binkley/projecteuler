import sympy

sol = 0
count = 0
for i in range(99999999999):
    if sympy.isprime(i):
        count += 1
        if count == 10001:
            sol = i
            break
print(sol)
