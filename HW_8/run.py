# это файл, куда собираем весь алгоритм нужных функций
from user import choose_mode # импортировали функцию choose_mode из файла user.py
from filling_dictionary import filling
from search import find

def running():
    person, mode = choose_mode() # сначала запускаем эту функцию, которая спрашивает у пользователя режим
    # нам возвращаются данные и мы их записываем в переменную person
    if mode == 'запись':
        filling(person) # вызываем функцию filling, в которую передаем person
    else:
        find(person)# функцию по поиску