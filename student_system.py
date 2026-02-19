# Student Data Management System
# Author: Your Name

# List to store students
students = []

# Function to add a student
def add_student():
    print("\nAdd New Student")
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter age: ")
    major = input("Enter major: ")
    courses_input = input("Enter completed courses (comma separated): ")
    courses = [course.strip() for course in courses_input.split(",")]  # Remove extra spaces
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "major": major,
        "courses": courses
    }
    students.append(student)
    print("Student added successfully!\n")


# Function to view all students
def view_students():
    if not students:
        print("\nNo students available.")
    else:
        print("\nAll Students:")
        for student in students:
            print(student)


# Function to find students by major using list comprehension
def find_students_by_major():
    major = input("Enter major to filter by: ").strip()
    filtered_students = [student for student in students if student["major"].lower() == major.lower()]
    
    if filtered_students:
        print(f"\nStudents in {major} major:")
        for student in filtered_students:
            print(student)
    else:
        print(f"No students found in {major} major.")


# Function to find students by course using a generator
def find_students_by_course():
    course = input("Enter course to filter by: ").strip()
    filtered_students = (student for student in students if course in student["courses"])
    
    found = False
    print(f"\nStudents who completed {course}:")
    for student in filtered_students:
        print(student)
        found = True

    if not found:
        print(f"No students found who completed {course}.")


# -----------------------------
# Menu system at the bottom
def main_menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add a student")
        print("2. View all students")
        print("3. Find students by major")
        print("4. Find students by course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            find_students_by_major()
        elif choice == "4":
            find_students_by_course()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


# Run the menu
if __name__ == "__main__":
    main_menu()


        
