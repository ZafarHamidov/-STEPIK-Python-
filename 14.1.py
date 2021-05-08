"""
/step/1
2

/step/2
i
res
n

/step/3
локальной
функции
значение
переменная
локальной

/step/4
# объявление функции
def draw_triangle():
    m = 15
    for i in range(1, m + 1, 2):
        print(' ' * ((m - i) // 2) + '*' * i)

# основная программа
draw_triangle() 

/step/5
def get_shipping_cost(quantity):
    return 1000 + 120 * (quantity - 1)

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))

/step/6
from math import factorial

# объявление функции
def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))

/step/7
# объявление функции
def number_to_words(num):
    s = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто','']
    if num <= 20:
        return s[num - 1]
    else:
        return s[num // 10 - 1 + 18] + ' ' + s[num % 10 - 1]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))

/step/8
def get_month(language, number):
    monthsRu = { 1 : 'январь', 2 : 'февраль', 3 : 'март', 4 : 'апрель', 5 : 'май', 6 : 'июнь', 7 : 'июль', 8 : 'август', 9 : 'сентябрь', 10 : 'октябрь', 11 : 'ноябрь', 12 : 'декабрь'}
    monthsEn = { 1 : 'january', 2 : 'february', 3 : 'march', 4 : 'april', 5 : 'may', 6 : 'june', 7 : 'july', 8 : 'august', 9 : 'september', 10 : 'october', 11 : 'november', 12 : 'december'}
    if language == 'ru':
        return monthsRu[number]
    else:
        return monthsEn[number]
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))

/step/9
def is_magic(date):
    day, month, year = date.split('.')
    return int(day) * int(month) == int(year) % 100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))

/step/10
def is_pangram(text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in text.lower():
        if letter in letters:
            letters.remove(letter)
    return len(letters) == 0

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
"""
