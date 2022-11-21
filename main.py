import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("coffee.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.modified = {}
        self.titles = None

    def item_changed(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee_settings").fetchall()
        if cur.execute("SELECT * FROM coffee_settings").fetchone() is not None:
            self.table_db.setRowCount(len(result))
            self.table_db.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.table_db.setItem(i, j, QTableWidgetItem(str(val)))
        else:
            self.table_db.setRowCount(0)
            self.table_db.setColumnCount(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
