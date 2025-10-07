def update_employee(employees):
    try:
        emp_id = int(input("Enter the Employee ID to update: "))
        for emp in employees:
            if emp["id"] == emp_id:
                print("Which field do you want to update?")
                print("1. Department")
                print("2. Role")
                print("3. Salary")
                choice = input("Enter choice (1-3): ")

                if choice == '1':
                    emp["department"] = input("Enter new department: ")
                elif choice == '2':
                    emp["role"] = input("Enter new role: ")
                elif choice == '3':
                    emp["salary"] = float(input("Enter new salary: "))
                else:
                    print("Invalid choice.")
                    return
                print("Employee updated successfully!")
                return
        print("Employee ID not found.")
    except ValueError:
        print("Invalid input.")

