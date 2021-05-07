"""
/step/2
B**E**E**G**E**E**K

/step/3
s = input()
print(*(s.split(' ')), sep='\n')

/step/4
s = input()
print('.'.join([i[0] for i in s.split(' ')]) + '.')

/step/5
s = input()
print(*s.split('\\'), sep='\n')

/step/6
for i in input().split():
    print('+' * int(i))
    
/step/7
l = input().split('.')
flag = True

for elem in l:
    if int(elem)>255:
        flag = False
if flag:
    print('ДА')
else:
    print('НЕТ')
    
/step/8
s = input()
separator = input()
print(separator.join([i for i in s]))

/step/9
s = input()
l = s.split(' ')
counter = 0
for i in range(len(l)):
    for j in range(i, len(l)):
        if i!=j and l[i]==l[j]:
            counter += 1
print(counter)
"""
