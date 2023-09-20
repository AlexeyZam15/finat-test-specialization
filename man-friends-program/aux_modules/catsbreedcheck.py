class CatsBreedCheck:

    def is_cat_breed(self, cat_breed_name: str):
        if cat_breed_name not in self.__cats_breeds:
            raise ValueError("Неверная порода кошки")

    __cats_breeds = """Абиссинская
Австралийский мист
Азиатская
Табби
Акринская
Американская жесткошёрстная
Американская короткошёрстная
Американский бобтейл длинношёрстный
Американский бобтейл короткошёрстный
Американский кёрл длинношёрстный
Американский кёрл короткошёрстный
Анатолийская
Аравийский мау
Балинезийская
Балийская
Бенгальская
Бомбейская
Бразильская короткошёрстная
Британская длинношёрстная
Британская короткошёрстная
Бурма
Бурманская
Бурмилла длинношёрстный
Бурмилла короткошёрстный
Гавана
Гималайская кошка
Девон рекс
Домашняя
Донской сфинкс
Египетская мау
Калифорнийская сияющая
Канаани
Карельский бобтейл длинношёрстный
Карельский бобтейл короткошёрстный
Кельтская
Европейская короткошёрстная
Кимрик
Колорпойнт
Корат
Корниш рекс
Курильский бобтейл длинношёрстный
Курильский бобтейл короткошёрстный
Лаперм длинношёрстный
Лаперм короткошёрстный
Манчкин длинношёрстная
Манчкин короткошёрстная
Мейн-кун
Меконгский бобтейл
Минскин
Мэнкс
Мэнская кошка
Наполеон
Невская маскарадная
Немецкий рекс
Нибелунг
Норвежская лесная
Орегон-рекс
Ориентальная длинношёрстная
Ориентальная короткошёрстная
Охос азулес
Охос азулес длинношёрстный
Оцикет
Персидская
Колорпойнт
Петерболд
Пиксибоб длинношёрстный
Пиксибоб короткошёрстный
Рагамаффин
Русская голубая
Рэгдолл
Саванна
Священная бирманская
Сейшельская длинношёрстная
Сейшельская короткошёрстная
Селкирк рекс длинношёрстный
Селкирк рекс короткошёрстный
Серенгети
Сиамская
Сибирская
Сингапурская
Скоттиш страйт
Скоттиш фолд
Сноу-Шу
Сококе
Сомали
Сфинкс
Канадский
Тайская
Тойгер
Тонкинская
Турецкая ангора
Турецкий ван
Украинский левкой
Уральский рекс длинношёрстный
Уральский рекс короткошёрстный
Форин Вайт
Хайленд фолд
Цейлонская
Чаузи
Шантильи Тиффаны
Шартрез
Эгейская
Экзотическая
Экспериментальная порода
Яванез
Яванская
Японский бобтейл длинношёрстный
Японский бобтейл короткошёрстный""".split("\n")