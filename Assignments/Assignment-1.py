employee_data = {101:
                    {'name': 'Satya',
                     'age': 27, 
                     'department': 'HR', 
                     'salary': 50000}}


def AddEmployee():
    print("Add employee")
def ViewEmployee():
    print("View employee")
def SearchEmployee():
    print("Search employee")

while True:
    print("MENU")
    menu = input("""Enter the task you want to perform (Add Employee, 
View All Employees,
Search for Employee, 
Exit
): """)
    if menu.lower() == "add employee":
        AddEmployee()
        break
    elif menu.lower() == "view all employees":
        ViewEmployee()
        break
    elif menu.lower() == "search for employee":
        SearchEmployee()
        break
    elif menu.lower() == "exit":
        print("Exiting")
        break
    else:
        print(" Enter Invalid input") 
    