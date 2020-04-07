import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import pyqtSlot, QModelIndex
from MainWindow import Ui_MainWindow
from directory import app as directory


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.table = QTableWidget(self.tablePersons)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.doubleClicked.connect(self.set_person_on_click)
        self.populate()
        self.buttonSavePerson.clicked.connect(self.save_on_click)

    def populate(self):
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(["Name", "Email", "Phone"])
        self.table.setFixedWidth(self.tablePersons.width())
        self.table.setFixedHeight(self.tablePersons.height())
        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)


        persons = directory.get_all_persons()

        for person in persons:
            self.table.insertRow(0)
            self.table.setItem(0, 0, QTableWidgetItem(person['name']))
            self.table.setItem(0, 1, QTableWidgetItem(person['email']))
            self.table.setItem(0, 2, QTableWidgetItem(person['phone']))

    @pyqtSlot()
    def save_on_click(self):
        directory.save_person(self.textName.toPlainText(), self.textEmail.toPlainText(), self.textPhone.toPlainText())
        self.populate()

    def set_person_on_click(self, signal):
        _signal = QModelIndex(signal)



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("Directory")

window.show()
app.exec()
