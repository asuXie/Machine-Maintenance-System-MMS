import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTabWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from datetime import datetime
from windows import AddEmployeeViewmodel, AddMachineViewmodel, AddTaskViewmodel
from databaseAcces import dbExecute, dbExtract
from tabs import Tab, MaintenanceTab


####################
#  INITIALIZATION  #
####################        
        


class AppWindowViewmodel(QMainWindow):
    def __init__(self):
        super(AppWindowViewmodel, self).__init__()
        loadUi('AppWindow.ui', self)
        
        #displaying time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        
        
        #tab Managers initialization
        self.employeeTabManager = Tab.Tab(self.employeesTable)
        self.machineTabManager = Tab.Tab(self.machineTable)
        self.plannedTasksTabManager = MaintenanceTab.MaintenanceTab(self.plannedTasksTable)
        
        
        
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
        self.deleteEmployeeButton.clicked.connect(self.employeeTabManager.deleteRecord)
        self.addMachineButton.clicked.connect(self.addMachineWindow)
        self.deleteMachineButton.clicked.connect(self.machineTabManager.deleteRecord)
        self.mainTab.currentChanged.connect(self.tabChanged)
        self.addTaskButton.clicked.connect(self.addTaskWindow)
        
        
        
    
    def tabChanged(self, index):
            print(index)
            if index == 2:
                self.employeeTabManager.loadTab()
            elif index == 1:
                self.machineTabManager.loadTab()
            elif index == 0:
                self.plannedTasksTabManager.loadTab()

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
        self.addTask = AddTaskViewmodel.AddTaskViewmodel(self.plannedTasksTabManager)
        self.addTask.show()
        self.addTask.exec_()
        
  
        
         
        


        
