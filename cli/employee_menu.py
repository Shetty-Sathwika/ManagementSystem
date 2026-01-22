from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB

#object for employee repo
emp_db = EmployeeDB()
#object for authentication
employee_auth = EmployeeAuthentication(emp_db)

#signup function
def employeeSignup():
    print('Employee Signup')
    name = input('enter your name: ')
    email = input('enter your email: ')
    password = input('enter your password: ')
    employee_auth.createEmployee(name,email,password)

def employeeLogin():
    print('Employee Login')
    