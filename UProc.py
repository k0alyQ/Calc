from UFrac import TFrac

from enum import Enum

from typing import TypeVar, Generic
# Тип T для обобщенного класса
T = TypeVar('T')

# Тип операции
class TOprtn(Enum):
    NoneOp = 0
    Add = 1
    Sub = 2
    Mul = 3
    Dvd = 4

# Тип функции
class TFunc(Enum):
    Rev = 1
    Sqr = 2

class TProc(Generic[T]):
    def __init__(self, default_value: T = TFrac("0\\1")):
        # Инициализация полей
        self.Lop_Res = default_value  # Левый операнд и результат
        self.Rop = default_value  # Правый операнд
        self.Operation = TOprtn.NoneOp  # Изначально операция не установлена

    def ReSet(self):
        # Сброс процессора
        self.Lop_Res = TFrac("0\\1")
        self.Rop = TFrac("0\\1")
        self.Operation = TOprtn.NoneOp

    def OprtnClear(self):
        # Сброс операции
        self.Operation = TOprtn.NoneOp

    def OprtnRun(self):
        # Выполнить операцию
        if self.Operation == TOprtn.Add:
            self.Lop_Res = self.Lop_Res.add(self.Rop)
        elif self.Operation == TOprtn.Sub:
            self.Lop_Res = self.Lop_Res.subtract(self.Rop)
        elif self.Operation == TOprtn.Mul:
            self.Lop_Res = self.Lop_Res.multiply(self.Rop)
        elif self.Operation == TOprtn.Dvd:
            self.Lop_Res = self.Lop_Res.divide(self.Rop)
        # Если операция не установлена, ничего не делаем
        elif self.Operation == TOprtn.NoneOp:
            pass

    def FuncRun(self, func: TFunc):
        # Выполнить функцию
        if func == TFunc.Rev:
            self.Rop = self.Rop.reciprocal()
        elif func == TFunc.Sqr:
            self.Rop = self.Rop.square()

    def Write_Lop_Res(self, operand: T):
        # Записать левый операнд
        self.Lop_Res = operand

    def Write_Rop(self, operand: T):
        # Записать правый операнд
        self.Rop = operand

    def Read_Lop_Res(self) -> T:
        # Чтение левого операнда
        return self.Lop_Res

    def Read_Rop(self) -> T:
        # Чтение правого операнда
        return self.Rop

    def Read_State(self) -> TOprtn:
        # Чтение состояния процессора
        return self.Operation

    def WriteState(self, operation: TOprtn):
        # Записать состояние процессора
        self.Operation = operation

    def __str__(self):
        return f"Левый операнд: {self.Lop_Res}, Правый операнд: {self.Rop}, Операция: {self.Operation}"

'''
# Пример использования
# Инициализация процессора с дробями
processor = TProc(TFrac("0\\1"))
#processor = TProc()

# Установка значений операндов
processor.Write_Lop_Res(TFrac("1\\2"))
processor.Write_Rop(TFrac("1\\3"))

# Установка операции
processor.WriteState(TOprtn.Add)

# Выполнение операции
processor.OprtnRun()
print(processor)  # Левый операнд: 5\6, Правый операнд: 1\3, Операция: TOprtn.Add

# Выполнение функции (обратная дробь для правого операнда)
processor.FuncRun(TFunc.Rev) # Левый операнд: 5\6, Правый операнд: 3\1, Операция: TOprtn.Add
print(processor)

print(processor.Read_Rop())

# Сброс состояния процессора
processor.ReSet()
print(processor) # Левый операнд: 0\1, Правый операнд: 0\1, Операция: TOprtn.NoneOp
'''