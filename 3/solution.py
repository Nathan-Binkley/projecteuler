import math

number = 600851475143

# we know number is odd

sol = 0

for i in range(3, int(math.sqrt(number))+1, 2):
    while number % i == 0:
        if sol < i:
            sol = i
        number = number / i

print(sol)