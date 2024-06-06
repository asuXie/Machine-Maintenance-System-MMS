import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from windows import AppWindowViewmodel
#from main import widget


 

class LoginWindowViewmodel(QMainWindow):
    def __init__(self, widget, cursor):
        super(LoginWindowViewmodel, self).__init__()
        loadUi('LoginWindow.ui', self)
        self.loginButton.clicked.connect(self.loginFunction)
        self.widget = widget
        self.cursor = cursor
        

    def loginFunction(self):

        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        for row in rows:
            if row[1] == self.loginField.text() and row[3] == self.passwordField.text():
                self.appWindow = AppWindowViewmodel.AppWindowViewmodel(self.cursor)
        
                self.widget.addWidget(self.appWindow)
                self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

            
            
        



        
        