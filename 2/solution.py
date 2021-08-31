i = 1
fibb = [1, 2, 3, 5, 8]
sol = 0
while i < 4000000:
    i = fibb[-1] + fibb[-2]
    if i >= 4000000:
        break
    fibb.append(i)
for i in fibb:
    if i % 2 == 0:
        sol += i
print(sol)
