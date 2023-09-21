from classes.parentclass import ParentClass


class Pet(ParentClass):
    input_fields = ParentClass.input_fields + ["Выученные команды", "Порода"]

    def __init__(self, name: str, birthday: str, learned_commands: str):
        super().__init__(name, birthday)
        self.__learned_commands = learned_commands

    @property
    def learned_commands(self):
        return self.__learned_commands
