import sys
from typing import override
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTabWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from datetime import datetime
from databaseAcces import dbExecute, dbExtract, dbGetID
from tabs import Tab
from windows import AddEmployeeViewmodel
import dbEnum


class CurrentTasksTab():
    
    def __init__(self, table):
            
            self.table = table
            self.content = None
            self.dbName = str(dbEnum.dbEnum[self.table.objectName()].value)
            self.loadTab()

    @override
    def loadTab(self):
        
        self.content = dbExtract(f"{self.dbName}", "*", "WHERE doneDate <= DATE('now')")
        if self.content != None:
            self.table.setRowCount(len(self.content))
            for i in range(len(self.content)):
                for j in range(0, len(self.content[i])):
                    self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.content[i][j])))
                    
            self.table.resizeColumnsToContents()

    def deleteRecord(self):
        
        
        id = self.table.item(self.table.currentRow(), 0).text()
        getID = dbGetID(self.dbName)
        command = f"DELETE FROM {self.dbName} WHERE {getID[0][1]} = {id}"
        
        dbExecute(command)
        self.loadTab()
    