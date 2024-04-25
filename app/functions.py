gpa_dict = {"A": 4, "A-": 3.7, "B+": 3.3, "B": 3, "B-": 2.7, 
            "C+": 2.3, "C": 2, "C-": 1.7, "D+": 1.3, "D": 1, "D-": 0.7, "F": 0}
def calculate_GPA(courses):
    gpa_total = 0
    credits_sum = 0

    # assuming courses is a list of course objs
    for course in courses:
        # get credits sum
        credits_sum += course["credits"]
    
    # calculate gpa
    for course in courses:
        weight = course["credits"] / credits_sum
        gpa_total += gpa_dict[course["grade"]] * weight

    return gpa_total

courses = [{"grade": "A", "credits": 2}, {"grade": "C", "credits": 1}, {"grade": "C", "credits": 1}]
# print(calculate_GPA(courses))

def percent_to_grade(percent):
    if percent >= 93:
        return 'A'
    elif percent >= 90:
        return 'A-'
    elif percent >= 87:
        return 'B+'
    elif percent >= 83:
        return 'B'
    elif percent >= 80:
        return 'B-'
    elif percent >= 77:
        return 'C+'
    elif percent >= 73:
        return 'C'
    elif percent >= 70:
        return 'C-'
    elif percent >= 67:
        return 'D+'
    elif percent >= 63:
        return 'D'
    elif percent >= 60:
        return 'D-'
    else:
        return 'F'

def calculate_course_grade(grades):
    grade_sum = 0
    total_weight = 0

    # assuming grades is a list of assignment objects with a number grade and weight
    for grade in grades:
        grade_sum += grade["percent"] * grade["weight"]
        total_weight += grade["weight"]
    
    weighted_grade = grade_sum / total_weight
    letter_grade = percent_to_grade(weighted_grade)
    percent_and_letter = {"percent": weighted_grade, "letter": letter_grade}

    # return obj containing percent and letter grade
    return percent_and_letter

assignments = [{"percent": 90, "weight": 10}, {"percent": 95, "weight": 10}, {"percent": 80, "weight": 30}, {"percent": 80, "weight": 30}]
# print(calculate_course_grade(assignments))

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