

from enum import Enum

class dbEnum(Enum):
    employeesTable = ("employees","name, surname, isOperator")
    machineTable = ("machine", "model, reqMaintenance, operatorID")
    plannedTasksTable = ("tasks", "type, machineID, description, doneDate, part")
    currentTasksTable = ("tasks", "")
    partsTable = ("parts", "name, price, stock")
    