# This module contains functions to process and display student data.
# It provides formatting utilities and printing helpers for student records.

def format_student_data(student):
    """
    Format a single student record into a human-readable string.

    Args:
        student (tuple): A student tuple in the form (ID, Name, Major).

    Returns:
        str: A formatted string in the form:
             "ID: <id> | Name: <name> | Major: <major>"

    Example:
        >>> format_student_data((101, "Alice Johnson", "Computer Science"))
        'ID: 101 | Name: Alice Johnson | Major: Computer Science'
    """
    # Unpack the tuple fields for clarity, then use an f-string to format.
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(student_list):
    """
    Print all student records to the console.

    Loops through every student in student_list, formats each one using
    format_student_data(), and prints the result.

    Args:
        student_list (list): A list of student tuples (ID, Name, Major).

    Returns:
        None
    """
    # Iterate over every student and print their formatted details.
    for student in student_list:
        print(format_student_data(student))