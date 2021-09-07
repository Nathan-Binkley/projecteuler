
m = [0, 0] #length, i

for i in range(1,1000000):
    p = i
    l = 0
    while p != 1:
        if p % 2 == 0:
            p /= 2
        else:
            p = 3*p + 1
        l += 1
    if l > m[0]:
        m = [l, i]
    print(i)

print(m)

