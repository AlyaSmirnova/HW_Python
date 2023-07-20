# Задача 34. Про Винни-Пуха

# stroka = input('Введите строку: ')
# list_1 = stroka.split() # разбиваем строку на элементы по пробелу в список
# print(list_1)

# glas = ['а', 'е', 'о', 'э', 'и', 'у', 'ы', 'я', 'ю', 'ё']
# res_list = [] # создали пустой список, в который будем класть результат

# for item in list_1: # проходимся по всем элементам списка первоначального
#     counter = 0 # вводим счетчик, который считает количество гласных букв в каждом элементе
#     for letter in item: # проходимся по каждой букве элемента
#         if letter in glas: # если эта буква есть в списке glas
#             counter += 1 # увеличиваем счетчик на 1
#     res_list.append(counter)
# print(res_list)

# if len(set(res_list)) == 1: # из res_list сделали множество, чтобы убрать повторяющиеся значения
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# Задача 36. 

# def print_operation_table(operation, num_rows = 6, num_columns = 6):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f"{x:>3}" for x in i])

# print_operation_table(lambda x, y: x * y)