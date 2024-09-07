student_heights = input("Input a list of student heights: ").split()
for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])
total = 0
for height in student_heights:
    total += height
students = 0
for student in student_heights:
    students += 1
if students > 0:  
    average = round(total / students)
    print(f"The average height is {average}")
else:
    print("No students were input.")