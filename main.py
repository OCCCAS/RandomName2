from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
import sys
from database_handler import get_all


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.fill_table()

    def fill_table(self):
        data = get_all()
        for i in range(len(data)):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(len(data[i])):
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, j, QTableWidgetItem(str(data[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_ = App()
    app_.show()
    sys.exit(app.exec_())
