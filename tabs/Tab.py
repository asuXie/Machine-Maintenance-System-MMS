import sys
from PyQt5 import QtWidgets, QtCore
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
        self.comboBoxes = ()

        self.dbName = str(dbEnum.dbEnum[self.table.objectName()].value)
        self.table.itemChanged.connect(self.editRecord)
        self.sortASCOrder = None
        self.tableColumns = None
       

        self.content = dbExtract(f"{self.dbName}", "*", f" {self.arguments}")
        
        self.loadTab()

    def extractData(self):
        self.content = dbExtract(f"{self.dbName}", "*", f" {self.arguments}")
        

    def loadTab(self):
        
        
        if self.content != None:
            self.table.setRowCount(len(self.content))
            for i in range(len(self.content)):
                for j in range(0, len(self.content[i])):
                    self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.content[i][j])))
                    
            self.table.resizeColumnsToContents()

    def deleteRecord(self):
        if self.table.currentRow() != None or self.table.currentRow().text() != None:
            id = self.table.item(self.table.currentRow(), 0).text()
            getID = dbGetID(self.dbName)
            if self.dbName != "parts":
                command = f"DELETE FROM {self.dbName} WHERE {getID[0][1]} = {id}"
            else:
                command = f"DELETE FROM {self.dbName} WHERE {getID[0][1]} = '{id}'"
            
            dbExecute(command)
            self.extractData()
            self.loadTab()

    def editRecord(self):
       
        row = self.table.currentRow()
        column = self.table.currentColumn()
        getID = dbGetID(self.dbName)
      
        if self.table.item(row, column)!= None:
            command = f"UPDATE {self.dbName} SET {getID[column][1]} = '{self.table.item(row, column).text()}' WHERE {getID[0][1]} = '{self.table.item(row, 0).text()}'"
            dbExecute(command)
            self.extractData()

    

    def searchByName(self, name):
        
        self.content = dbExtract(f"{self.dbName}", "*", f" WHERE name LIKE '%{name}%'")
        self.loadTab()

    def sortBy(self, column, order):
        if column != None and order != None and column != "" and order != "":
            if order == "Ascending":
                self.sortASCOrder = True
                self.content = dbExtract(f"{self.dbName}", "*", f" {self.arguments} ORDER BY {column} ASC")
                self.loadTab()
            if order == "Descending":
                self.sortASCOrder = False
                self.content = dbExtract(f"{self.dbName}", "*", f" {self.arguments} ORDER BY {column} DESC")
                self.loadTab()
        else:
            self.content = dbExtract(f"{self.dbName}", "*", f" {self.arguments}")
            self.loadTab()

    

        
                    
            

    
            
      
        
   
        
    
        
    
