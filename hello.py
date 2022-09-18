# типы данных и переменная
# int, float, boolen, str, list, None
value =None
a = 123
b = 1.23
print(a)
print(b)
value = 12334
print(value)
s = 'hello world' # введение переменной строки (str)

print(s) # вывод строки
print(a, '-',b, '-',s)
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True # Логическая переменная
print(f)

# В языке PYTHON нет массивов, но  зато есть списки.
list = ['1', '2', '3']
print(list)

# Ввод и вывод данных
# print, input

#print('Введите a')
#a = int(input())   # Перед операцией указываем тип переменной
#print('Введите b')
#b = int(input())
#print(a, ' + ' , b, ' = ', a+b)
#print('{} {}'.format(a,b))
#print(f'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **
# **,  
# (), Сокращенные операции
a = 1.3
b = 3
c = round(a * b, 3) # 3 - количество знаков после запятой, функция ROUND - позволяет округлить значение до целых чисел.
print(c)
# Логические операции 
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in
# gen

f = [1,2,3,4]
print(f)
print(not 2 in f)

# Управляющие конструкции
# if, if-else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)    

# Управляющие конструкции: WHILE

original = 16896 # конвертируем перевернутое число
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)    

# Управляющие конструкции: WHILE-ELSE

original = 16896 # конвертируем перевернутое число
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')    
print(inverted)

# Управляющие конструкции: FOR

for i in 1,2,3,4,5,6:
    print(i**2)


# ФУНКЦИИ

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))               

# НЕМНОГО О СТРОКАХ

text = 'съешь ещё этих мягких французских булок'
print(len(text))                    # 39
print('ещё' in text)                # True
print(text.isdigit())               # False
print(text.islower())               # True
print(text.replace('ещё','ЕЩЁ'))
print(text[0])   # с
print(text[1])   # ъ
print(text[len(text)])  # IndexError
print(text[len(text)-1])  # к
print(text[-5])  #  б
print(text[:])   # print(text)
print(text[:2])  # съ
print(text[len(text)-2:]) # ок
print(text[2:9])  # ешь ещё
print(text[6:-18])  # ещё этих мягких 
print(text[0:len(text):6])   # сеикакл
print(text[::6])  # сеикакл
text = text[2:9] + text[-5] + text[:2]

for c in text:
    print(c)

# СПИСКИ: ВВЕДЕНИЕ

numbers = [1, 2, 3, 4, 5]
print(numbers)              # [1, 2, 3, 4, 5]
ran = range(1, 6)
numbers = list(ran)
print(numbers)              # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)              # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i)                # [20, 4, 6, 8, 10]
print(numbers)              # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']

for e in colors:
    print(e)   # red green blue

for e in colors:
    print(e*2)    # redred greengreen blueblue

colors.append('gray')  # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray'])  # TRUE
colors.remove('red')  # del colors[0] # удалить элемент