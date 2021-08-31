pal = 0
for i in range(1, 1000):
    for j in range(1,1000):
        s = str(i*j)
        rs = "".join(list(reversed(s)))
        if s == rs and i*j > pal:
            pal = i*j

print(pal)