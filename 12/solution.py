import sympy

def create(num):
    sol = 0
    for i in range(num+1):
        sol += i
    return sol

def check(num):
    return list(sympy.divisors(num))
i = 0
while True:
    v = create(i)
    c = check(v)
    if len(c) > 500:
        print(i, v)
        break
    i += 1