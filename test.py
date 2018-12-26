import pyrebase
import firebase_admin
from firebase import firebase
from firebase_admin import credentials
from firebase_admin import db


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Ezra', 'Jesalva', 50000)
emp_2 = Employee('Corey','Shaefer', 65000)
print(emp_2.full_name())
print('{} is loaded through statically'.format(Employee.full_name(emp_1)))
