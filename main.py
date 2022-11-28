import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import *

# 56ad3dd
class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(660, 100)

        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        self.coffee = cur.execute("""SELECT * FROM coffee_base""").fetchall()

        self.butt1.clicked.connect(self.createTable)
        

    def createTable(self):
        self.setFixedSize(660, 440)

        self.table1.setColumnCount(len(self.coffee))
        self.table1.setHorizontalHeaderLabels(["ID", "Name", "Roasting", "Beans/Ground", "Taste", "Price", "Size"])
        self.table1.setRowCount(0)
        for i, row in enumerate(self.coffee):
            self.table1.setRowCount(
                self.table1.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table1.setItem(
                    i, j, QTableWidgetItem(elem))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())