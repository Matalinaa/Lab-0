# Игнатьева Алёна ПИ 1-1. Упражнение 10 - Арифметика

from math import log10

# Запрашиваем у пользователя 2 целых числа

print ("Введите первое число:")
a = int(input())

print ("Введите второе число:")
b = int(input())

# Вывод на экран следующих математических операций:

summa = a + b    # Сумма a и b
print (summa)

dif = abs(a - b)    # Разница между a и b
print (dif)

proiz = a * b    # Произведение a и b
print (proiz)

ch_del = a / b    # Частное от деления a на b
print (ch_del)

ost_del = a % b    # Остаток от деления a на b
print (ost_del)

log = log10(a)    # Десятичный логарифм числа a
print (log)

st = a ** b    # Результат возведения числа а в степень b
print (st)
