def view_employees(employees):
    if not employees:
        print("No employees found.")
        return

    print("\n{:<5} {:<15} {:<15} {:<15} {:<10}".format("ID", "Name", "Department", "Role", "Salary"))
    print("-" * 60)
    for emp in employees:
        print("{:<5} {:<15} {:<15} {:<15} {:<10}".format(
            emp["id"], emp["name"], emp["department"], emp["role"], emp["salary"]
        ))
    print()

