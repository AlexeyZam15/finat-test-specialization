from aux_modules.datecheck import DateCheck


class ParentClass:
    __id_counter = 0

    def __init__(self, name: str, birthday: str):
        self.__id_counter += 1
        self.__id = self.__id_counter
        self.__name = name
        DateCheck.is_date(birthday)
        self.__birthday = birthday

    def __str__(self):
        return f'''Id: {self.__id}
Имя: {self.__name}
Дата рождения: {self.__birthday}'''

    @property
    def name(self):
        return self.__name

    @property
    def birthday(self):
        return self.__birthday

    @property
    def id(self):
        return self.__id
