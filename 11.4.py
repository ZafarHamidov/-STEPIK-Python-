"""
/step/2
names.append('Chromatica')

/step/3
[4, 2, 8, 6, 5, 7, 1]

/step/4
[4, 2, 1, 2, 3, 7, 17, 777]

/step/5
['red', 'orange', 'green', 'blue', 'purple', 'brown']

/step/6
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])        
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)

/step/7
n = int(input())
l = []
for i in range(n):
    l.append(input())
    
print(l)

/step/8
start = ord('a')
l = []

for i in range(26):
    l.append(chr(start+i)*(i+1))
    
print(l)

/step/9
n = int(input())
l = []
for i in range(1, n+1):
    l.append(int(input())**3)
print(l)

/step/10
n = int(input())
l = []
for i in range(1, n+1):
    if n%i==0:
        l.append(i)   
print(l)

/step/11
n = int(input())
l = [int(input()) for _ in range(n)]
output = []
for i in range(len(l)-1):
    output.append(l[i] + l[i+1])
print(output)

/step/12
a = [int(i) for i in [input() for _ in range(int(input()))]]
del a[1::2]
print(a)

/step/13
n = int(input())
li = []
for _ in range(n):
    li.append(input())
index = int(input())    
res = ''
for s in li:
    if len(s) >= index:
        res += s[index - 1]
print(res)

/step/14
n = int(input())
s = ''
for i in range(n):
    s += input()
print([i for i in s])
"""
