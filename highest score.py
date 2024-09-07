student_scores = input("Input a list of student scores: ").split()
for n in range(len(student_scores)):
    student_scores[n] = int(student_scores[n])
highest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")