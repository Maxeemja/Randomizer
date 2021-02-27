import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_window import Ui_Window
import random
import time
list_of_members = ["Вово Гала", "Падстрєла", "Грыня Бибизян", "Максимджа лохом не бывает", "Лос Петучиньо", "Бандэрас"]


class App(QMainWindow, Ui_Window):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_Window()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(lambda: self.click_btn())

    def click_btn(self):
        time.sleep(0.1)
        self.ui.label_result.setText(random.choice(list_of_members))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = App()
    mainwin.show()
    sys.exit(app.exec_())
