from datetime import date

from aux_modules.dogsbreedcheck import DogsBreedCheck
from classes.pets import Pet


class Dog(Pet):
    def __init__(self, name: str, birthday: str, learned_commands: str, breed: str):
        super().__init__(name, birthday, learned_commands)
        DogsBreedCheck().is_dog_breed(breed)
        self.__breed = breed

    @property
    def breed(self):
        return self.breed

    def __str__(self):
        return f'''{super().__str__()}
Порода: {self.__breed}'''
