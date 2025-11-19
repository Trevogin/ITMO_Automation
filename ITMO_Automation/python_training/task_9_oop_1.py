# Создайте класс Input, принимающий 1 аргумент при инициализации (Loc)
# Создайте объект search (экземпляр класса Input)
# Выведите в консоль значение аргумента Loc, объекта search

class Input:

    def __init__(self, loc):
        self.loc = loc

search = Input('input#search')

print (search.loc)