import random
import sys

from PyQt5 import uic, QtGui, QtCore  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame
from PyQt5.QtCore import QTimer


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тренажёр слепой печати")
        uic.loadUi('trenajer.ui', self)
        self.setup_ui()

    def setup_ui(self):
        self.trigger_stage_1()
        self.registration_button.clicked.connect(self.trigger_stage_2)
        self.sign_in_button.clicked.connect(self.trigger_stage_2)
        self.start_button.clicked.connect(self.start)
        self.start_button.setStyleSheet(
            "background-color: #9966CC")
        self.exit_button.clicked.connect(self.exit)
        self.exit_button.setStyleSheet(
            "background-color: #9966CC")
        self.instruction_button.clicked.connect(self.instr)
        self.instruction_button.setStyleSheet(
            "background-color: #9966CC")
        self.back.setStyleSheet(
            "background-color: #9966CC")
        self.back.setFont(QtGui.QFont("Times", 15))
        self.restart.setFont(QtGui.QFont("Times", 15))
        self.restart.clicked.connect(self.rest)
        self.restart.setStyleSheet(
            "background-color: #9966CC")
        pal = self.statistic.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
        self.statistic.setPalette(pal)
        self.statistic.setFont(QtGui.QFont("Times", 13))

        self.privet.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.error.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

        self.sec = 0
        self.timer = QTimer(self)
        self.set_time()
        self.timer.timeout.connect(self.counter)
        self.back.clicked.connect(self.menu)

        self.vyvod.hide()
        self.result.hide()
        self.time.hide()
        self.back.hide()
        self.statistic.hide()
        self.restart.hide()

    def trigger_stage_1(self):
        self.stage_1.setVisible(True)
        self.stage_2.setVisible(False)

    def trigger_stage_2(self):
        self.name = self.name_registration.text()
        self.password = self.password_registration.text()
        if '' == self.name:
            self.error.setText('Введите имя пользователя, пожалуйста')
            self.trigger_stage_1()

        elif '' == self.password:
            self.error.setText('Придумайте пароль, пожалуйста')
            self.trigger_stage_1()
        else:
            self.stage_2.setVisible(True)
            self.stage_1.setVisible(False)
            self.privet.setText('Добро пожаловать, \n {}'.format(self.name))

    def menu(self):
        self.privet.show()
        self.privet.setText('Добро пожаловать, \n {}'.format(self.name))
        self.statistic.hide()
        self.vyvod.hide()
        self.result.hide()
        self.time.hide()
        self.back.hide()
        self.restart.hide()
        self.start_button.show()
        self.exit_button.show()
        self.instruction_button.show()

    def set_time(self):
        hour = self.sec / 3600
        minut = (self.sec % 3600) / 60
        sec = (self.sec % 3600) % 60
        self.time.setText('%02d:%02d:%02d' % (hour, minut, sec))

    def counter(self):
        self.sec += 1
        self.set_time()

    def start(self):
        self.privet.hide()
        self.sch = 0
        self.alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        self.alphabet = list(self.alphabet)
        self.start_button.hide()
        self.exit_button.hide()
        self.instruction_button.hide()
        self.time.show()
        self.vyvod.show()
        self.result.show()
        self.timer.start(1000)
        if self.sec < 60:
            self.letter = random.choice(self.alphabet)
            pal = self.vyvod.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
            self.vyvod.setPalette(pal)
            self.vyvod.setText(self.letter)
        else:
            self.timer.stop()
        self.result.hide()
        self.time.hide()
        self.vyvod.hide()
        self.back.show()
        self.restart.show()
        self.statistic.show()
        self.statistic.setText(f'Ваш результат: {self.sch} символов в минуту')

    def keyPressEvent(self, event):
        self.result.setText(str(event.text()))

    def exit(self):
        self.close()

    def rest(self):
        self.restart.hide()
        self.start()

    def instr(self):
        self.privet.hide()
        self.start_button.hide()
        self.exit_button.hide()
        self.instruction_button.hide()
        self.back.show()
        self.statistic.show()
        self.statistic.setText('Для начала нажмите кнопку "START". '
                               'После вводите букву, которые увидите на экране '
                               'в окошке. На все задание у вас будет 1 минута. '
                               'Чем чаще вы будете тренироваться, тем лучше будет становиться ваш '
                               'результат.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
