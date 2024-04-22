gpa_dict = {"A": 4, "A-": 3.7, "B+": 3.3, "B": 3, "B-": 2.7, 
            "C+": 2.3, "C": 2, "C-": 1.7, "D+": 1.3, "D": 1, "D-": 0.7, "F": 0}
def calculateGPA(courses):
    gpa_total = 0
    credits_sum = 0

    # assuming courses is an array of course objs
    for course in courses:
        # get credits sum
        credits_sum += course["credits"]
    
    # calculate gpa
    for course in courses:
        weight = course["credits"] / credits_sum
        gpa_total += gpa_dict[course["grade"]] * weight

    return gpa_total
