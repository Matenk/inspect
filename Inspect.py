import inspect
from pprint import pprint

class SomeClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def some_methode(self):
        return 4 + 10


some_obj = SomeClass('Jack', 30)

def introspection_info(obj):

    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        print('Метод или аттрибут + Тип: \n',attr_name, type(attr))

    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    pprint(f'Только методы: {methods}')





    get_module = inspect.getmodule(some_obj)
    print(f'Путь к объекту: {get_module}.')



introspection_info(some_obj)

