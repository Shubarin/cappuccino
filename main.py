import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QWidget
from main_design import Ui_MainWindow
from addEditCoffeeForm_design import Ui_Form

class ViewDB(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ViewDB, self).__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('data/coffee.sqlite')
        self.varieties_set = set()
        self.degrees_set = set()
        self.type_set = set()
        self.size_set = set()
        self.init_search()
        self.load_table('''SELECT * FROM coffee''')
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pushButton.clicked.connect(self.search_items)
        self.pushButton_2.clicked.connect(self.addEditCoffeeForm)

    def addEditCoffeeForm(self):
        self.new_wnd = AddEditCoffeeForm()
        self.new_wnd.show()
        self.new_wnd.pushButton.clicked.connect(self.insert_line)
        cur = self.con.cursor()
        varieties_all = cur.execute('SELECT * FROM varieties').fetchall()
        self.new_wnd.comboBox.addItems(sorted(list(map(lambda x: str(x[1]), varieties_all))))
        degrees_all = cur.execute('SELECT * FROM the_degree_of_roast').fetchall()
        self.new_wnd.comboBox_2.addItems(sorted(list(map(lambda x: str(x[1]), degrees_all))))
        type_ = cur.execute('SELECT * FROM coffee_type').fetchall()
        self.new_wnd.comboBox_3.addItems(sorted(list(map(lambda x: str(x[1]), type_))))

    def insert_line(self):
        que = 'INSERT INTO coffee(title, varienties, the_degrees_of_roast, ' \
              'coffe_types, description, cost, size) VALUES('
        cur = self.con.cursor()
        varieties_all = cur.execute('SELECT * FROM varieties').fetchall()
        varieties_dict = {x[1]: x[0] for x in varieties_all}
        degrees_all = cur.execute('SELECT * FROM the_degree_of_roast').fetchall()
        degrees_dict = {x[1]: x[0] for x in degrees_all}
        type_ = cur.execute('SELECT * FROM coffee_type').fetchall()
        type_dict = {x[1]: x[0] for x in type_}
        title = self.new_wnd.lineEdit.text()
        varienties = varieties_dict[self.new_wnd.comboBox.currentText()]
        degrees = degrees_dict[self.new_wnd.comboBox_2.currentText()]
        coffee_type = type_dict[self.new_wnd.comboBox_3.currentText()]
        description = self.new_wnd.lineEdit_2.text()
        cost = self.new_wnd.lineEdit_3.text()
        size_ = self.new_wnd.lineEdit_4.text()
        que += f'"{str(title)}", {str(varienties)}, {str(degrees)}, ' \
            f'{str(coffee_type)}, "{str(description)}", {str(cost)}, {str(size_)})'
        cur.execute(que)
        self.con.commit()
        self.load_table('''SELECT * FROM coffee''')

    def load_table(self, que):
        cur = self.con.cursor()
        coffee = cur.execute(que).fetchall()
        title = [description[0] for description in cur.description]
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        for i, line in enumerate(coffee):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, item in enumerate(line):
                if j == 2:
                    res = str(cur.execute(f'SELECT title FROM varieties WHERE id = {str(item)}').fetchone()[0])
                elif j == 3:
                    res = str(
                        cur.execute(f'SELECT title FROM the_degree_of_roast WHERE id = {str(item)}').fetchone()[0])
                elif j == 4:
                    res = str(cur.execute(f'SELECT title FROM coffee_type WHERE id = {str(item)}').fetchone()[0])
                else:
                    res = str(item)
                self.tableWidget.setItem(i, j, QTableWidgetItem(res))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def search_items(self):
        title = '%' + self.title.text() + '%'
        cost = '%' + self.cost.text() + '%'
        que = f'''SELECT * FROM coffee WHERE title like "{title}" AND cost like "{cost}" '''
        if self.comboBox_varienties.currentText() != '-':
            que += f' AND varienties={str(self.varieties_dict[self.comboBox_varienties.currentText()])}'
        if self.comboBox_degree.currentText() != '-':
            que += f' AND the_degrees_of_roast={str(self.degrees_dict[self.comboBox_degree.currentText()])}'
        if self.comboBox_type.currentText() != '-':
            que += f' AND coffe_types={str(self.type_dict[self.comboBox_type.currentText()])}'
        if self.comboBox_size.currentText() != '-':
            que += f' AND size={str(self.comboBox_size.currentText())}'
        self.load_table(que)

    def init_search(self):
        cur = self.con.cursor()
        coffees = cur.execute('SELECT * FROM coffee').fetchall()
        self.varieties_set.add('-')
        self.varieties_dict = {}
        self.degrees_set.add('-')
        self.degrees_dict = {}
        self.type_set.add('-')
        self.type_dict = {}
        for line in coffees:
            var = cur.execute(f'SELECT * FROM varieties WHERE id = {line[2]}').fetchone()
            degree = cur.execute(f'SELECT * FROM the_degree_of_roast WHERE id = {line[3]}').fetchone()
            type_ = cur.execute(f'SELECT * FROM coffee_type WHERE id = {line[4]}').fetchone()
            size_ = line[7]
            self.varieties_set.add(var[1])
            self.varieties_dict[var[1]] = var[0]
            self.degrees_set.add(degree[1])
            self.degrees_dict[degree[1]] = degree[0]
            self.type_set.add(type_[1])
            self.type_dict[type_[1]] = type_[0]
            self.size_set.add(size_)
        self.comboBox_varienties.addItems(sorted(self.varieties_set))
        self.comboBox_degree.addItems(sorted(self.degrees_set))
        self.comboBox_type.addItems(sorted(self.type_set))
        self.comboBox_size.addItems(map(str, ['-'] + (sorted(self.size_set))))


class AddEditCoffeeForm(QWidget, Ui_Form):
    def __init__(self):
        super(AddEditCoffeeForm, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ViewDB()
    wnd.show()
    sys.exit(app.exec())
