from datetime import datetime, date


class DateCheck:

    @staticmethod
    def is_date(date_value: str):
        if isinstance(date_value, date):
            return date_value.strftime("%d.%m.%Y")
        date_list = date_value.split(".")
        if len(date_value) < 10 or len(date_list) != 3:
            raise ValueError("Дата не соответствует формату dd.mm.yyyy")
        for i in date_list:
            try:
                el = int(i)
            except ValueError:
                raise ValueError("Элемент в дате рождения не является целым числом")
        if 31 < int(date_list[0]):
            raise ValueError("Число дня больше 31")
        elif int(date_list[0]) < 1:
            raise ValueError("Число дня меньше 1")
        if 12 < int(date_list[1]):
            raise ValueError("Число месяца больше 12")
        elif int(date_list[1]) < 1:
            raise ValueError("Число месяца меньше 1")
        if datetime.strptime(date_value, '%d.%m.%Y').date() > date.today():
            raise ValueError("Дата рождения больше даты сегодняшнего дня")
        return date_value

    @staticmethod
    def change_date_format(date: str):
        DateCheck.is_date(date)
        number = ""
        date_numbers = []
        for s in date:
            if s == ".":
                date_numbers.append(number)
                number = ""
            number += s
        date_numbers.append(number)
        new_date = f"{date_numbers[2]}-{date_numbers[1]}-{date_numbers[0]}".replace(".", "")
        return new_date
