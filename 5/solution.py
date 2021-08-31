import sympy

cap = 20
hit = False

check_list = [11, 13, 14, 16, 17, 18, 19, 20]

for i in range(20, 999999999, 20):
    if all(i % n == 0 for n in check_list):
        print(i)
        break

print("None found")
