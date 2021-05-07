"""
/step/2
cde

/step/3
defg

/step/4
abc

/step/5
abcdefg

/step/6
gda

/step/7
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])

/step/8
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])

/step/9
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])

/step/10
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

/step/11
n = input()
if n[::-1] == n[:]:
    print("YES")
else:
    print("NO")
    
/step/12
s = input()
print(len(s), s * 3, s[0], s[0:3], s[-3:], s[::-1], s[1:-1], sep='\n')

/step/13
n = input()
print(n[2:3])
print(n[-2:-1])
print(n[:5])
print(n[:-2])
print(n[::2])
print(n[1::2])
print(n[::-1])
print(n[-1::-2])

/step/14
from math import *
s = input()
i = ceil(len(s)/2)
print(s[i:]+s[:i])
"""
