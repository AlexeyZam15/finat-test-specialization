class FileManager:
    def __init__(self, file_path: str):
        self.__path = file_path

    def create_objects_from_clv(self, create_object_func, name_class_ratio, exception_class):
        with open(self.__path, mode='r', encoding='utf-8') as file:
            data_lines = file.read().splitlines()
            if len(data_lines) > 1:
                for line in data_lines[1:]:
                    try:
                        data = line.split(";")
                        if data[3] != "Не определено":
                            create_object_func(name_class_ratio[data[3]], data[1:3] + data[4:6])
                        else:
                            create_object_func(exception_class, data[1:3] + data[4:6])
                    except Exception as e:
                        raise IOError(f"Ошибка с чтением данных из csv файла {self.__path}")

    def write_data_to_file(self, data, data_cols_names: list[str], data_cols_params: list[str]):
        with open(self.__path, mode='w', encoding="utf-8") as file:
            if data_cols_names:
                data_cols = [f'"{i}"' for i in data_cols_names]
                content = f'{";".join(data_cols)}\n'
            for i in data:
                content += f"{';'.join([str(getattr(i, j)) for j in data_cols_params])}\n"
            file.write(content)
