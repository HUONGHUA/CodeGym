


dept_db = {
      101 : 'HRD',
      102 : 'FINANCE',
      103 : 'ACCOUNTS',
      104 : 'SALES',
      105 : 'ENGINEERING',
      106 : 'SUPPORT'
     }

employee_db = {
    1000: dict(name="Alex", doj='01-10-89', dept=103),
    1001: dict(name="Mary", doj='01-11-88', dept=101),
    1002: dict(name="John", doj='01-10-87', dept=104),
    1003: dict(name="David", doj='01-06-89', dept=105),
    1004: dict(name="Anne", doj='01-01-86', dept=106),
    1005: dict(name="Samson", doj='01-02-89', dept=101)
}


def get_emp_info(emp_id):
    if emp_id in employee_db:
        return employee_db[emp_id]
    else:
        print(emp_id, " doesn't exists ")
        return


def get_dept_info(dept_id):
    if dept_id in dept_db:
        return dept_db[dept_id]
    else:
        print(dept_id, " doesn't exists ")
        return


def display_emp_data(emp_data):
    for key, value in emp_data.items():
        if key == 'dept':
            print(key, " : ", get_dept_info(value))
        else:
            print(key, " : ", value)


emp_id = int(input("Please Enter Emp Id :"))

emp_data = get_emp_info(emp_id)

if emp_data:
    display_emp_data(emp_data)