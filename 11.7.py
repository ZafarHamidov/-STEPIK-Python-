"""
/step/2
[выражение for переменная in последовательность]

/step/3
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [i[1:] for i in keywords]
print(new_keywords)

/step/4
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(i) for i in keywords]
print(lengths)

/step/5
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [i for i in keywords if len(i)>4]
print(new_keywords)

/step/6
palindromes = [i for i in range(100, 1001) if str(i)==str(i)[::-1]]
print(palindromes)

/step/7
n = int(input())
print(*[i**2 for i in range(1, n+1)], sep='\n')

/step/8
input = input().split(' ')
print(*[int(i)**3 for i in input])

/step/9
s = input().split(' ')
print(*s, sep='\n')

/step/10
s = input()
print(*[i for i in s if i.isdigit()], sep='')

/step/11
s = input().split()
print(*[int(i)**2 for i in s if int(i)%2==0 and int(i)**2%10!=4])
"""
