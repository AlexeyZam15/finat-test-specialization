from aux_modules.horsesbreedcheck import HorsesBreedCheck
from classes.pack_animals import PackAnimal


class Horse(PackAnimal):
    def __init__(self, name: str, birthday: str, capacity_kg: int, breed: str):
        super().__init__(name, birthday, capacity_kg)
        HorsesBreedCheck().is_horse_breed(breed)
        self.__breed = breed

    @property
    def breed(self):
        return self.breed

    def __str__(self):
        return f'''{super().__str__()}
Порода: {self.__breed}'''
