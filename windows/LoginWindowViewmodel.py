import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from windows import AppWindowViewmodel
#from main import widget


 

class LoginWindowViewmodel(QMainWindow):
    def __init__(self, widget):
        super(LoginWindowViewmodel, self).__init__()
        loadUi('LoginWindow.ui', self)
        self.loginButton.clicked.connect(self.loginFunction)
        self.widget = widget
        

    def loginFunction(self):
        
        self.aWindow = AppWindowViewmodel.AppWindowViewmodel()
        
        self.widget.addWidget(self.aWindow)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)



        
        