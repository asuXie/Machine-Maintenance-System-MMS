import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from datetime import datetime


        
        


class AppWindowViewmodel(QMainWindow):
    def __init__(self):
        super(AppWindowViewmodel, self).__init__()
        loadUi('AppWindow.ui', self)
        
        #displaying time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.showTime()

        #displaying table
        self.machineTable.setColumnWidth(0, 200)
        self.machineTable.setColumnWidth(1, 200)
        self.machineTable.setColumnWidth(2, 200)
        self.machineTable.setColumnWidth(3, 200)
        self.machineTable.setColumnWidth(4, 200)
        self.machineTable.setColumnWidth(5, 200)
        self.machineTable.setColumnWidth(6, 200)

    def showTime(self):
        time = datetime.now()
        self.dateTimeLabel.setText(time.strftime("%d/%m/%Y %H:%M:%S"))

  
        
         
        


        
