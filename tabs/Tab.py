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
    
    def __init__(self, table = None, arguments = "", children = None):
        
        self.table = table
        self.arguments = arguments
        self.content = None
        self.childrenCombo = children 
        if self.childrenCombo != None:
            self.childrenDict = self.childrenComboToDict()
            for i in self.childrenDict:
                print(self.childrenDict[i])

        self.dbName = str(dbEnum.dbEnum[self.table.objectName()].value)
        #self.table.cellClicked.connect(self.cellWasClicked)
        self.table.itemChanged.connect(self.editRecord)
        self.sortASCOrder = None
        self.tableColumns = None
       

        self.content = dbExtract(f"{self.dbName}", "*", f" {self.arguments}")
        
        self.loadTab()



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
            self.loadTab()

    def editRecord(self):
       
        row = self.table.currentRow()
        column = self.table.currentColumn()
        getID = dbGetID(self.dbName)
      
        if self.table.item(row, column)!= None:
            command = f"UPDATE {self.dbName} SET {getID[column][1]} = '{self.table.item(row, column).text()}' WHERE {getID[0][1]} = '{self.table.item(row, 0).text()}'"
            dbExecute(command)

    

    def searchByName(self, name):
        
        self.content = dbExtract(f"{self.dbName}", "*", f" WHERE name LIKE '%{name}%'")
        self.loadTab()

    def sortBy(self, column):
        if self.sortASCOrder != True:
            self.sortASCOrder = True
            self.content = dbExtract(f"{self.dbName}", "*", f" {self.arguments} ORDER BY {column} ASC")
        else:
            self.sortASCOrder = False
            self.content = dbExtract(f"{self.dbName}", "*", f" {self.arguments} ORDER BY {column} DESC")
        self.loadTab()


    def childrenComboToDict(self):
        
        dict = {}
        for i in range(len(self.childrenCombo)):
            dict[self.childrenCombo[i].objectName()] = self.childrenCombo[i]
        return dict
    
    ##Combo boxes set value
    def setComboValues(self):
        #TODO
        pragma = dbGetID(self.dbName)
        for i in range(len(pragma)):
            self.childrenDict[0].addItem(pragma[i][1])

        self.childrenDict[0].addItem("")
        for j in range(len(self.tableColumns)):
            self.childrenDict[0].addItem(str(pragma[j][1]))

        self.childrenDict[1].addItem("")
        self.childrenDict[1].addItem("ASC")
        self.childrenDict[1].addItem("DESC")
        print(self.tableColumns)



        
                    
            

    
            
      
        
   
        
    
        
    
