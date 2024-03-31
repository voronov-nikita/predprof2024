import sys
import pyqtgraph as pg

from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QTableWidgetItem, QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QTableWidget
from PyQt5.QtGui import QPixmap, QIcon

import datetime


class MyWidget(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)  # Загружаем дизайн
        self.historybutton.clicked.connect(self.open_second_form)


if __name__ == '__main__':
    # создаем инициализацию приложения
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())