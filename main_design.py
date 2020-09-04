# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_type.setObjectName("comboBox_type")
        self.gridLayout.addWidget(self.comboBox_type, 1, 3, 1, 1)
        self.comboBox_varienties = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_varienties.setObjectName("comboBox_varienties")
        self.gridLayout.addWidget(self.comboBox_varienties, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 6)
        self.comboBox_size = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_size.setObjectName("comboBox_size")
        self.gridLayout.addWidget(self.comboBox_size, 1, 5, 1, 1)
        self.comboBox_degree = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_degree.setObjectName("comboBox_degree")
        self.gridLayout.addWidget(self.comboBox_degree, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.cost = QtWidgets.QLineEdit(self.centralwidget)
        self.cost.setObjectName("cost")
        self.gridLayout.addWidget(self.cost, 1, 4, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.title = QtWidgets.QLineEdit(self.centralwidget)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 6)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кофемашина (:"))
        self.pushButton.setText(_translate("MainWindow", "Искать"))
        self.label_6.setText(_translate("MainWindow", "Объем упаковки:"))
        self.label_3.setText(_translate("MainWindow", "Степень обжарки:"))
        self.label_2.setText(_translate("MainWindow", "Сорт:"))
        self.label.setText(_translate("MainWindow", "Название:"))
        self.label_5.setText(_translate("MainWindow", "Цена:"))
        self.label_4.setText(_translate("MainWindow", "Тип:"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить запись"))
