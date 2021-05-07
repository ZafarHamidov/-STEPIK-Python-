"""
/step/1
print([i for i in range(2, int(input())+1, 2)])

/step/2
'''list + list'''
l, m = input().split(), input().split()
print(*(int(l[i]) + int(m[i]) for i in range(len(l))))

/step/3
l = [i for i in input().split()]
s = '+'.join(l)
s += '=' + str(sum([int(i) for i in l]))
print(s)

/step/4
n = input().split("-")
c = [len(i) for i in n] 
if c == [3, 3, 4] and ''.join(n).isdigit(): 
    print("YES")
elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7': 
    print("YES")
else:
    print("NO")
    
/step/5
l = input().split()
print(max([len(i) for i in l]))

/step/6
l = input().split()
print(*[i[1:] + i[0] + 'ки' for i in l])
"""
