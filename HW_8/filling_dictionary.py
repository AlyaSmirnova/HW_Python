def filling(person): # функция принимает кортеж с данными
    with open('example.txt', 'a', encoding='utf-8') as file: # открываем файл для дозаписи
        for el in person: # проходимся по данным человека и записываем их в наш файл
            file.write(el + '\n')
        file.write('\n')