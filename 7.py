# Игнатьева Алёна ПИ 1-1. Упражнение 7 - "Сумма первых n положительных чисел"

# Предлагаем пользователю ввести число

print ("Введите число:")
num = int(input())

# Считаем сумму всех натуральных положительных чисел до n

summa = num * (num + 1) / 2

# Выводим сумму на экран

print ("Сумма первых", num, "чисел равна", int(summa))
