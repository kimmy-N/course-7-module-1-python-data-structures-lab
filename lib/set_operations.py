# This module contains set-based operations for student data.
# Sets are ideal for tracking unique values because they automatically
# eliminate duplicates and support efficient membership testing (O(1) lookup).

def unique_majors(student_list):
    """
    Return a set of unique student majors using a set comprehension.

    A set comprehension is used (instead of a loop + .add()) because it
    is concise, expressive, and directly communicates the intent of
    collecting unique values.

    Args:
        student_list (list): A list of student tuples (ID, Name, Major).

    Returns:
        set: A set containing each distinct major present in student_list.
             Returns an empty set if student_list is empty.

    Example:
        >>> unique_majors(students)
        {'Computer Science', 'Mathematics', 'Physics'}
    """
    # Set comprehension: extract the major field (index 2) from each student.
    # Duplicate majors are automatically discarded by the set data structure.
    return {student[2] for student in student_list}
