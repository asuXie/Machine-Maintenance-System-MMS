import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from datetime import datetime
from windows import AddEmployeeViewmodel
from databaseAcces import dbExecute, dbExtract


        
        


class AppWindowViewmodel(QMainWindow):
    def __init__(self):
        super(AppWindowViewmodel, self).__init__()
        loadUi('AppWindow.ui', self)
        
        #displaying time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.showTime()

        #refreshing button variables
        
        self.employeesSize = 0
        

        #displaying table
        self.machineTable.setColumnWidth(0, 200)
        self.machineTable.setColumnWidth(1, 200)
        self.machineTable.setColumnWidth(2, 200)
        self.machineTable.setColumnWidth(3, 200)
        self.machineTable.setColumnWidth(4, 200)
        self.machineTable.setColumnWidth(5, 200)
        self.machineTable.setColumnWidth(6, 200)

        self.employeesTable.setColumnWidth(0, 200)
        self.employeesTable.setColumnWidth(1, 200)
        self.employeesTable.setColumnWidth(2, 200)
        self.employeesTable.setColumnWidth(3, 200)
        self.employeesTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        #button initialization
        self.addEmployeeButton.clicked.connect(self.addEmployeeWindow)
        self.refreshEmployeesButton.clicked.connect(self.loadEmployees)
        self.deleteEmployeeButton.clicked.connect(self.deleteEmployee)
        
    

    
    

    ########################
    ###EMPLOYEE FUNCTIONS###
    ########################

    def loadEmployees(self):
        
        self.workers = dbExtract("employees", "*")
        
        
        self.employeesTable.setRowCount(len(self.workers))
        for i in range(len(self.workers)):
            for j in range(4):
                if j !=3:
                    self.employeesTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.workers[i][j])))
                else:
                    if self.workers[i][j] == 1:
                        self.employeesTable.setItem(i, j, QtWidgets.QTableWidgetItem("Yes"))
                    else:
                        self.employeesTable.setItem(i, j, QtWidgets.QTableWidgetItem("No"))
        self.employeesTable.resizeColumnsToContents()

    def deleteEmployee(self):
        
        id = self.employeesTable.item(self.employeesTable.currentRow(), 0).text()
        command = f"DELETE FROM employees WHERE workerID = {id}"
        dbExecute(command)
        self.loadEmployees()

    def showTime(self):
        time = datetime.now()
        self.dateTimeLabel.setText(time.strftime("%d/%m/%Y %H:%M:%S"))
        


    def addEmployeeWindow(self):
        self.addEmployee = AddEmployeeViewmodel.AddEmployeeViewmodel()
        self.addEmployee.show()
        self.addEmployee.exec_()
        
  
        
         
        


        
