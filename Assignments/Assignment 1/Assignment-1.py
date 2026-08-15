employee_data = {
    101: {
        'name': 'Satya',
        'age': 27,
        'department': 'HR',
        'salary': 50000
    }
}


def add_employee():
    while True:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employee_data:
            print("Employee ID already exists. Please enter a different ID.\n")
        else:
            break

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    employee_data[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print("Employee added successfully.\n")


def view_employees():
    if not employee_data:
        print("No employees available.\n")
        return

    print(f"{'ID':<10} {'Name':<15} {'Age':<8} {'Department':<15} {'Salary':<10}")
    for emp_id, details in employee_data.items():
        print(f"{emp_id:<10} {details['name']:<15} {details['age']:<8} {details['department']:<15} {details['salary']:<10}")


def search_employee():
    if not employee_data:
        print("No employees available.\n")
        return

    emp_id = int(input("Enter Employee ID to search: "))

    if emp_id in employee_data:
        details = employee_data[emp_id]
        print(f"{'ID':<10} {'Name':<15} {'Age':<8} {'Department':<15} {'Salary':<10}")
        print(f"{emp_id:<10} {details['name']:<15} {details['age']:<8} {details['department']:<15} {details['salary']:<10}")
    else:
        print("Employee not found.\n")


def main_menu():
    while True:
        print("--- MENU ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1' or choice.lower() == 'add employee':
            add_employee()
        elif choice == '2' or choice.lower() == 'view all employees':
            view_employees()
        elif choice == '3' or choice.lower() == 'search for employee':
            search_employee()
        elif choice == '4' or choice.lower() == 'exit':
            print("Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main_menu()


    