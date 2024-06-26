
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from datetime import datetime
from windows import AddEmployeeViewmodel, AddMachineViewmodel, AddTaskViewmodel, AddPartViewmodel
from databaseAcces import dbExecute, dbExtract, dbGetID
from dbEnum import dbEnum
from tabs import Tab
import csv


#klasa okna głównego     
        


class AppWindowViewmodel(QMainWindow):
    def __init__(self):
        super(AppWindowViewmodel, self).__init__()
        loadUi('AppWindow.ui', self)
        self.pixmap = QPixmap('LOGO INSIDE.png')
        self.insideLabel.setPixmap(self.pixmap)
        
        #wyświetlanie czasu
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        
        
        #inicjalizacja managerów zakładek
        self.employeeTabManager = Tab.Tab(self.employeesTable, "")
        self.machineTabManager = Tab.Tab(self.machineTable, "")
        self.plannedTasksTabManager = Tab.Tab(self.plannedTasksTable, "WHERE doneDate > DATE('now')")
        self.currentTasksTabManager = Tab.Tab(self.currentTasksTable, "WHERE doneDate <= DATE('now')")
        self.partsTabManager = Tab.Tab(self.partsTable, "")
        
        
        
        
        

        

        #przypisywanie funkcji do przycisków
        self.addEmployeeButton.clicked.connect(self.addEmployeeWindow)
        self.deleteEmployeeButton.clicked.connect(self.employeeTabManager.deleteRecord)

        self.addMachineButton.clicked.connect(self.addMachineWindow)
        self.deleteMachineButton.clicked.connect(self.machineTabManager.deleteRecord)

        
        self.addTaskButton.clicked.connect(self.addTaskWindow) 
        self.deleteTaskButton.clicked.connect(self.plannedTasksTabManager.deleteRecord)
        self.taskDoneButton.clicked.connect(self.currentTasksTabManager.deleteRecord)
        
        self.addPartButton.clicked.connect(self.addPartWindow)
        self.deletePartButton.clicked.connect(self.partsTabManager.deleteRecord)

        self.mainTab.currentChanged.connect(self.tabChanged)

        self.partsNameSearch.textChanged.connect(self.searchParts)
        self.machinesNameSearch.textChanged.connect(self.searchMachines)
        self.employeeSurnameSearch.textChanged.connect(self.searchEmployees)
        self.plannedTasksNameSearch.textChanged.connect(self.searchPlannedTasks)

        self.browseEmployees.clicked.connect(self.employeeTabManager.browseFiles)
        self.browseMachines.clicked.connect(self.machineTabManager.browseFiles)
        self.browseTasks.clicked.connect(self.plannedTasksTabManager.browseFiles)
        self.browseParts.clicked.connect(self.partsTabManager.browseFiles)
        

        ###################
        #COMBOBOXES       #
        ###################

        #wypełnianie comboboxów i sortowanie

        self.fillComboBoxes((self.sortWhatComboParts, self.sortByComboParts), self.partsTable)
        self.sortByComboParts.currentIndexChanged.connect(self.sortByParts)

        self.fillComboBoxes((self.sortWhatComboMachines, self.sortByComboMachines), self.machineTable)
        self.sortByComboMachines.currentIndexChanged.connect(self.sortByMachines)

        self.fillComboBoxes((self.sortWhatComboEmployees, self.sortByComboEmployees), self.employeesTable)
        self.sortByComboEmployees.currentIndexChanged.connect(self.sortByEmployees)

        self.fillComboBoxes((self.sortWhatComboMaintenance, self.sortByComboMaintenance), self.plannedTasksTable)
        self.sortByComboMaintenance.currentIndexChanged.connect(self.sortByMaintenance)

      

        
        
    
    #zmiana i odświeżanie zakładek    
    
    def tabChanged(self, index):
        match index:
            
            case 2:
                self.employeeTabManager.extractData()
                self.employeeTabManager.loadTab()
            case 1:
                self.machineTabManager.extractData()
                self.machineTabManager.loadTab()
            case 0:
                self.employeeTabManager.extractData()
                self.plannedTasksTabManager.loadTab()
                self.currentTasksTabManager.loadTab()
            case 3:
                self.partsTabManager.extractData()
                self.partsTabManager.loadTab()

    #wyświetlanie czasu
    
    def showTime(self):
        time = datetime.now()
        self.dateTimeLabel.setText(time.strftime("%d/%m/%Y %H:%M:%S"))
    

    ########################
    ###FUNKCJE OKIENKOWE####
    ########################

    #funkcje okienkowe dodwania rekordów

    def addEmployeeWindow(self):
        self.addEmployee = AddEmployeeViewmodel.AddEmployeeViewmodel(self.employeeTabManager)
        self.addEmployee.show()
        self.addEmployee.exec_()

    def addMachineWindow(self):
        self.addMachine = AddMachineViewmodel.AddMachineViewmodel(self.machineTabManager)
        self.addMachine.show()
        self.addMachine.exec_()

    def addTaskWindow(self):
        self.addTask = AddTaskViewmodel.AddTaskViewmodel(self.plannedTasksTabManager, self.currentTasksTabManager)
        self.addTask.show()
        self.addTask.exec_()
        
    def addPartWindow(self):
        self.addPart = AddPartViewmodel.AddPartViewmodel(self.partsTabManager)
        self.addPart.show()
        self.addPart.exec_()
        

    #funkcje wyszukiwania
    
    def searchParts(self):
        self.partsTabManager.searchByName(self.partsNameSearch.text(), 'name')

    def searchMachines(self):
        self.machineTabManager.searchByName(self.machinesNameSearch.text(), 'model')

    def searchEmployees(self):
        self.employeeTabManager.searchByName(self.employeeSurnameSearch.text(), 'surname')

    def searchPlannedTasks(self):
        self.plannedTasksTabManager.searchByName(self.plannedTasksNameSearch.text(), 'machineID')

        
        
    ####################    
    #funkcje sortowania#
    ####################

    #wypełnianie comboboxów

    def fillComboBoxes(self, comboBoxes, table):
        comboBoxes[0].addItem("")
        dbName = str(dbEnum[table.objectName()].value[0])
        pragma = dbGetID(dbName)
        for i in range(len(pragma)):
            comboBoxes[0].addItem(pragma[i][1])
        
        comboBoxes[1].addItem("")
        comboBoxes[1].addItem("Ascending")
        comboBoxes[1].addItem("Descending")

    #sortowanie

    def sortByParts(self):
        comboBoxes = (self.sortWhatComboParts, self.sortByComboParts)
        self.partsTabManager.sortBy(comboBoxes[0].currentText(), comboBoxes[1].currentText())

    def sortByMachines(self):
        comboBoxes = (self.sortWhatComboMachines, self.sortByComboMachines)
        self.machineTabManager.sortBy(comboBoxes[0].currentText(), comboBoxes[1].currentText())

    def sortByEmployees(self):
        comboBoxes = (self.sortWhatComboEmployees, self.sortByComboEmployees)
        self.employeeTabManager.sortBy(comboBoxes[0].currentText(), comboBoxes[1].currentText())
    
    def sortByMaintenance(self):
        comboBoxes = (self.sortWhatComboMaintenance, self.sortByComboMaintenance)
        self.plannedTasksTabManager.sortBy(comboBoxes[0].currentText(), comboBoxes[1].currentText())

    def employeesCSV(self):
        content = self.browseFiles()
        content = csv.reader(content)
        

        
        
         
        


        
