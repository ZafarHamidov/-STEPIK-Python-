"""
/step/2
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
print(sum([i**2 for i in numbers]))

/step/3
n = int(input())
l = [int(input()) for _ in range(n)]
output = [(x**2 + 2*x + 1) for x in l]
print(*l, sep='\n')
print()
print(*output, sep='\n')

/step/4
n = int(input())
l = [int(input()) for _ in range(n)]
l.remove(max(l))
l.remove(min(l))
print(*l, sep='\n')

/step/5
n = int(input())
l = list()
for i in range(n):
    s = input()
    if s not in l:
        l.append(s)
print(*l, sep='\n')

/step/6
n = int(input())
l = [input() for _ in range(n)]
search = input()
output = []
for i in l:
    if search.lower() in i.lower():
        output.append(i)
        
print(*output, sep = '\n')

/step/7
s = [input() for _ in range(int(input()))]
d = [input() for _ in range(int(input()))]
for i in s:
    for j in d:
        if j.lower() not in i.lower():
            break
    else:
        print(i)
        
/step/8
a, b, c = list(), list(), list()
for _ in range(int(input())):
    n = int(input())
    if n > 0:
        a.append(n)
    elif n < 0:
        b.append(n)
    elif n == 0:
        c.append(n)
print(*b, sep='\n')
print(*c, sep='\n')
print(*a, sep='\n')
"""
