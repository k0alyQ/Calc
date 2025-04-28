from UFrac import TFrac
from UEditor import TEditor
from UProc import TProc, TOprtn, TFunc
from UMemory import TMemory

from enum import Enum


# Определение состояний калькулятора
class TCtrlState(Enum):
    cStart = 0        # Начальное состояние
    cEditing = 1      # Ввод и редактирование
    FunDone = 2       # Функция выполнена
    cValDone = 3      # Значение введено
    cExpDone = 4      # Выражение вычислено
    cOpChange = 5     # Операция изменена
    cError = 6        # Ошибка

class TCtrl:
    # Управление выполнением команд калькулятора
    # Распределяет команды калькулятора между объектами
    # («редактор», «процессор», «память», «буфер обмена»),
    # которые должны эти команды выполнять.

    def __init__(self):
        self.editor = TEditor()  # Объект для редактирования
        self.processor = TProc(TFrac("0\\1"))  # Объект процессора
        self.memory = TMemory(TFrac("0\\1"))  # Объект памяти
        self.state = TCtrlState.cStart  # Начальное состояние калькулятора
        self.number = TFrac("0\\1")  # Число, результат последней операции
        self.full_expression = "0\\1"  # добавляем строку выражения
        self._history = []

    def do_command_calc(self, a: int, b: str, MState: str) -> str:
        """
        Выполняет команду калькулятора
         (управляет операциями с редактором, процессором, памятью)
        a - номер команды пользователя
        b - строка для буфера обмена
        MState - строка состояния памяти
        """

    def do_command_editor(self, a: int, digit=None) -> str:
        # Выполняет команду редактирования в редакторе
        self.editor.edit(a, digit)
        self.full_expression = self.editor.read_str_frac()
        return self.full_expression

    def do_oprtn(self, a: int) -> str:
        # Выполняет операцию с числом
        # Сохраняем текущее число как левый операнд
        left_operand = TFrac(self.editor.read_str_frac())
        self.processor.Write_Lop_Res(left_operand)

        # Устанавливаем тип операции
        self.processor.WriteState(TOprtn(a))
        op_map = {1: " + ", 2: " - ", 3: " * ", 4: " / "}
        self.full_expression += op_map.get(a, " ? ")

        # Ожидаем второй операнд
        # Сброс редактора под ввод правого операнда
        self.editor.clear() ############
        self.state = TCtrlState.cValDone
        return self.full_expression

    def do_func(self, a: int) -> str:
        # Выполняет функцию
        # Установка операнда из редактора
        frac = TFrac(self.editor.read_str_frac())
        self.processor.Write_Rop(frac)
        if a == 1:
            self.processor.FuncRun(TFunc.Sqr)
            func_str = "sqr("
        elif a == 2:
            self.processor.FuncRun(TFunc.Rev)
            func_str = "1/("
        else:
            self.state = TCtrlState.cError
            return "Ошибка: Неверная функция"

        # Чтение результата
        result = self.processor.Read_Rop()
        # Сброс редактора и установка результата
        self.editor.write_str_frac(str(result))
        self.full_expression = f"{func_str}{frac}) = {result}"
        self.state = TCtrlState.FunDone
        return str(result)

    def calculate(self, *args) -> str:

        hist_record = {
            "left_number": self.processor.Lop_Res,
            "operation": self.processor.Operation,
        }
        # Сохраняем правый операнд
        right_operand = TFrac(self.editor.read_str_frac())
        hist_record["right_number"] = right_operand
        self.processor.Write_Rop(right_operand)

        # Выполняем операцию
        self.processor.OprtnRun()

        # Получаем результат
        result = self.processor.Read_Lop_Res()
        hist_record["result"] = result
        self._history.append(hist_record)


        self.editor.write_str_frac(str(result))

        self.full_expression = f"{result}"

        # Обновляем состояние
        self.state = TCtrlState.cExpDone
        return self.full_expression

    def get_history(self):
        return self._history


    def do_mem(self, a: int, MState: str) -> str:
        # Выполнить команду памяти
        return Mstate, result

    def set_initial_calculator_state(self, a: int) -> str:
        # Устанавливает начальное состояние калькулятора
        self.state = TCtrlState.cStart
        self.number = TFrac("0\\1")
        self.editor.clear()
        self.processor.ReSet()
        self.memory.clear()
        self.full_expression = "0\\1"
        return "Начальное состояние установлено"

    def read_calculator_state(self) -> TCtrlState:
        # Читает состояние калькулятора
        return self.state

    def write_calculator_state(self, CState) -> TCtrlState:
        # Записывает состояние калькулятора
        self.state = CState

    def __del__(self):
        # Освобождение памяти
        del self.editor
        del self.processor
        del self.memory
        del self.number
        del self.full_expression

    def __str__(self):
        return f"Состояние калькулятора: {self.state}, Число: {self.number}, Редактор: {self.editor}, Процессор: {self.processor}, Память: {self.memory}"

