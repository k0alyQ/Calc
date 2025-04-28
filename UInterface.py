from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QSpinBox, QGridLayout, QLabel, QMessageBox, QTableWidgetItem, QTableWidget, QCommandLinkButton)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QValidator

from UControl import TCtrl

# 👇 ВАЛИДАТОР — запрещает буквы
class DigitBackslashValidator(QValidator):
    def validate(self, input_text, pos):
        if all(char.isdigit() or char == '\\' or char == '+' or char == '-' or char == '*' or char == '/' for char in input_text):
            return QValidator.State.Acceptable, input_text, pos
        else:
            return QValidator.State.Invalid, input_text, pos

class ClcPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.control = TCtrl()

    def initUI(self):
        self.setWindowTitle("Калькулятор простых дробей")
        main_layout = QVBoxLayout()

        top_buttons_layout = QHBoxLayout()

        help_button = QCommandLinkButton("Справка")
        help_button.clicked.connect(self.HelpInfo)

        history_button = QCommandLinkButton("История")
        history_button.clicked.connect(self.HistoryShow)

        top_buttons_layout.addWidget(history_button)
        top_buttons_layout.addWidget(help_button)

        main_layout.addLayout(top_buttons_layout)
        ################################################
        self.input_field = QLineEdit("0/1")
        self.input_field.setAlignment(Qt.AlignmentFlag.AlignRight) # Выравнивание текста по правому краю
        validator = DigitBackslashValidator()
        self.input_field.setValidator(validator)
        main_layout.addWidget(self.input_field)

        #base_layout = QHBoxLayout()
        ################################################
        grid_layout = QGridLayout()

        self.BS_button = QPushButton('BS')
        self.BS_button.clicked.connect(self.BackSpace)
        grid_layout.addWidget(self.BS_button, 0, 1)

        self.CE_button = QPushButton('CE')
        self.CE_button.clicked.connect(self.Clear)
        grid_layout.addWidget(self.CE_button, 0, 2)

        self.C_button = QPushButton('C')
        self.C_button.clicked.connect(self.ClearEntry)
        grid_layout.addWidget(self.C_button, 0, 3)

        ################################################
        self.MC_button = QPushButton('MC')
        # self.add_button.clicked.connect(self.Add_record)
        grid_layout.addWidget(self.MC_button, 1, 0)

        self.button7 = QPushButton('7')
        self.button7.clicked.connect(lambda: self.AddDigit(7))
        grid_layout.addWidget(self.button7, 1, 1)

        self.button8 = QPushButton('8')
        self.button8.clicked.connect(lambda: self.AddDigit(8))
        grid_layout.addWidget(self.button8, 1, 2)

        self.button9 = QPushButton('9')
        self.button9.clicked.connect(lambda: self.AddDigit(9))
        grid_layout.addWidget(self.button9, 1, 3)

        self.button_del = QPushButton('/')
        self.button_del.clicked.connect(lambda: self.Operation(4)) # Divide
        grid_layout.addWidget(self.button_del, 1, 4)

        self.button_Sqr = QPushButton('Sqr')
        self.button_Sqr.clicked.connect(lambda: self.Function(1))
        grid_layout.addWidget(self.button_Sqr, 1, 5)

        #################################################
        self.MR_button = QPushButton('MR')
        # self.add_button.clicked.connect(self.Add_record)
        grid_layout.addWidget(self.MR_button, 2, 0)

        self.button4 = QPushButton('4')
        self.button4.clicked.connect(lambda: self.AddDigit(4))
        grid_layout.addWidget(self.button4, 2, 1)

        self.button5 = QPushButton('5')
        self.button5.clicked.connect(lambda: self.AddDigit(5))
        grid_layout.addWidget(self.button5, 2, 2)

        self.button6 = QPushButton('6')
        self.button6.clicked.connect(lambda: self.AddDigit(6))
        grid_layout.addWidget(self.button6, 2, 3)

        self.button_umn = QPushButton('*')
        self.button_umn.clicked.connect(lambda: self.Operation(3)) # Multiply
        grid_layout.addWidget(self.button_umn, 2, 4)

        self.button_1delx = QPushButton('1/x')
        self.button_1delx.clicked.connect(lambda: self.Function(2))
        grid_layout.addWidget(self.button_1delx, 2, 5)

        #################################################
        self.MS_button = QPushButton('MS')
        # self.add_button.clicked.connect(self.Add_record)
        grid_layout.addWidget(self.MS_button, 3, 0)

        self.button1 = QPushButton('1')
        self.button1.clicked.connect(lambda: self.AddDigit(1))
        grid_layout.addWidget(self.button1, 3, 1)

        self.button2 = QPushButton('2')
        self.button2.clicked.connect(lambda: self.AddDigit(2))
        grid_layout.addWidget(self.button2, 3, 2)

        self.button3 = QPushButton('3')
        self.button3.clicked.connect(lambda: self.AddDigit(3))
        grid_layout.addWidget(self.button3, 3, 3)

        self.button_minus = QPushButton('-')
        self.button_minus.clicked.connect(lambda: self.Operation(2))
        grid_layout.addWidget(self.button_minus, 3, 4)

        #################################################
        self.Mplus_button = QPushButton('M+')
        # self.add_button.clicked.connect(self.Add_record)
        grid_layout.addWidget(self.Mplus_button, 4, 0)

        self.button0 = QPushButton('0')
        self.button0.clicked.connect(self.AddZERO)
        grid_layout.addWidget(self.button0, 4, 1)

        self.button_plus_minus = QPushButton('+/-')
        self.button_plus_minus.clicked.connect(self.PlusMinus)
        grid_layout.addWidget(self.button_plus_minus, 4, 2)

        self.button_droby = QPushButton("\\")
        self.button_droby.clicked.connect(self.AddSeparator)
        grid_layout.addWidget(self.button_droby, 4, 3)

        self.button_plus = QPushButton('+')
        self.button_plus.clicked.connect(lambda: self.Operation(1))
        grid_layout.addWidget(self.button_plus, 4, 4)

        self.button_result = QPushButton('=')
        self.button_result.clicked.connect(self.CalculateResult)
        grid_layout.addWidget(self.button_result, 4, 5)

        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)

        ########################################

    def validate_input(self, value):
        # Разрешаем только цифры и символы '\\'
        if not all(c.isdigit() or c == '\\' for c in value):
            return False
        return True

    def BackSpace(self):
        result = self.control.do_command_editor(4)
        self.input_field.setText(result)

    def Clear(self):
        result = self.control.do_command_editor(3)
        self.input_field.setText(result)

    def ClearEntry(self):
        result = self.control.do_command_editor(3)############
        self.input_field.setText(result)

    def PlusMinus(self):
        result = self.control.do_command_editor(0)
        self.input_field.setText(result)

    def AddSeparator(self):
        result = self.control.do_command_editor(5)
        self.input_field.setText(result)

    def AddDigit(self, digit):
        result = self.control.do_command_editor(1, digit)
        self.input_field.setText(result)

    def AddZERO(self, digit):
        result = self.control.do_command_editor(2)
        self.input_field.setText(result)

    def Operation(self, operation_type):
        result = self.control.do_oprtn(operation_type)
        self.input_field.setText(result)

    def Function(self, function_type):
        result = self.control.do_func(function_type)
        self.input_field.setText(result)

    def CalculateResult(self):
        #self.control.processor.Write_Rop(TFrac(self.input_field.text()))
        #self.control.processor.OprtnRun()
        #result = self.control.processor.Read_Lop_Res()
        #self.input_field.setText(str(result))

        #self.control.write_calculator_state(TCtrlState.cExpDone)
        result = self.control.calculate()
        self.input_field.setText(result)

    def HelpInfo(self):
        msg = QMessageBox()
        msg.setWindowTitle("Справка")
        msg.setText("Конвертер - это приложение для перевода чисел между системами счисления от 2 до 16.\n\n"

                    "Для выполнения перевода:\n"

                    "Выберите исходную систему счисления.\n"
                    "Введите число, используя кнопки интерфейса или клавиатуру (с обязательным нажатием Enter в конце при вводе с клавиатуры).\n"
                    "Выберите целевую систему счисления.\n"
                    "Нажмите кнопку “Результат” для получения результата.\n\n"
                    "Дополнительные функции:\n"

                    "\"Очистка\" - Очистка полей ввода и результата.\n"
                    "\"Стереть\" - Удаление последнего символа в поле ввода.\n"
                    "\"Выход\" - Закрытие приложения.\n"
                    "\"История\" - Просмотр истории преобразований за текущую сессию.\n\n\n"
                    "Авторы: Хан К. В., Базарова А. Д., Костыркина Е. С.")
        #msg.setIconPixmap(QIcon("help.png").pixmap(64, 64))
        msg.exec()

    def HistoryShow(self):

        self.history_window = HistoryWindow(self.control.get_history())
        self.history_window.show()

