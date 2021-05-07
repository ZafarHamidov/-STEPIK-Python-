"""
/step/2
6

/step/3
True

/step/4
False

/step/5
8

/step/6
I learn Python language

/step/7
123cd123123a

/step/8
n = input()
s = n.strip()
z = s.count(" ")
print(z + 1)

/step/9
n = input()
z = n.lower()
if z == "a" or "г" or "ц" or "т":
    print("Аденин:", z.count("а"))
    print("Гуанин:", z.count("г"))
    print("Цитозин:", z.count("ц"))
    print("Тимин:", z.count("т"))
    
/step/10
n = int(input())
strings = [input() for i in range(n)]
counter = 0

for s in strings:
    if s.count('11')>2:
        counter += 1
        
print(counter)

/step/11
s = input()
counter = 0
for i in s:
    if i.isdigit():
        counter += 1

print(counter)

/step/12
n = input()
if n.endswith(".ru") or n.endswith(".com"):
    print("YES")
else:
    print("NO")
    
/step/13
s = input()[::-1]; l = [s.count(i) for i in s]; print(s[l.index(max(l))])

/step/14
s = input()

if s.find('f')==-1:
    print('NO')
elif s.count('f')==1:
    print(s.find('f'))
else:
    print(str(s.find('f')) + ' ' + str(len(s) - s[::-1].find('f') - 1))
    
/step/15
st = input()
first = st.find('h')
last = st.rfind('h')
st = st[:first] + st[(last + 1):]
print(st)
"""
