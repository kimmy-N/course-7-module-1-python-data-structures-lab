# This module contains functions for filtering student data.
# List comprehensions are used for concise, readable, and Pythonic filtering.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.

    Args:
        student_list (list): A list of student tuples (ID, Name, Major).
        major (str): The major to filter students by (case-insensitive).

    Returns:
        list: A new list containing only the student tuples whose major
              matches the given major string.

    Example:
        >>> filter_students_by_major(students, "Mathematics")
        [(102, 'Bob Smith', 'Mathematics'), (105, 'Eve Lewis', 'Mathematics')]
    """
    # List comprehension: iterate over all students and keep only those
    # whose major matches the requested major (case-insensitive comparison).
    return [
        student
        for student in student_list
        if student[2].lower() == major.lower()
    ]
