import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from windows import AppWindowViewmodel
from databaseAcces import create_connection, extract_users
#from main import widget


 

class LoginWindowViewmodel(QMainWindow):
    def __init__(self, widget):
        super(LoginWindowViewmodel, self).__init__()
        loadUi('LoginWindow.ui', self)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.wrongPasswordLabel.hide()
        self.loginButton.clicked.connect(self.loginFunction)
        self.exitButton.clicked.connect(sys.exit)
        self.pixmap = QPixmap('LOGO MMS.png')
        self.logoLabel.setPixmap(self.pixmap)
        self.widget = widget

      
        

    def loginFunction(self):

        
        rows = extract_users()
        for row in rows:
            if row[1] == self.loginField.text() and row[3] == self.passwordField.text():
                self.appWindow = AppWindowViewmodel.AppWindowViewmodel()
        
                self.widget.addWidget(self.appWindow)
                self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        else:
            self.wrongPasswordLabel.show()
            

            
            
        



        
        