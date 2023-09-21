from aux_modules.camelsbreedcheck import CamelsBreedCheck
from classes.pack_animals import PackAnimal


class Camel(PackAnimal):
    __name = "Верблюд"

    input_fields = PackAnimal.input_fields + ['порода']

    def __init__(self, name: str, birthday: str, learned_commands: str, breed: str):
        super().__init__(name, birthday, learned_commands)
        CamelsBreedCheck().is_camel_breed(breed)
        self.__breed = breed

    @property
    def breed(self):
        return self.breed

    def __str__(self):
        return f'''{super().__str__()}
Порода: {self.__breed}'''

    @property
    def name(self):
        return self.__name
