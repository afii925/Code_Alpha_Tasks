 
## Student Grade Tracker 


def add_student(students):
    student_name = input("Enter the student's name: ")
    if student_name not in students:
        students[student_name] = {}
        print(f"Student '{student_name}' added.")
    else:
        print(f"Student '{student_name}' already exists.")

def add_grade(students):
    student_name = input("Enter the student's name: ")
    if student_name not in students:
        print(f"Student '{student_name}' does not exist. Please add the student first.")
        return

    subject = input("Enter the subject name: ")
    try:
        grade = float(input("Enter the grade: "))
        if subject in students[student_name]:
            students[student_name][subject].append(grade)
        else:
            students[student_name][subject] = [grade]
        print(f"Grade {grade} added for student '{student_name}' in subject '{subject}'.")
    except ValueError:
        print("Invalid input! Please enter a numeric grade.")

def view_grades(students):
    student_name = input("Enter the student's name: ")
    if student_name not in students:
        print(f"Student '{student_name}' does not exist.")
        return

    if not students[student_name]:
        print(f"No grades recorded for student '{student_name}'.")
        return

    print(f"Grades for {student_name}:")
    for subject, grade_list in students[student_name].items():
        print(f"{subject}: {', '.join(map(str, grade_list))}")

def calculate_average(students):
    student_name = input("Enter the student's name: ")
    if student_name not in students:
        print(f"Student '{student_name}' does not exist.")
        return

    if not students[student_name]:
        print(f"No grades recorded for student '{student_name}'.")
        return

    total_sum = 0
    total_count = 0
    for grade_list in students[student_name].values():
        total_sum += sum(grade_list)
        total_count += len(grade_list)

    if total_count == 0:
        print("No grades to calculate average.")
    else:
        average = total_sum / total_count
        print(f"Overall average grade for {student_name}: {average:.2f}")

def display_menu():
    print("\nStudent Grade Tracker")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Grades")
    print("4. Calculate Average")
    print("5. Exit")

def main():
    students = {}
    while True:
        display_menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            add_grade(students)
        elif choice == '3':
            view_grades(students)
        elif choice == '4':
            calculate_average(students)
        elif choice == '5':
            print("Exit the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()