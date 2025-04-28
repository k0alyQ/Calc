class TEditor:
    # Ввод, хранение и редактирование строкового
    # представления простых дробей

    # Константы
    SEPARATOR = "\\" # Разделитель числителя и знаменателя
    ZERO = "0\\1" # Строковое представление числа

    def __init__(self):
        self.string = TEditor.ZERO

    #@property
    def frac_is_zero(self):
        # Проверка на 0\1
        return self.string == TEditor.ZERO

    def add_negate(self):
        # Добавление или удаление знака "-"
        if self.string.startswith("-"):
            self.string = self.string[1:] # Удалили -
        else:
            self.string = "-" + self.string # Добавили -
        return self.string

    def add_digit(self, digit):
        # Добавление цифры к строке
        if digit < 0 or digit > 9:
            return 1
        if self.string == TEditor.ZERO:
            self.string = ""  # Убираем 0\1 перед первым вводом
        self.string += str(digit)
        return self.string

    def add_ZERO(self):
        # Добавление нуля к строке
        if self.string.endswith(TEditor.SEPARATOR):  # Запрет 5\0
            return self.string
        if self.string == TEditor.ZERO:
            self.string = ""  # Убираем 0\1 перед первым вводом
        self.string += "0"
        return self.string

    def add_separator(self):
        # Добавление разделителя \ к строке
        if self.string.endswith(TEditor.SEPARATOR): # Запрет 5\\\2
            return self.string  # Не добавляем второй '\'
        self.string += TEditor.SEPARATOR
        return self.string

    def del_last_symb(self):
        # Удаление последнего символа (BS)
        self.string = self.string[:-1]
        return self.string

    def clear(self):
        # Установить строку как '0\1'
        self.string = TEditor.ZERO
        return self.string

    def edit(self, command, digit=None):
        if command == 0:
            return self.add_negate()
        elif command == 1:
            return self.add_digit(digit)
        elif command == 2:
            return self.add_ZERO()
        elif command == 3:
            return self.clear()
        elif command == 4:
            return self.del_last_symb()
        elif command == 5:
            return self.add_separator()
        else:
            return 1

    #@property
    def read_str_frac(self):
        # Чтение строкового представления дроби
        if "/0" in self.string:
            return TEditor.ZERO
        return self.string

    def write_str_frac(self, value):
        # Запись строкового представления дроби
        self.string = value

    def __str__(self):
        return self.string

'''
# Пример использования
x = TEditor()
print(x.read_str_frac()) # 0\1
print(x.write_str_frac("5\\5"))
print(x.read_str_frac()) # 5\5
print(x.frac_is_zero()) # False
print(x.edit(0)) # -5\5
print(x.edit(1, 9)) # -5\59
print(x.edit(2)) # -5\590
print(x.edit(3)) # 0\1
print(x.edit(4)) # 0\
print(x.edit(5)) # 0\\
'''














