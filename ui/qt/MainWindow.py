# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 470)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(490, 470))
        MainWindow.setMaximumSize(QtCore.QSize(490, 470))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tablePersons = QtWidgets.QTableView(self.centralwidget)
        self.tablePersons.setGeometry(QtCore.QRect(30, 140, 431, 261))
        self.tablePersons.setObjectName("tablePersons")
        self.textName = QtWidgets.QTextEdit(self.centralwidget)
        self.textName.setGeometry(QtCore.QRect(30, 60, 121, 31))
        self.textName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textName.setTabChangesFocus(True)
        self.textName.setObjectName("textName")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 30, 58, 16))
        self.label_1.setObjectName("label_1")
        self.textEmail = QtWidgets.QTextEdit(self.centralwidget)
        self.textEmail.setGeometry(QtCore.QRect(180, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEmail.setFont(font)
        self.textEmail.setTabChangesFocus(True)
        self.textEmail.setObjectName("textEmail")
        self.textPhone = QtWidgets.QTextEdit(self.centralwidget)
        self.textPhone.setGeometry(QtCore.QRect(330, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textPhone.setFont(font)
        self.textPhone.setTabChangesFocus(True)
        self.textPhone.setObjectName("textPhone")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 30, 58, 16))
        self.label_3.setObjectName("label_3")
        self.buttonSavePerson = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSavePerson.setGeometry(QtCore.QRect(350, 100, 112, 32))
        self.buttonSavePerson.setObjectName("buttonSavePerson")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "Name:"))
        self.textEmail.setPlaceholderText(_translate("MainWindow", "myemail@email.com"))
        self.textPhone.setPlaceholderText(_translate("MainWindow", "1-800-AWESOME"))
        self.label_2.setText(_translate("MainWindow", "Email:"))
        self.label_3.setText(_translate("MainWindow", "Phone:"))
        self.buttonSavePerson.setText(_translate("MainWindow", "Save Person"))
