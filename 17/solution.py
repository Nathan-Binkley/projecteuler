from num2words import num2words
a = ""

for i in range(1,1001):
    p = num2words(i)
    p = p.replace("-", "")
    p = p.replace(" ", "")
    a += p
print(a)
print(len(a))