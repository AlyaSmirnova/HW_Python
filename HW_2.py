# Задача 10. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input('Введите количество монеток на столе: '))
# sum = 0 # сюда записываем количество монеток, которые перевернем
# for i in range(n): # проходимся по всем n монеткам + допускаем, что сторона решки - это 1
#     m = int(input('Ввведите 1 или 0 для определения стороны монетки: '))
#     if m == 0: 
#         sum += 1
# print(sum)

# Задача 12.  Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# sum = int(input('Ввведите результат суммы двух чисел: '))
# mult = int(input('Введите результат произведения двух чисел: '))
# for i in range(sum): # проходимся по всем числам в диапазоне sum
#     for j in range(mult): # проходимся по всем числам в диапазоне mult
#         if sum == i + j and mult == i * j:
#             print(i, j)

# Задача 14. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число: '))
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1