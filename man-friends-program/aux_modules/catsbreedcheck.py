class CatsBreedCheck:

    def is_cat_breed(self, cat_breed_name: str):
        if cat_breed_name not in self.__cats_breeds:
            raise ValueError("Неверная порода кошки")

    __cats_breeds = """абиссинская
австралийский мист
азиатская
табби
акринская
американская жесткошёрстная
американская короткошёрстная
американский бобтейл длинношёрстный
американский бобтейл короткошёрстный
американский кёрл длинношёрстный
американский кёрл короткошёрстный
анатолийская
аравийский мау
балинезийская
балийская
бенгальская
бомбейская
бразильская короткошёрстная
британская длинношёрстная
британская короткошёрстная
бурма
бурманская
бурмилла длинношёрстный
бурмилла короткошёрстный
гавана
гималайская кошка
девон рекс
домашняя
донской сфинкс
египетская мау
калифорнийская сияющая
канаани
карельский бобтейл длинношёрстный
карельский бобтейл короткошёрстный
кельтская
европейская короткошёрстная
кимрик
колорпойнт
корат
корниш рекс
курильский бобтейл длинношёрстный
курильский бобтейл короткошёрстный
лаперм длинношёрстный
лаперм короткошёрстный
манчкин длинношёрстная
манчкин короткошёрстная
мейн-кун
меконгский бобтейл
минскин
мэнкс
мэнская кошка
наполеон
невская маскарадная
немецкий рекс
нибелунг
норвежская лесная
орегон-рекс
ориентальная длинношёрстная
ориентальная короткошёрстная
охос азулес
охос азулес длинношёрстный
оцикет
персидская
колорпойнт
петерболд
пиксибоб длинношёрстный
пиксибоб короткошёрстный
рагамаффин
русская голубая
рэгдолл
саванна
священная бирманская
сейшельская длинношёрстная
сейшельская короткошёрстная
селкирк рекс длинношёрстный
селкирк рекс короткошёрстный
серенгети
сиамская
сибирская
сингапурская
скоттиш страйт
скоттиш фолд
сноу-шу
сококе
сомали
сфинкс
канадский
тайская
тойгер
тонкинская
турецкая ангора
турецкий ван
украинский левкой
уральский рекс длинношёрстный
уральский рекс короткошёрстный
форин вайт
хайленд фолд
цейлонская
чаузи
шантильи тиффаны
шартрез
эгейская
экзотическая
экспериментальная порода
яванез
яванская
японский бобтейл длинношёрстный
японский бобтейл короткошёрстный""".split("\n")