from classes.parentclass import ParentClass


class PackAnimal(ParentClass):
    def __init__(self, name: str, birthday: str, capacity_kg: int):
        super().__init__(name, birthday)
        if not isinstance(capacity_kg, int):
            raise ValueError("Грузоподъёмность не является числом")
        self.__capacity_kg = capacity_kg

    @property
    def capacity_kg(self):
        return self.__capacity_kg

    def __str__(self):
        return f'''{super().__str__()}
Грузоподъёмность: {self.__capacity_kg} кг'''
