"""
/step/1
s = 'Python rocks!'
print(len(s))

/step/2
s = 'Python rocks!'
print(s[3])

/step/3
s = 'Python rocks!'
print(s[1:5])

/step/4
s = '    Python rocks!     '
print(s.strip())

/step/5
s = 'Python rocks!'
print(s.upper())

/step/6
s = 'Python rocks!'
print(s.replace("o", "@"))

/step/7
s = input()
new_str = ''
for i in range(len(s)):
    if i%3!=0:
        new_str += s[i]
print(new_str)

/step/8
w = input()
print(w.replace("1", "one"))

/step/9
q = input()
print(q.replace("@", ""))

/step/10
s = input()

if s.find('f')==-1:
    print(-2)
elif s.count('f')==1:
    print(-1)
else:
    new_str = s[:s.find('f')] + s[s.find('f')+1:]
    print(new_str.find('f') + 1)

/step/11
s = input()
last_idx = len(s) - s[::-1].find('h') - 1
first_idx = s.find('h')
print(s[:first_idx+1] + s[first_idx+1:last_idx][::-1] + s[last_idx:])
"""
