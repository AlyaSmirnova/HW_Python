def find(surname): # пишем функцию по поиску, принимает фамилию (которую ввел пользователь для поиска)
    with open('example.txt', 'r', encoding='utf-8') as file: # открываем файл для чтения
        while True: # пока у нас будут строки 
            line = file.readline() # считываем файл по строке
            if not line:
                break # прерываем цикл, если линия пустая
            if line[:-1] == surname: # если строка равна введенному пользователем surname (-1 нужен, чтобы не учитывать \n)
                print(line) # выводим эту строку и 3 следующих
                print(file.readline())
                print(file.readline())
                print(file.readline())