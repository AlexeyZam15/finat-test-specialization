from aux_modules.catsbreedcheck import CatsBreedCheck
from classes.pets import Pet


class Cat(Pet):
    def __init__(self, name: str, birthday: str, learned_commands: str, breed: str):
        super().__init__(name, birthday, learned_commands)
        CatsBreedCheck().is_cat_breed(breed)
        self.__breed = breed

    @property
    def breed(self):
        return self.breed

    def __str__(self):
        return f'''{super().__str__()}
Порода: {self.__breed}'''
