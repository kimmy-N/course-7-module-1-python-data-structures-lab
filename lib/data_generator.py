# This module contains generator-based functions for lazy student data retrieval.
# Generator expressions are memory-efficient: unlike lists, they produce items
# one at a time on demand rather than building the entire result in memory.
# This is particularly valuable when working with large student datasets.

def student_generator(student_list, major):
    """
    Lazily yield student records filtered by major using a generator expression.

    Unlike filter_students_by_major() (which builds a complete list in memory),
    this function returns a generator object that produces one student at a time.
    Callers use next() or a for loop to consume values only when needed.

    Args:
        student_list (list): A list of student tuples (ID, Name, Major).
        major (str): The major to filter students by (case-insensitive).

    Yields:
        tuple: Student tuples (ID, Name, Major) whose major matches the argument.

    Example:
        >>> gen = student_generator(students, "Mathematics")
        >>> next(gen)
        (102, 'Bob Smith', 'Mathematics')
        >>> next(gen)
        (105, 'Eve Lewis', 'Mathematics')
    """
    # Generator expression: same logic as a list comprehension, but wrapped
    # in () instead of [] so Python produces values lazily (no upfront memory).
    return (
        student
        for student in student_list
        if student[2].lower() == major.lower()
    )
