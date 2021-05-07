"""
/step/3
Произойдет ошибка TypeError

/step/4
a = int(input())
b = int(input())
chr1 = 0
for i in range(a,b + 1):
    print(chr(i), end=' ')
    
/step/5
s = input()
for i in s:
    print(ord(i), end=' ')
    
/step/6
n = int(input())
a = input()
for i in a:
    k = ord(i)-n
    if k < 97:
        k = k + 26
    print(chr(k), end = '')
"""
