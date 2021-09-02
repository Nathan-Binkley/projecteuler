import sys, os

for i in range(99, 201):
    os.system(f'mkdir C:\\Users\\nbink\\Documents\\GitHub\\projecteuler\\{i}')
    f = open(f'C:/Users/nbink/Documents/GitHub/projecteuler/{i}/description.txt', "x")
    f.write("")
    f.close()
    f = open(f'C:/Users/nbink/Documents/GitHub/projecteuler/{i}/solution.py', "x")
    f.write("")
    f.close()
