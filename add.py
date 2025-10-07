from constants import MAX_EMPLOYEES

def add_employee(employees):
    if len(employees) >= MAX_EMPLOYEES:
        print("Cannot add more employees. Maximum limit reached.")
        return

    try:
        emp_id = int(input("Enter Employee ID: "))
        # Check for duplicate ID
        for emp in employees:
            if emp["id"] == emp_id:
                print("Employee with this ID already exists.")
                return
        name = input("Enter Name: ").strip()
        department = input("Enter Department: ").strip()
        role = input("Enter Role: ").strip()
        salary = float(input("Enter Salary: "))

        employee = {
            "id": emp_id,
            "name": name,
            "department": department,
            "role": role,
            "salary": salary
        }

        employees.append(employee)
        print(" Employee added successfully!")

    except ValueError:
        print(" Invalid input. Please enter correct data types.")
