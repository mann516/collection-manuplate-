mport datetime

students = {}

def add_student():
    try:
        student_id = input("Enter student ID: ")
        if student_id in students:
            print("Student ID already exists.")
            return
        name = input("Name: ")
        age = int(input("Age: "))
        dob = input("Date of Birth (YYYY-MM-DD): ")
        datetime.datetime.strptime(dob, '%Y-%m-%d')  # Validate date format
        grade = input("Grade: ")
        subjects = input("Subjects (comma-separated): ").split(',')

        students[student_id] = {
            "name": name.strip(),
            "age": age,
            "dob": dob.strip(),
            "grade": grade.strip(),
            "subjects": [s.strip() for s in subjects]
        }

        print("\nStudent added successfully!\n")
    except ValueError:
        print("Invalid input. Please enter data in the correct format.\n")

def display_all_students():
    if not students:
        print("No students found.\n")
        return
    print("\n--- Display All Students ---")
    for sid, info in students.items():
        print(f"Student ID: {sid} | Name: {info['name']} | Age: {info['age']} | "
              f"Grade: {info['grade']} | Subjects: {', '.join(info['subjects'])}")
    print()

def menu():
    while True:
        print("Welcome to the Student Data Organizer!\n")
        print("Select an option:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            print("Update functionality not implemented in this example.\n")
        elif choice == '4':
            print("Delete functionality not implemented in this example.\n")
        elif choice == '5':
            all_subjects = {subject for info in students.values() for subject in info['subjects']}
            print(f"Subjects Offered: {', '.join(all_subjects)}\n")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.\n")

if _name_ == "_main_":
    menu()