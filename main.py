import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3

con = sqlite3.connect('release/data/coffee.sqlite')
cur = con.cursor()


class Ui_Coffee(object):
    def setupUi(self, Coffee):
        Coffee.setObjectName("Coffee")
        Coffee.resize(653, 532)
        self.tableWidget = QtWidgets.QTableWidget(Coffee)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 631, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.addButton = QtWidgets.QPushButton(Coffee)
        self.addButton.setGeometry(QtCore.QRect(10, 10, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")

        self.retranslateUi(Coffee)
        QtCore.QMetaObject.connectSlotsByName(Coffee)

    def retranslateUi(self, Coffee):
        _translate = QtCore.QCoreApplication.translate
        Coffee.setWindowTitle(_translate("Coffee", "Кофе"))
        self.addButton.setText(_translate("Coffee", "Изменить таблицу"))


class Ui_addEditCoffeeForm(object):
    def setupUi(self, addEditCoffeeForm):
        addEditCoffeeForm.setObjectName("addEditCoffeeForm")
        addEditCoffeeForm.resize(1273, 133)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        addEditCoffeeForm.setFont(font)
        self.lineEdit1 = QtWidgets.QLineEdit(addEditCoffeeForm)
        self.lineEdit1.setGeometry(QtCore.QRect(10, 49, 171, 31))
        self.lineEdit1.setObjectName("lineEdit1")
        self.label1 = QtWidgets.QLabel(addEditCoffeeForm)
        self.label1.setGeometry(QtCore.QRect(16, 10, 161, 31))
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(addEditCoffeeForm)
        self.label2.setGeometry(QtCore.QRect(190, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.lineEdit2 = QtWidgets.QLineEdit(addEditCoffeeForm)
        self.lineEdit2.setGeometry(QtCore.QRect(190, 50, 171, 31))
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit3 = QtWidgets.QLineEdit(addEditCoffeeForm)
        self.lineEdit3.setGeometry(QtCore.QRect(370, 50, 171, 31))
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit4 = QtWidgets.QLineEdit(addEditCoffeeForm)
        self.lineEdit4.setGeometry(QtCore.QRect(550, 50, 171, 31))
        self.lineEdit4.setObjectName("lineEdit4")
        self.lineEdit5 = QtWidgets.QLineEdit(addEditCoffeeForm)
        self.lineEdit5.setGeometry(QtCore.QRect(730, 50, 171, 31))
        self.lineEdit5.setObjectName("lineEdit5")
        self.lineEdit6 = QtWidgets.QLineEdit(addEditCoffeeForm)
        self.lineEdit6.setGeometry(QtCore.QRect(910, 50, 171, 31))
        self.lineEdit6.setObjectName("lineEdit6")
        self.lineEdit7 = QtWidgets.QLineEdit(addEditCoffeeForm)
        self.lineEdit7.setGeometry(QtCore.QRect(1090, 50, 171, 31))
        self.lineEdit7.setObjectName("lineEdit7")
        self.label3 = QtWidgets.QLabel(addEditCoffeeForm)
        self.label3.setGeometry(QtCore.QRect(370, 10, 171, 31))
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(addEditCoffeeForm)
        self.label4.setGeometry(QtCore.QRect(550, 10, 171, 31))
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(addEditCoffeeForm)
        self.label5.setGeometry(QtCore.QRect(730, 10, 171, 31))
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setObjectName("label5")
        self.label6 = QtWidgets.QLabel(addEditCoffeeForm)
        self.label6.setGeometry(QtCore.QRect(910, 10, 171, 31))
        self.label6.setAlignment(QtCore.Qt.AlignCenter)
        self.label6.setObjectName("label6")
        self.label7 = QtWidgets.QLabel(addEditCoffeeForm)
        self.label7.setGeometry(QtCore.QRect(1090, 10, 171, 31))
        self.label7.setAlignment(QtCore.Qt.AlignCenter)
        self.label7.setObjectName("label7")
        self.pushButton = QtWidgets.QPushButton(addEditCoffeeForm)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 1251, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(addEditCoffeeForm)
        QtCore.QMetaObject.connectSlotsByName(addEditCoffeeForm)

    def retranslateUi(self, addEditCoffeeForm):
        _translate = QtCore.QCoreApplication.translate
        addEditCoffeeForm.setWindowTitle(_translate("addEditCoffeeForm", "Добавление/изменение кофе"))
        self.label1.setText(_translate("addEditCoffeeForm", "ID"))
        self.label2.setText(_translate("addEditCoffeeForm", "Название сорта"))
        self.label3.setText(_translate("addEditCoffeeForm", "Степень обжарки"))
        self.label4.setText(_translate("addEditCoffeeForm", "Молотый/в зернах"))
        self.label5.setText(_translate("addEditCoffeeForm", "Описание вкуса"))
        self.label6.setText(_translate("addEditCoffeeForm", "Цена"))
        self.label7.setText(_translate("addEditCoffeeForm", "Объем упаковки"))
        self.pushButton.setText(_translate("addEditCoffeeForm", "Добавить/Изменить"))



class AddEditCoffeeForm(QWidget, Ui_addEditCoffeeForm):
    def __init__(self, arg):
        self.arg = arg
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)

    def add(self):
        print(True)
        id = str(self.lineEdit1.text())
        name = str(self.lineEdit2.text())
        roast = str(self.lineEdit3.text())
        cond = str(self.lineEdit4.text())
        taste = str(self.lineEdit5.text())
        price = int(self.lineEdit6.text())
        size = int(self.lineEdit7.text())
        try:
            if len(cur.execute(f'SELECT * From coffee WHERE id = {int(id)}').fetchall()) == 0:
                cur.execute(f'''INSERT INTO coffee('ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах', 
                'Описание вкуса', 'Цена', 'Объем упаковки') VALUES(?, ?, ?, ?, ?, ?, ?)''',
                            (id, name, roast, cond, taste, price, size))
                con.commit()
            else:
                cur.execute(
                    f'''UPDATE coffee SET 'Название сорта' = '{name}', 'Степень обжарки' = '{roast}', 
                    'Молотый/в зернах' = '{cond}', 'Описание вкуса' = '{taste}',
                'Цена' = {price}, 'Объем упаковки' = {size} WHERE id = {id}''')
                con.commit()
            self.arg.loadTable()
        except Exception as ex:
            print(ex)


class MyWidget(QWidget, Ui_Coffee):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable()
        self.addButton.clicked.connect(self.show_)

    def loadTable(self):
        reader = [['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах', 'Описание вкуса', 'Цена',
                   'Объем упаковки']]
        res = cur.execute(f'''SELECT * From coffee''').fetchall()
        for i in range(len(res)):
            res[i] = list(res[i])
        reader += res
        title = reader[0]
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(reader[1::]):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def show_(self):
        global ex1
        ex1 = AddEditCoffeeForm(self)
        ex1.show()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
