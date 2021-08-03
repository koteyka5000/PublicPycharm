exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_3 = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_3]

sum = 0
for grade in grades:
    sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "5"
elif 80 <= avg < 90:
    letter_grade = "4"
elif 69 < avg < 80:
    letter_grade = "3"
elif 69 >= avg >= 65:
    letter_grade = "2"
else:
    letter_grade = "1"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)
if letter_grade is "1":
    print("Student is failing.")
else:
    print("Student is passing.")
