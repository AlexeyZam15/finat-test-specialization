import datetime


class Data:
    def __init__(self, data: list):
        self.creation_date = datetime.datetime.today()
        self.__data = data

    def __str__(self):
        return " ".join([str(i) for i in self.__data])

    def append(self, item):
        self.__data.append(item)

    def __iter__(self):
        for i in self.__data:
            yield i

    def __getitem__(self, index: int):
        return self.__data[index]

    def __len__(self):
        return len(self.__data)
