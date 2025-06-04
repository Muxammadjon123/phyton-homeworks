def add_employee():
    with open('employees.txt', 'a') as file:
        while True:
            employee_id = input("Please enter employee's ID: ").strip()
            name = input("Please enter the name of employee: ").strip()
            position = input("Please enter the position of employee: ").strip()
            salary = input("Please enter the salary of employee: ").strip()

            record = f"{employee_id},{name},{position},{salary}\n"
            file.write(record)
            print(" Record added successfully!")

            choice = input("Do you want to add another employee (y/n)? ").strip()
            if choice.lower() == 'n':
                break


def view_all_employees():
    try:
        with open("employees.txt", 'r') as file:
            print("\n EMPLOYEE RECORDS:\n")
            lines = file.readlines()
            if not lines:
                print("No records found.")
            else:
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print(" File not found.")


def search_employee():
    emp_id = input("Please enter the Employee ID to search: ").strip()
    found = False
    try:
        with open("employees.txt", 'r') as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("\n Employee Found:\n" + line.strip())
                    found = True
                    break
        if not found:
            print(" Employee not found.")
    except FileNotFoundError:
        print(" File not found.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ").strip()
    updated_lines = []
    found = False
    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(emp_id + ","):
                    print("Current record:", line.strip())
                    name = input("New Name: ").strip()
                    position = input("New Position: ").strip()
                    salary = input("New Salary: ").strip()
                    updated_line = f"{emp_id},{name},{position},{salary}\n"
                    updated_lines.append(updated_line)
                    found = True
                else:
                    updated_lines.append(line)

        if found:
            with open("employees.txt", "w") as file:
                file.writelines(updated_lines)
            print(" Employee updated successfully.")
        else:
            print(" Employee not found.")
    except FileNotFoundError:
        print(" No records file found.")


def delete_employee():
    emp_id = input("Please enter the ID of employee to delete: ").strip()
    found = False
    updated_lines = []
    try:
        with open("employees.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if not line.startswith(emp_id + ','):
                    updated_lines.append(line)
                else:
                    found = True

        if found:
            with open("employees.txt", 'w') as file:
                file.writelines(updated_lines)
            print("Employee deleted successfully.")
        else:
            print(" Employee not found.")
    except FileNotFoundError:
        print(" File not found.")


def menu():
    while True:
        print("\n========== Employee Management System ==========")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        print("===============================================\n")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_all_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice. Please select a number between 1 and 6.")



menu()
