
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from databaseAcces import dbExecute, dbExtract, dbGetID, importData
from tabs import Tab
import csv
import dbEnum


class Tab():
    
    def __init__(self, table = None, arguments = ""):
        
        self.table = table
        self.arguments = arguments
        self.content = None
        self.comboBoxes = ()

        self.dbName = str(dbEnum.dbEnum[self.table.objectName()].value[0])
        self.table.itemChanged.connect(self.editRecord)
        self.sortASCOrder = None
        self.tableColumns = None
       

        self.content = dbExtract(f"{self.dbName}", "*", f" {self.arguments}")
        
        self.loadTab()
    
    #ekstrakcja danych z bazy

    def extractData(self):
        self.content = dbExtract(f"{self.dbName}", "*", f" {self.arguments}")
        
    #ładowanie danych do tabeli

    def loadTab(self):
        
        
        if self.content != None:
            self.table.setRowCount(len(self.content))
            for i in range(len(self.content)):
                for j in range(0, len(self.content[i])):
                    self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.content[i][j])))
                    
            self.table.resizeColumnsToContents()
    
    #usuwanie rekordu z bazy

    def deleteRecord(self):
       
        if self.table.currentRow() != None and self.table.currentRow() >= 0:
            id = self.table.item(self.table.currentRow(), 0).text()
            getID = dbGetID(self.dbName)
            if self.dbName != "parts":
                command = f"DELETE FROM {self.dbName} WHERE {getID[0][1]} = {id}"
            else:
                command = f"DELETE FROM {self.dbName} WHERE {getID[0][1]} = '{id}'"
            
            dbExecute(command)
            self.extractData()
            self.loadTab()
    
    #edycja rekordu w bazie

    def editRecord(self):
       
        row = self.table.currentRow()
        column = self.table.currentColumn()
        getID = dbGetID(self.dbName)
      
        if self.table.item(row, column)!= None:
            command = f"UPDATE {self.dbName} SET {getID[column][1]} = '{self.table.item(row, column).text()}' WHERE {getID[0][1]} = '{self.table.item(row, 0).text()}'"
            dbExecute(command)
            self.extractData()

    
    #szukanie rekordu po nazwie

    def searchByName(self, name, column):
        
        self.content = dbExtract(f"{self.dbName}", "*", f" WHERE {column} LIKE '%{name}%'")
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

    #import danych z pliku csv

    def browseFiles(self):
        self.file = QFileDialog.getOpenFileName(None, 'Open File', 'C:\\', 'CSV Files (*.csv)')
        if self.file[0] != "":
            file = open(self.file[0], 'r')    
            content = csv.reader(file)
            #print(",".join(["?"]*4))
            importData(self.dbName, dbEnum.dbEnum[self.table.objectName()].value[1], content)
            self.extractData()
            self.loadTab()


        
        

    

        
                    
            

    
            
      
        
   
        
    
        
    
