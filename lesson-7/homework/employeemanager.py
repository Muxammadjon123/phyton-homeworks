class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}"


class EmployeeManager:
    def __init__(self, file_name="employee.txt"):
        self.file_name = file_name

    def add_employee(self):
        employee_id = input("Please enter the ID of employee: ")
        name = input("Please enter the name of employee: ")
        position = input("Please enter the position of employee: ")
        salary = input("Please enter the salary of employee: ")
        employee = Employee(employee_id, name, position, salary)

        with open(self.file_name, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employee(self):
        try:
            with open(self.file_name, 'r') as file:
                records = file.readlines()
                if not records:
                    print("No records found.")
                else:
                    for line in records:
                        print(line.strip())
        except FileNotFoundError:
            print("File not found.")

    def search_employee(self):
        emp_id = input("Please enter the ID of employee: ")
        found = False
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    if line.startswith(emp_id + ","):
                        print("Employee found: " + line.strip())
                        found = True
                        break
            if not found:
                print("Employee not found.")
        except FileNotFoundError:
            print("File not found.")

    def update_employee(self):
        emp_id = input("Please enter the ID of employee to update: ")
        updated_lines = []
        updated = False
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    if line.startswith(emp_id + ","):
                        print(f"Updating info for employee ID {emp_id}")
                        name = input("Enter updated name: ")
                        position = input("Enter updated position: ")
                        salary = input("Enter updated salary: ")
                        updated_lines.append(f"{emp_id},{name},{position},{salary}\n")
                        updated = True
                    else:
                        updated_lines.append(line)
        except FileNotFoundError:
            print("File not found.")
            return

        if updated:
            with open(self.file_name, 'w') as file:
                file.writelines(updated_lines)
            print("Employee information updated successfully.")
        else:
            print("Employee ID not found.")

    def delete_employee(self):
        emp_id = input("Please enter the ID of employee to delete: ")
        deleted = False
        updated_lines = []
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    if line.startswith(emp_id + ","):
                        deleted = True
                        continue
                    updated_lines.append(line)
        except FileNotFoundError:
            print("File not found.")
            return

        if deleted:
            with open(self.file_name, 'w') as file:
                file.writelines(updated_lines)
            print("Employee deleted successfully.")
        else:
            print("Employee ID not found.")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employee()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
