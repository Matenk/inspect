import inspect
from pprint import pprint
class SomeClass:
    def init(self):
        self.attribute = 30

    def some_methode(self):
        return self.attribute + 10

some_obj = SomeClass()

def introspection_info(obj):

    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        print(dict(Аттрибут=attr_name, Тип=type(attr)))

    get_method = inspect.getmembers(some_obj)
    get_module = inspect.getmodule(some_obj)
    print(f'Путь к объекту: {get_module}.')
    pprint(dict(Методы_объекта=get_method))




introspection_info(some_obj)
