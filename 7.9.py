"""
/step/1
n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i

l = [i for i in range(1, sum+1)]    
counter = 0

for i in range(1, n+1):
    s = []
    for j in range(i):
        s.append(l[counter + j])
    counter += i
    print(*s)
    
/step/2
n = int(input())

for i in range(1, n+1):
    l = [str(j) for j in range(1, i)]
    l.extend([str(j) for j in range(i, 0, -1)])
    print(''.join(l))
    
/step/3
a, b = int(input()), int(input())
sum, bigsum, num, bignum = 0, 0, 0, 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i // j == i / j:
            sum += j
            num = i
    if sum > bigsum:
        bignum = num
        bigsum = sum
    if sum == bigsum:
        bignum = max(num, bignum)
        bigsum = sum
    num, sum = 0, 0
print(bignum, bigsum)

/step/4
n = int(input())

for i in range(1, n+1):
    counter = 0
    for j in range(1, i+1):
        if i%j==0:
            counter += 1
    print(str(i) + '+'*counter)
    
/step/5
n = int(input())
sum = 0

while n > 9:
    while n/10!=0:
        sum += n%10
        n //= 10
    n = sum
    sum = 0
    
print(n)

/step/6
def factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum


n = int(input())
l = [factorial(i) for i in range(1, n+1)]
print(sum(l))

/step/7
a, b = [int(input()) for i in range(2)]

for i in range(a, b+1):
    counter = 0
    for j in range(1, i):
        if i%j==0:
            counter += 1
    if counter == 1:
        print(i)

"""
