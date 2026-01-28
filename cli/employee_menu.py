from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB
from validation.email_validator import email_vali
from validation.pass_validator import password_vali
from getpass4 import getpass
from utils.pass_hash import password_hasher,check_password

#object for employee repo
emp_db = EmployeeDB()
#object for authentication
employee_auth = EmployeeAuthentication(emp_db)

#signup function
def employeeSignup():
    print('Employee Signup')
    name = input('enter your name: ')
    email = input('enter your email: ')
    verify_email = emp_db.searchEmp(email)
    if verify_email is None:
        if email_vali(email = email) is not None :
            password = getpass('enter your password: ')
            confirm_pw = getpass('enter your password: ')
            if password == confirm_pw:
                if password_vali(password):
                    password = password_hasher(password)
                    employee_auth.createEmployee(name,email,password)
                else:
                    print('''password is not valid
password minimum length should be 5
password should contain an uppercase
password should contain atleast one digit
and a special character''')
                    employeeSignup()
        else:
            print('''Enter valid email!!!''')
            employeeSignup()
    else:
        print('Email already exist goto login ')
        employeeLogin()

#login function
def employeeLogin():
    print('Employee Login')
    email = input('enter your email: ')
    password = getpass('enter password: ')
    hashed_pw = employee_auth.empLogin(email)
    if check_password(password,hashed_pw):
        print('Login Successfull!!')
    else:
        print('Login failed')