sofsum = 0
s = 0

count = 100
for i in range(count+1):
    s += i ** 2
    sofsum += i
sofsum **= 2



print(s, sofsum, sofsum - s)