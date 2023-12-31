from aux_modules.datecheck import DateCheck


class ParentClass:
    date_col = 3
    __id_counter = 0

    input_fields = ["Имя", "Дата рождения"]

    fields_names_ids = {"Id": "Id",
                        "Имя": "name",
                        "Дата рождения": "birthday",
                        "Класс": "class_name",
                        "Порода": "breed",
                        "Выученные команды": "learned_commands"}

    required_input_fields = ["name", "birthday", "breed", "learned_commands"]

    field_width = {"Id": 3,
                   "Имя": 4,
                   "Дата рождения": 14,
                   "Класс": 13,
                   "Порода": 13,
                   "Выученные команды": 13}

    def __init__(self, name: str, birthday: str):
        if not name:
            raise ValueError("Имя не может быть пустым")
        birthday = DateCheck.is_date(birthday)
        ParentClass.__id_counter += 1
        self.__id = ParentClass.__id_counter
        if len(self.__id.__str__()) > ParentClass.field_width["Id"] - 1:
            ParentClass.field_width["Id"] = len(self.__id.__str__()) + 1
        self.__name = name
        if len(self.__name) > ParentClass.field_width["Имя"] - 1:
            ParentClass.field_width["Имя"] = len(self.__name) + 1
        self.__birthday = birthday
        if len(self.__birthday) > ParentClass.field_width["Дата рождения"] - 1:
            ParentClass.field_width["Дата рождения"] = len(self.__name) + 1
        self.__class_name = "Не определено"
        self.__breed = "Не определено"
        self.__learned_commands = ""

    def __str__(self):
        text = " ".join([f'{i:{ParentClass.field_width[i]}}' for i in ParentClass.field_width])
        text += (((f'\n{self.Id:{ParentClass.field_width["Id"]}}|{self.name:{ParentClass.field_width["Имя"]}}|'
                   + f'{self.birthday:{ParentClass.field_width["Дата рождения"]}}|')
                  + f'{self.class_name:{ParentClass.field_width["Класс"]}}|{self.breed:{ParentClass.field_width["Порода"]}}|')
                 + f'{self.learned_commands:{ParentClass.field_width["Выученные команды"]}}')
        return text

    def get_fields(self):
        return [(f'{self.Id}', f'{self.name}',
                 f'{DateCheck.change_date_format(self.birthday)}',
                 f'{self.class_name}', f'{self.breed}',
                 f'{self.learned_commands}')]

    @property
    def name(self):
        return self.__name

    @property
    def birthday(self):
        return self.__birthday

    @property
    def Id(self):
        return self.__id

    @property
    def learned_commands(self):
        return self.__learned_commands

    @learned_commands.setter
    def learned_commands(self, new_value):
        self.__learned_commands = new_value

    @property
    def breed(self):
        return self.__breed

    @property
    def class_name(self):
        return self.__class_name

    @class_name.setter
    def class_name(self, new_name: str):
        self.__class_name = new_name
        if len(self.__class_name) > ParentClass.field_width["Класс"] - 1:
            ParentClass.field_width["Класс"] = len(self.__class_name) + 1

    @staticmethod
    def id_counter_reset():
        ParentClass.__id_counter = 0
