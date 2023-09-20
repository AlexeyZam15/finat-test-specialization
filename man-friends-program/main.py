from classes.camels import Camel
from classes.cats import Cat
from classes.dogs import Dog
from classes.hamsters import Hamster


def main():
    dog1 = Dog("Шарик", "15.04.1998", "Голос, фас, апорт", "Азавак")
    cat1 = Cat("Матроскин", "15.04.1998", "Голос, фу", "Абиссинская")
    hamster1 = Hamster("Хоми", "15.04.1998", "Голос", "Джунгарская")
    camel1 = Camel("Верблюд1", "15.04.1998", "Голос", "одногорбый верблюд")
    print(camel1)


if __name__ == '__main__':
    main()
