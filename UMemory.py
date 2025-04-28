from UFrac import TFrac

from typing import TypeVar, Generic
# Создаем параметризованный тип T
T = TypeVar('T')

class TMemory(Generic[T]):  # Параметризация типа T
    # Константы для состояния памяти
    _On = "Включена"
    _Off = "Выключена"

    def __init__(self, initial_value: T = None):  ###T = TFrac("0\\1")
        # Инициализация памяти
        if initial_value is None:
            self.FNumber = T(0, 1)
        else:
            self.FNumber = initial_value #################T(initial_value)
        self.FState = TMemory._Off

    def store(self, value: T):
        # Записать число в память
        self.FNumber = value
        self.FState = TMemory._On

    def get(self) -> T:
        # Взять число из памяти
        if self.FNumber is not None:
            self.FState = TMemory._On
            #return self.FNumber
            return self.FNumber
        return 1

    def add(self, value: T):
        # Добавить число к текущему в памяти
        if isinstance(value, TFrac):
            self.FNumber = self.FNumber.add(value)
            self.FState = TMemory._On

    def clear(self):
        # Очистить память
        #self.FNumber = None
        self.FNumber = TFrac("0\\1")
        self.FState = TMemory._Off

    def read_memory_state(self):
        # Читать состояние памяти
        return self.FState

    #def read_number(self) -> T:
        # Читать число в памяти
        #return self.FNumber

    def __str__(self):
        return f"Состояние памяти: {self.FState}, Число: {self.FNumber}"

'''
# Пример использования с TFrac:
#memory_frac = TMemory(TFrac("0\\1"))
memory_frac = TMemory("0\\1")
print(memory_frac)

memory_frac.store(TFrac("2\\3"))
print(memory_frac)  # Состояние памяти: Включена, Число: 2\3

memory_frac.add(TFrac("1\\3"))
print(memory_frac)  # Состояние памяти: Включена, Число: 1\1

print(memory_frac.get())
print(memory_frac.read_memory_state())
print(memory_frac.read_number())

memory_frac.clear()
print(memory_frac)  # Состояние памяти: Выключена, Число: 0\1
'''