class HistoryWindow(QWidget):
    def __init__(self, history_data):
        super().__init__()
        self.setWindowTitle("История")
        self.resize(625, 400)
        layout = QVBoxLayout(self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["№", "Левый операнд", "Операция", "Правый операнд", "Результат"])
        self.table.setColumnWidth(0, 50)  # "№"
        self.table.setColumnWidth(1, 150)  # "Исходное число"
        self.table.setColumnWidth(2, 150)  # "Исходная система"
        self.table.setColumnWidth(3, 150)  # "Система результата"
        self.table.setColumnWidth(4, 100)  # "Результат"
        self.HistoryLoad(history_data)
        close_button = QPushButton("Закрыть", self)
        close_button.clicked.connect(self.close)
        layout.addWidget(self.table)
        layout.addWidget(close_button)
        self.setLayout(layout)

    def HistoryLoad(self, history_data):
        self.table.setRowCount(len(history_data))
        for i, entry in enumerate(history_data):
            for col, value in enumerate(
                    [i + 1, entry["left_number"], entry["operation"], entry["right_number"], entry["result"]]):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                self.table.setItem(i, col, item)
        self.table.resizeRowsToContents()
'''
    def ChangeText(self):
        self.Convert()

    def ChangeEnter(self):
        text = self.input_field.text().upper()
        self.input_field.setText(text)
        alphabet = '.0123456789ABCDEF'
        for char in text:
            if char not in alphabet[:self.input_base.value() + 1]:
                self.ClearInput()
                QMessageBox.critical(self, "Ошибка", "Введены неверные символы!")
                return
        self.ClearInput()
        for char in text:
            if char == '.':
                self.AddDot()
            else:
                self.AddChar(char)

    def UpdBtns(self):
        base = self.input_base.value()
        for char, btn in self.buttons.items():
            btn.setEnabled(int(char, 16) < base)

    def AddChar(self, char):
        self.input_field.setText(self.control.do_cmnd(char))

    def ClearInput(self):
        self.input_field.setText(self.control.do_cmnd("Ce"))
        self.result_field.setText(self.input_field.text())

    def BackSpace(self):
        self.input_field.setText(self.control.do_cmnd('Bs'))

    def AddDot(self):
        self.control.do_cmnd('.')
        if '.' not in self.input_field.text():
            self.control.ed.addDelim()
            self.input_field.setText(self.control.ed.GetNumber())

    def Convert(self):
        self.control.set_pin(self.input_base.value())
        self.control.set_pout(self.result_base.value())
        self.result_field.setText(self.control.do_cmnd(19))
'''



'''


'''
