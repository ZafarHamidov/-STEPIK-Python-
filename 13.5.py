"""
/step/2
def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))

/step/3
def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))

/step/4
# объявление функции
def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))

/step/5
# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for c in password:
        if c.isupper():
            flag1 = True
        elif c.islower():
            flag2 = True
        elif c.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3 

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))

/step/6
def is_one_away(word1, word2):
    counter = 0
    
    if len(word1) != len(word2):
        return False
    else:
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                counter += 1
        if counter == 1:
            return True
        else:
            return False

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))

/step/7
# объявление функции
def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

/step/8
def is_valid_password(password):
    a, b, c = password[0], password [1], password[2]
    if len(password) != 3:
        return False
    isSimple = True
    for i in range(2, int(b)):
        if int(b)%i==0:
            isSimple = False
    if a == a[::-1] and int(c)%2 == 0 and isSimple:
        return True
    else:
        return False

# считываем данные
psw=input().split(':')

# вызываем функцию
print(is_valid_password(psw))

/step/9
def is_correct_bracket(text):
    openBrackets = 0
    for elem in text:
        if elem == '(':
            openBrackets += 1
        elif elem == ')':
            if openBrackets==0:
                return False
            else:
                openBrackets -= 1
    if openBrackets == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))

/step/10
def convert_to_python_case(text):
    s = ''
    for elem in text:
        if elem.isupper():
            if s == '':
                s += elem.lower()
            else:
                s += '_' + elem.lower()
        else:
            s += elem
    return s

text = input()

print(convert_to_python_case(text))
"""
