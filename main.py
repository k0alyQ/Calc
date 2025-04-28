import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from UInterface import ClcPanel

def except_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon("phone.jpg"))
    # Создаём виджет
    sys._excepthook = sys.excepthook
    sys.excepthook = except_hook
    window = ClcPanel()
    window.show()
    sys.exit(app.exec())