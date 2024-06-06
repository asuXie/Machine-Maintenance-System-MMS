import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from windows import AppWindowViewmodel, LoginWindowViewmodel
import sqlite3
from sqlite3 import Error


#create database access
conn = None

    
try:
    conn = sqlite3.connect('base.db')
    print(sqlite3.version)
except Error as e:
    print(e)

cur = conn.cursor()
cur.execute("SELECT * FROM users")

rows = cur.fetchall()
for row in rows:
    print(row)




        




app = QApplication(sys.argv)


widget = QtWidgets.QStackedWidget()

window = LoginWindowViewmodel.LoginWindowViewmodel(widget, cur)


widget.addWidget(window)
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()

app.exec_()
