import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTabWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from datetime import datetime
from databaseAcces import dbExecute, dbExtract
from tabs import Tab
from windows import AddEmployeeViewmodel
import dbEnum


class EmployeeTab():
    
    def __init__(self, table):
        

        self.employeesTable = table
        self.name = self.employeesTable.objectName()
        #TODO LOADING BY KEY
        print(dbEnum.dbEnum[self.name].value)
        self.loadEmployees()


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
    
        
    


