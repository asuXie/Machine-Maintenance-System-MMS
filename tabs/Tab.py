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


class Tab():
    
    def __init__(self, table):
        
        self.table = table
        self.content = None
        self.dbName = str(dbEnum.dbEnum[self.table.objectName()].value)
        self.loadTab()



    def loadTab(self):
        
        self.content = dbExtract(f"{self.dbName}", "*")
        if self.content != None:
            self.table.setRowCount(len(self.content))
            for i in range(len(self.content)):
                for j in range(0, len(self.content[i])):
                    self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.content[i][j])))
                    
            self.table.resizeColumnsToContents()

    def deleteRecord(self):
        
        id = self.table.item(self.table.currentRow(), 0).text()
        command = f"DELETE FROM employees WHERE workerID = {id}"
        dbExecute(command)
        self.loadTab()
    
        
    
