# The max options we have is 40 choices we can make. Down, or left 20 times each. 
# This can be mathematically represented as 
#(40)!/((20!)(40-20)!) or 40!/(20!)^2

import math

print(math.factorial(40)/(math.factorial(20)**2))