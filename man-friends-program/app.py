from classes.camels import Camel
from classes.cats import Cat
from classes.dogs import Dog
from classes.donkeys import Donkey
from classes.hamsters import Hamster
from classes.horses import Horse
from classes.parentclass import ParentClass
from data import Data


class App:
    def __init__(self, file_path: str):
        self.__data = Data(list[ParentClass]())

        self.__actions = {'1': 'вывести список животных',
                          '2': 'завести новое животное',
                          '3': 'поиск',
                          '4': 'изменение',
                          '5': 'удаление'}

        self.__functions = {'1': self.show_all,
                            '2': self.add_new,
                            '3': self.add_new,
                            '4': self.add_new,
                            '5': self.add_new}

        self.__path = file_path

        self.__child_classes_names = {"1": "Верблюд",
                                      "2": "Лошадь",
                                      "3": "Осёл",
                                      "4": "Кошка",
                                      "5": "Собака",
                                      "6": "Хомяк",
                                      }

        self.__child_classes_functions = {"1": self.create_child,
                                          "2": self.create_child,
                                          "3": self.create_child,
                                          "4": self.create_child,
                                          "5": self.create_child,
                                          "6": self.create_child
                                          }

        self.__child_classes_parameters = {"1": Camel,
                                           "2": Horse,
                                           "3": Donkey,
                                           "4": Cat,
                                           "5": Dog,
                                           "6": Hamster,
                                           }

    def __choose_input(self, actions: dir, functions: dir, text: str, parameters: dir = None):
        action = None
        while action not in self.__actions and action != 'q':
            print(text, *[f'{i} - {actions[i]}' for i in actions], 'q - выход')
            action = input()
            if action not in self.__actions and action != 'q':
                print('Введены неверные данные')
        if action != 'q':
            if not parameters:
                functions[action]()
            else:
                functions[action](parameters[action])
        else:
            return False
        return True

    def start(self):
        open(self.__path, mode="w")
        action = True
        while action:
            action = self.__choose_input(self.__actions, self.__functions, 'Какое действие хотите совершить?')
        if not action:
            return False


    def show_all(self):
        print(self.__data)

    def add_new(self):
        action = self.__choose_input(self.__child_classes_names, self.__child_classes_functions,
                                     'Выберите класс нового животного:', self.__child_classes_parameters)

    def __input_fields(self, input_fields: list):
        print('Заполните поля:')
        data = []
        for i in range(len(input_fields)):
            data.append(input(f'{input_fields[i]}: '))
        return data

    def create_child(self, class_name):
        self.__data.append(class_name(*self.__input_fields(class_name.input_fields)))
