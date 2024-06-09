import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QDate
from datetime import date, datetime

from databaseAcces import create_connection, extract_users, dbExecute

#from main import widget


 
class AddMachineViewmodel(QDialog):
    def __init__(self, manager):
        super(AddMachineViewmodel, self).__init__()
        loadUi('AddMachineWindow.ui', self)
        #self.dialogAddEmployeeButton.clicked.connect(self.addEmployee)
        self.exitButton.clicked.connect(self.exitWindow)
        self.manager = manager

        #minimum date
        self.minumumDate = QDate(date.today())
        self.calendarMachine.setMinimumDate(self.minumumDate)

        #button initialization
        self.dialogAddMachineButton.clicked.connect(self.addMachine)

        
        self.show()
        
    def addMachine(self):
       selectedDate = self.calendarMachine.selectedDate()
       
       date_tuple = selectedDate.getDate()
       date_string = f"{date_tuple[0]}-{date_tuple[1]:02d}-{date_tuple[2]:02d}"
       date_object = datetime.fromisoformat(date_string)
       print(date_object)
       #print(self.machineModelField.text())
       #print(self.machineOperatorField.text())
       command = f"INSERT INTO machine (model, reqMaintenance, operatorID) VALUES ('{self.machineModelField.text()}', {date_string}, {self.machineOperatorField.text()})"
       print(command)
       dbExecute(command)
       self.manager.loadTab()
       self.close()

    def exitWindow(self):
        
        self.close()