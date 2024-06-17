import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi

from databaseAcces import dbExecute

#from main import widget


 
class AddEmployeeViewmodel(QDialog):
    def __init__(self, manager):
        super(AddEmployeeViewmodel, self).__init__()
        loadUi('AddEmployeeWindow.ui', self)
        self.dialogAddEmployeeButton.clicked.connect(self.addEmployee)
        self.exitButton.clicked.connect(self.exitWindow)
        self.manager = manager

        
        self.show()
        
    def addEmployee(self):
        command = f"INSERT INTO employees (name, surname, isOperator) VALUES ('{self.addEmployeeNameField.text()}', '{self.addEmployeeSurnameField.text()}', False)"
        dbExecute(command)
        self.manager.extractData()
        self.manager.loadTab()
        self.close()
        return True

    def exitWindow(self):
        
        self.close()