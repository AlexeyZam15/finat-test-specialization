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

        self.__actions = {'1': 'список животных',
                          '2': 'добавить животное',
                          '3': 'обучить команде'}

        self.__functions = {'1': self.show_all,
                            '2': self.add_new,
                            '3': self.teach_command}

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

        self.__child_classes_ratio = {"верблюд": Camel,
                                      "лошадь": Horse,
                                      "осёл": Donkey,
                                      "кошка": Cat,
                                      "собака": Dog,
                                      "хомяк": Hamster,
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

    def __read_data_clv(self):
        with open(self.__path, mode='r', encoding='utf-8') as file:
            data_lines = file.read().splitlines()
            if len(data_lines) > 1:
                for line in data_lines[1:]:
                    try:
                        data = line.split(";")
                        if data[3] != "Не определено":
                            self.create_child(self.__child_classes_ratio[data[3]], data[1:3] + data[4:6])
                        else:
                            self.create_child(ParentClass, data[1:3] + data[4:6])
                    except Exception as e:
                        raise IOError(f"Ошибка с чтением данных из csv файла {self.__path}")

    def start(self):
        self.__data = Data(list[ParentClass]())
        open(self.__path, mode="a")
        print("Программа реестра животных запущена")
        self.__read_data_clv()
        action = True
        while action:
            action = self.__choose_input(self.__actions, self.__functions, 'Какое действие хотите совершить?')
        if not action:
            return False

    def show_all(self):
        print(*[f'{i:{ParentClass.field_width[i]}}' for i in ParentClass.field_width])
        for i in self.__data:
            print(f'{i.id:{ParentClass.field_width["Id"]}}|{i.name:{ParentClass.field_width["Имя"]}}|'
                  f'{i.birthday:{ParentClass.field_width["Дата рождения"]}}|'
                  f'{i.class_name:{ParentClass.field_width["Класс"]}}|{i.breed:{ParentClass.field_width["Порода"]}}|'
                  f'{i.learned_commands:{ParentClass.field_width["Выученные команды"]}}')

    def add_new(self):
        action = self.__choose_input(self.__child_classes_names, self.__child_classes_functions,
                                     'Выберите класс нового животного:', self.__child_classes_parameters)

    @staticmethod
    def __input_fields(input_fields: list):
        print('Заполните поля:')
        data = []
        for i in range(len(input_fields)):
            data.append(input(f'{input_fields[i]}: '))
        return data

    def create_child(self, class_name, data: list = None):
        if not data:
            data = self.__input_fields(class_name.input_fields)
        child = class_name(*data)
        self.__data.append(child)
        with open(self.__path, mode='w', encoding="utf-8") as data:
            content = '"Id";"Имя";"Дата рождения";"Класс";"Порода";"Выученные команды"\n'
            for i in self.__data:
                content += f"{i.id};{i.name};{i.birthday};{i.class_name};{i.breed};{i.learned_commands}\n"
            data.write(content)

    def teach_command(self):
        id_value = input("Введите id животного, которого хотите научить команде: ")
        animal: ParentClass = self.__data.get_by_param("id", id_value)
        if animal:
            command = input("Введите название новой команды: ")
            print(animal.learned_commands)
            animal.learned_commands += f", {command}"
        else:
            print('Введён неверный id')

