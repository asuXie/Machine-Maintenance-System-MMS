#create enum comparing tables to tables in database

from enum import Enum

class dbEnum(Enum):
    employeesTable = "employees"
    machineTable = "machines"
    