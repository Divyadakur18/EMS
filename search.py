def search_employee(employees):
    key = input("Search by ID or Name: ").strip()

    found = False
    for emp in employees:
        if str(emp["id"]) == key or emp["name"].lower() == key.lower():
            print("\nEmployee Found:")
            print(f"ID: {emp['id']}")
            print(f"Name: {emp['name']}")
            print(f"Department: {emp['department']}")
            print(f"Role: {emp['role']}")
            print(f"Salary: {emp['salary']}\n")
            found = True
            break

    if not found:
        print("Employee not found.")

