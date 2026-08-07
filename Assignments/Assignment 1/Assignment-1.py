employee_data = {101:
                    {'name': 'Satya',
                     'age': 27, 
                     'department': 'HR', 
                     'salary': 50000}}
 

def AddEmployee(emp_id, name, age, department, salary):
    if emp_id in employee_data:
        print("Employee ID already exists")
        return

    employee_data[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }
    print("Employee Added Successfully")

def ViewEmployee():
    if not employee_data:
        print("No employees available")
        return

    for emp_id, details in employee_data.items():
        print(f"\nEmployee ID: {emp_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']}")
    
def SearchEmployee(emp_id):
    if emp_id not in employee_data:
        print("Employee ID doesn't exists")
        return
    else:
        print(employee_data[emp_id])

while True:
    print("MENU")
    menu = input("""Enter the task you want to perform:
Add Employee, 
View All Employees,
Search for Employee, 
Exit

): """)
    if menu.lower() == "add employee":
        emp_id = int(input("Enter the employee ID: "))

        if emp_id in employee_data:
            print("Employee ID already exists")
            break

        name = input("Enter the name of the employee: ")
        age = int(input("Enter the age of the employee: "))
        department = input("Enter the department of the employee: ")
        salary = int(input("Enter the salary of the employee: "))

        AddEmployee(emp_id, name, age, department, salary)
        

    elif menu.lower() == "view all employees":
        ViewEmployee()

    elif menu.lower() == "search for employee":
        emp_id =int(input("Enter Employee ID: "))
        SearchEmployee(emp_id)

    elif menu.lower() == "exit":
        print("Exiting")
        break
    
    else:
        print(" Enter Invalid input") 
    