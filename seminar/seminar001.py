# 1. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.  
# 2. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N.
# 3. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру после запятой.
# 4. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30).
  

# Задача 1

amount_of_numbers = 5
number_list = []

for i in range(amount_of_numbers):
    number_list.append(int(input("Введите число: ")))

max_number = number_list[0]
# print(max(number_list))
for number in range(1, amount_of_numbers):
    if max_number < number_list[number]:
        max_number = number_list[number]

print(max_number)

# Задача 2

n = int(input("Введите число n: "))
for i in range(-n, n + 1):
    print(i, end = ' ')

# Задача 3 

x = float(input("Введите число: "))
print(int(x * 10) % 10)

# Задача 4

a = int(input("Введите число: "))
if ((a % 5 == 0) and (a % 10 == 0)) or ((a % 15 == 0) and (a % 30 != 0)):
    print("Yes")
else:
    print("No")    