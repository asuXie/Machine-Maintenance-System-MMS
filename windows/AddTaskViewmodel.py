import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QDate
from datetime import date, datetime

from databaseAcces import dbExecute, dbExtract
#from main import widget


 
class AddTaskViewmodel(QDialog):
    def __init__(self, manager):
        super(AddTaskViewmodel, self).__init__()
        loadUi('AddTaskWindow.ui', self)
        self.exitButton.clicked.connect(self.exitWindow)
        self.manager = manager
        self.setTypeCombo()
        self.setMachinesCombo()
        self.setPartsCombo()
        self.show()

        #minimum date
        self.minumumDate = QDate(date.today())
        self.doneTaskCalendar.setMinimumDate(self.minumumDate)

    


        
    def addTask(self):
        selectedDate = self.doneTaskCalendar.selectedDate()
        dateTuple = selectedDate.getDate()
        dateIso = datetime.isoformat(datetime(dateTuple[0], dateTuple[1], dateTuple[2]))
        dateString = dateIso.split("T")[0]
        command = f"INSERT INTO tasks (type, machineID, partID, date) VALUES ('{self.typeCombo.currentText()}', {self.machineCombo.currentText()}, {self.partsCombo.currentText()}, '{dateString}')"
        dbExecute(command)
        self.manager.loadTab()
        self.close()

    def exitWindow(self):
        
        self.close()

    def setTypeCombo(self):
        self.types = dbExtract("maintenanceType", "*")
        #print(self.types)
        for i in range(len(self.types)):
            self.typeCombo.addItem(self.types[i][0])

    def setMachinesCombo(self):
        self.machines = dbExtract("machine", "*")
        print(self.machines)
        for i in range(len(self.machines)):
            self.machineCombo.addItem(str(self.machines[i][0]))

    def setPartsCombo(self):
        self.parts = dbExtract("parts", "*", "WHERE stock > 0")
        for i in range(len(self.parts)):
            self.partsCombo.addItem(str(self.parts[i][0]))