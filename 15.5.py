"""
/step/2
нет

/step/3
ROT 13

/step/5
Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!

/step/6
Kf sv, fi efk kf sv, kyrk zj kyv hlvjkzfe!

/step/7
Скупой теряет все, желая все достать.

/step/8
The grass is always greener on the other side of the fence.

/step/9
Learn to walk before you run.

/step/10
FIRST_SYM = 'a'
LAST_SYM = 'z'
FIRST_SYM_CAPS = 'A'
LAST_SYM_CAPS = 'Z'


def cifer(str, alph, shift):
    result = ''
    for sym in str:
        if (ord(sym) + shift in range(ord(FIRST_SYM), ord(LAST_SYM) + 1) and ord(sym) in range(ord(FIRST_SYM), ord(LAST_SYM) + 1)) or (ord(sym) + shift in range(ord(FIRST_SYM_CAPS), ord(LAST_SYM_CAPS) + 1) and ord(sym) in range(ord(FIRST_SYM_CAPS), ord(LAST_SYM_CAPS) + 1)):
            result += chr(ord(sym) + shift)
        elif ord(sym) in range(ord(FIRST_SYM), ord(LAST_SYM) + 1) or ord(sym) in range(ord(FIRST_SYM_CAPS), ord(LAST_SYM_CAPS) + 1):
            result += chr(ord(sym) + shift - alph)
        else:
            result += sym
    return result

def letter_in_string(str):
    count = 0
    for a in str: 
        if (a.isalpha()) == True: 
            count+=1
    return count 

input_str = input()

result = ''

for elem in input_str.split(' '):
    result += cifer(elem, 26, letter_in_string(elem))
    result += ' '
    
print(result)
"""
