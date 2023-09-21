from classes.parentclass import ParentClass


class Pet(ParentClass):
    def __init__(self, name: str, birthday: str, learned_commands: str):
        super().__init__(name, birthday)
        self.__learned_commands = learned_commands
        self.__input_fields = self.input_fields + ["выученные команды"]

    @property
    def learned_commands(self):
        return self.__learned_commands

    def __str__(self):
        return f'''{super().__str__()}
Выученные команды: {self.__learned_commands}'''
