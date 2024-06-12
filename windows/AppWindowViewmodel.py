import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTabWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from datetime import datetime
from windows import AddEmployeeViewmodel, AddMachineViewmodel, AddTaskViewmodel, AddPartViewmodel
from databaseAcces import dbExecute, dbExtract
from tabs import Tab


####################
#  INITIALIZATION  #
####################        
        


class AppWindowViewmodel(QMainWindow):
    def __init__(self):
        super(AppWindowViewmodel, self).__init__()
        loadUi('AppWindow.ui', self)
        self.pixmap = QPixmap('LOGO INSIDE.png')
        self.insideLabel.setPixmap(self.pixmap)
        
        #displaying time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        
        
        #tab Managers initialization
        self.employeeTabManager = Tab.Tab(self.employeesTable)
        self.machineTabManager = Tab.Tab(self.machineTable)
        self.plannedTasksTabManager = Tab.Tab(self.plannedTasksTable, "WHERE doneDate > DATE('now')")
        self.currentTasksTabManager = Tab.Tab(self.currentTasksTable, "WHERE doneDate <= DATE('now')")
        self.partsTabManager = Tab.Tab(self.partsTable)
        
        
        
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
        

        

        #button initialization
        self.addEmployeeButton.clicked.connect(self.addEmployeeWindow)
        self.deleteEmployeeButton.clicked.connect(self.employeeTabManager.deleteRecord)
        self.addMachineButton.clicked.connect(self.addMachineWindow)
        self.deleteMachineButton.clicked.connect(self.machineTabManager.deleteRecord)
        self.mainTab.currentChanged.connect(self.tabChanged)
        self.addTaskButton.clicked.connect(self.addTaskWindow)
        self.deleteTaskButton.clicked.connect(self.plannedTasksTabManager.deleteRecord)
        self.taskDoneButton.clicked.connect(self.currentTasksTabManager.deleteRecord)
        self.addPartButton.clicked.connect(self.addPartWindow)
        self.deletePartButton.clicked.connect(self.partsTabManager.deleteRecord)
        
        
        
        
    
    def tabChanged(self, index):
        match index:
            
            case 2:
                self.employeeTabManager.loadTab()
            case 1:
                self.machineTabManager.loadTab()
            case 0:
                self.plannedTasksTabManager.loadTab()
                self.currentTasksTabManager.loadTab()
            case 3:
                self.partsTabManager.loadTab()

    def showTime(self):
        time = datetime.now()
        self.dateTimeLabel.setText(time.strftime("%d/%m/%Y %H:%M:%S"))
    

    ########################
    ###WINDOW   FUNCTIONS###
    ########################

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
  
        
         
        


        
