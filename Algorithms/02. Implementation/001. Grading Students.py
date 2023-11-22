# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    # Write your code here
    updatedGrades = []
    for grade in grades:
        if grade >= 38:
            bar = ((grade // 5) + 1) * 5
            if (bar - grade) < 3:
                #print(bar)
                updatedGrades.append(int(bar))
            else:
                #print(grade)
                updatedGrades.append(int(grade))
        else:
            #print(grade)
            updatedGrades.append(int(grade))

    return updatedGrades


grades = [73, 67, 38, 33]

afterUpdate = gradingStudents(grades)

for g in afterUpdate:
    print(g)