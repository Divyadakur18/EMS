def delete_employee(employees):
    try:
        emp_id = int(input("Enter the Employee ID to delete: "))
        for i, emp in enumerate(employees):
            if emp["id"] == emp_id:
                del employees[i]
                print("Employee deleted successfully!")
                return
        print("Employee ID not found.")
    except ValueError:
        print("Invalid input.")

