"""
/step/3
20

/step/4
16

/step/5
6

/step/6
def convert_to_miles(km):
    return km * 0.6214

# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))

/step/7
def get_days(month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month==2:
        return 28
    else:
        return 31

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))

/step/8
def get_factors(num):
    l = []
    for i in range(1, num+1):
        if num%i==0:
            l.append(i)
    return l

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))

/step/9
def number_of_factors(num):
    l = []
    for i in range(1, num+1):
        if num%i==0:
            l.append(i)
    return len(l)

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))

/step/10
def find_all(target, symbol):
    l = []
    for i in range(len(target)):
        if target[i] == symbol:
            l.append(i)
    return l

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))

/step/11
def merge(list1, list2):
    list1.extend(list2)
    list1.sort()
    l = list1
    return l

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))

/step/13
if __name__ == "__main__":
	n = int(input())
	l = []
	for i in range(n):
		l.extend(input().split())
	l2  = [int(i) for i in l]
	l2.sort()
	print(*l2)
"""
