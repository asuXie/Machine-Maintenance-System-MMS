import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi

from databaseAcces import dbExecute

#from main import widget


 
class AddPartViewmodel(QDialog):
    def __init__(self, manager):
        super(AddPartViewmodel, self).__init__()
        loadUi('AddPartsWindow.ui', self)
        self.dialogAddPartButton.clicked.connect(self.addPart)
        self.exitButton.clicked.connect(self.exitWindow)
        self.manager = manager

        
        self.show()
        
    def addPart(self):
        command = f"INSERT INTO parts (name, price, stock) VALUES ('{self.dialogPartNameField.text()}', {float(self.dialogPartPriceField.text())}, {int(self.dialogPartStockField.value())})"
        dbExecute(command)
        self.manager.extractData()
        self.manager.loadTab()
        self.close()

       

        
    
    def exitWindow(self):
        
        self.close()