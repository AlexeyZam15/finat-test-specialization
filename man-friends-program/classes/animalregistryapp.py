from classes.camels import Camel
from classes.cats import Cat
from classes.dogs import Dog
from classes.donkeys import Donkey
from classes.hamsters import Hamster
from classes.horses import Horse
from classes.parentclass import ParentClass
from aux_modules.counter import Counter
from classes.data import Data
from aux_modules.filemanager import FileManager
from sqlconnect import SQLConnect
import datetime


class AnimalRegistryApp:
    def __init__(self, sql_connect: SQLConnect, csv_file: str, view_class_name):
        self.__sql_connect = sql_connect
        self.__view = None
        self.__data = Data(list[ParentClass]())

        self.__view_class_name = view_class_name

        self.__actions = {'1': 'список животных',
                          '2': 'добавить животное',
                          '3': 'обучить команде'}

        self.__functions = {'1': self.__show_all,
                            '2': self.__add_new,
                            '3': self.__teach_command}

        try:
            self.__file_manager = FileManager(csv_file)
        except:
            raise IOError("Ошибка работы с файлом " + csv_file)

        self.__child_classes_names = {"1": "Верблюд",
                                      "2": "Лошадь",
                                      "3": "Осёл",
                                      "4": "Кошка",
                                      "5": "Собака",
                                      "6": "Хомяк",
                                      }

        self.__child_classes_functions = {"1": self.__create_child,
                                          "2": self.__create_child,
                                          "3": self.__create_child,
                                          "4": self.__create_child,
                                          "5": self.__create_child,
                                          "6": self.__create_child
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

        self.counter = Counter()

        self.__title = "Реестр животных"

    def start(self):
        self.__view = self.__view_class_name()
        self.__view.set_program_title(self.__title)
        self.__data = Data(list[ParentClass]())
        ParentClass.id_counter_reset()
        self.__create_objects_from_sql(self.__create_child, self.__child_classes_ratio, ParentClass)
        self.__show_all()
        # self.__file_manager.create_objects_from_clv(self.__create_child, self.__child_classes_ratio, ParentClass)
        # action = True
        # while action:
        #     action = self.__view.choose_input(self.__actions, self.__functions, 'Какое действие хотите совершить?')
        # if not action:
        #     return False
        return False

    def __show_all(self):
        if len(self.__data):
            text = " ".join([f'{i:{ParentClass.field_width[i]}}' for i in ParentClass.field_width])
            for i in self.__data:
                text += (f'\n{i.Id:{ParentClass.field_width["Id"]}}|{i.name:{ParentClass.field_width["Имя"]}}|' +
                         f'{i.birthday:{ParentClass.field_width["Дата рождения"]}}|' +
                         f'{i.class_name:{ParentClass.field_width["Класс"]}}|{i.breed:{ParentClass.field_width["Порода"]}}|' +
                         f'{i.learned_commands:{ParentClass.field_width["Выученные команды"]}}')
            self.__view.print_msg(text)
        else:
            self.__view.print_msg("Список животных пуст")

    def __add_new(self):
        action = self.__view.choose_input(self.__child_classes_names, self.__child_classes_functions,
                                          'Выберите класс нового животного:', self.__child_classes_parameters)

    def __input_fields(self, input_fields: list):
        self.__view.print_msg('Заполните поля:')
        data = []
        for i in range(len(input_fields)):
            data.append(self.__view.input_func(f'{input_fields[i]}: '))
        return data

    def __create_child(self, class_name, data: list = None):
        if not data:
            data = self.__input_fields(class_name.input_fields)
        child = class_name(*data)

        with self.counter as cnt:
            cnt.add()

        self.__data.append(child)

        self.__file_manager.write_data_to_file(self.__data, ParentClass.fields_names_ids.keys(),
                                               ParentClass.fields_names_ids.values())
        # self.__sql_connect.import_data()

    def __teach_command(self):
        id_value = self.__view.input_func("Введите id животного, которого хотите научить команде: ")
        animal: ParentClass = self.__data.get_by_param("Id", id_value)
        if animal:
            command = self.__view.input_func("Введите название новой команды: ")
            if animal.learned_commands:
                animal.learned_commands += f", {command}"
            else:
                animal.learned_commands = f"{command}"
        else:
            self.__view.print_msg('Введён неверный id')
        self.__file_manager.write_data_to_file(self.__data, ParentClass.fields_names_ids.keys(),
                                               ParentClass.fields_names_ids.values())

    def __create_objects_from_sql(self, create_object_func, name_class_ratio, exception_class):
        sql_data = self.__sql_connect.execute(f"SELECT * FROM {self.__sql_connect.main_table}")
        for data in sql_data:
            try:
                if data[3] != "Не определено":
                    create_object_func(name_class_ratio[data[3]], data[1:3] + data[4:6])
                else:
                    create_object_func(exception_class, data[1:3] + data[4:6])
            except Exception as e:
                raise IOError(f"Ошибка с чтением данных из "
                              f"таблицы {self.__sql_connect.main_table} базы данных {self.__sql_connect.database}")
