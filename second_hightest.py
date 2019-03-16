def second_highest(students):
    grades = [s[1] for s in students]
    grades = sorted(grades, reverse=True)
    second = grades[1]
    
    second_high_students = [s[0] for s in students if s[1] == second]
    for student in second_high_students:
        print(student)

student = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]
second_highest(student)