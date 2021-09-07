import sympy


sol = 0
sd = list(sympy.divisors(220))[:-1]
si = list(sympy.divisors(284))[:-1]
print(sd,si)
print(sd==si)

vals = []

for i in range(1, 10000):
    sd = sum(list(sympy.divisors(i))[:-1])
    if sum(list(sympy.divisors(sd))[:-1]) == i and sd != i and i not in vals:
        sol += sd
        sol += i
        vals.append(i)
        vals.append(sd)
        print([i, sd])
print(sol)

