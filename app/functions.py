gpa_dict = {"A": 4, "A-": 3.7, "B+": 3.3, "B": 3, "B-": 2.7, 
            "C+": 2.3, "C": 2, "C-": 1.7, "D+": 1.3, "D": 1, "D-": 0.7, "F": 0}
"""
gpa_dict is a dictionary that maps letter grades to their corresponding GPA values.
"""

def calculate_GPA(courses):
    """
    Calculate the GPA based on a list of courses.

    :param courses: A list of tuples where each tuple contains the course grade and credits.
    :return: The GPA as a float.
    """
    gpa_total = 0
    credits_sum = 0

    # assuming courses is a list of course objs
    for course in courses:
        # get credits sum
        credits_sum += float(course[1])
    
    # calculate gpa
    for course in courses:
        weight = float(course[1]) / credits_sum
        gpa_total += gpa_dict[course[0]] * weight

    return gpa_total

def calculate_final_exam_grade(current_grade, final_weight, target_grade):
    """
    Calculate the required final exam grade to achieve a target grade in the course.

    :param current_grade: The current grade as a percentage (e.g., 75 for 75%).
    :param target_grade: The target grade as a percentage (e.g., 80 for 80%).
    :param final_weight: The weight of the final exam as a percentage (e.g., 30 for 30%).
    :return: The required final exam grade as a percentage.
    """
    # Convert percentages to decimals for calculation
    current_grade = current_grade / 100
    target_grade = target_grade / 100
    final_weight = final_weight / 100

    # Calculate the required final exam grade
    required_final = (target_grade - (1 - final_weight) * current_grade) / final_weight

    # Convert the result back to a percentage
    required_final_percent = required_final * 100
    return required_final_percent