from add import add_employee
from view import view_employees
from search import search_employee
from update import update_employee
from delete import delete_employee

def menu():
    employees = []

    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            update_employee(employees)
        elif choice == '5':
            delete_employee(employees)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice. Please select from 1 to 6.")

# Run the program
if __name__ == "__main__":
    menu()
