import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QDate
from datetime import date, datetime

from databaseAcces import dbExecute, dbExtract
#from main import widget


 
class AddTaskViewmodel(QDialog):
    def __init__(self, manager, secondManager):
        super(AddTaskViewmodel, self).__init__()
        loadUi('AddTaskWindow.ui', self)
        self.exitButton.clicked.connect(self.exitWindow)
        self.dialogAddTaskButton.clicked.connect(self.addTask)
        self.manager = manager
        self.secondManager = secondManager
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
        command = f"INSERT INTO tasks (type, machineID, part, description, doneDate) VALUES ('{self.typeCombo.currentText()}', {int(self.machineCombo.currentText())}, '{self.partsCombo.currentText()}', '{self.descriptionField.toPlainText()}', '{dateString}')"
        dbExecute(command)
        self.manager.loadTab()
        self.secondManager.loadTab()
        self.close()

    def exitWindow(self):
        
        self.close()

    def setTypeCombo(self):
        self.types = dbExtract("maintenanceType", "*")
        for i in range(len(self.types)):
            self.typeCombo.addItem(self.types[i][0])

    def setMachinesCombo(self):
        self.machineCombo.addItem("")
        self.machines = dbExtract("machine", "*")
        for i in range(len(self.machines)):
            self.machineCombo.addItem(str(self.machines[i][0]))

    def setPartsCombo(self):
        self.partsCombo.addItem("")
        self.parts = dbExtract("parts", "*", "WHERE stock > 0")
        for i in range(len(self.parts)):
            self.partsCombo.addItem(str(self.parts[i][0]))