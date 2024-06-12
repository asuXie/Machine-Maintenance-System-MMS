import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTabWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from datetime import datetime
from databaseAcces import dbExecute, dbExtract, dbGetID
from tabs import Tab
from windows import AddEmployeeViewmodel
import dbEnum


class Tab():
    
    def __init__(self, table = None, arguments = ""):
        
        self.table = table
        self.arguments = arguments
        self.content = None
        self.selectedRow = None
        self.selectedColumn = None
        self.dbName = str(dbEnum.dbEnum[self.table.objectName()].value)
        #self.table.cellClicked.connect(self.cellWasClicked)
        self.table.cellChanged.connect(self.editRecord)
        
        self.loadTab()



    def loadTab(self):
        
        self.content = dbExtract(f"{self.dbName}", "*", f"{self.arguments}")
        if self.content != None:
            self.table.setRowCount(len(self.content))
            for i in range(len(self.content)):
                for j in range(0, len(self.content[i])):
                    self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.content[i][j])))
                    
            self.table.resizeColumnsToContents()

    def deleteRecord(self):
        
        
        id = self.table.item(self.table.currentRow(), 0).text()
        getID = dbGetID(self.dbName)
        if self.dbName != "parts":
            command = f"DELETE FROM {self.dbName} WHERE {getID[0][1]} = {id}"
        else:
            command = f"DELETE FROM {self.dbName} WHERE {getID[0][1]} = '{id}'"
        
        dbExecute(command)
        self.loadTab()

    def editRecord(self):
        row = self.table.currentRow()
        column = self.table.currentColumn()
        getID = dbGetID(self.dbName)
        #update selected row
        

        command = f"UPDATE {self.dbName} SET {getID[column][1]} = '{self.table.item(row, column).text()}' WHERE {getID[0][1]} = '{self.table.item(row, 0).text()}'"
        dbExecute(command)
        self.loadTab()
        

    def unselectCell(self):
        print("unselect")
        self.selectedRow = None
        self.selectedColumn = None
        
        
    
        
    
