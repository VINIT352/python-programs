
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
sub4 = float(input("Enter marks for subject 4: "))
sub5 = float(input("Enter marks for subject 5: "))


total_marks = sub1 + sub2 + sub3 + sub4 + sub5


avg_marks = total_marks / 5


percent_marks = (total_marks / 500) * 100

if percent_marks >= 90:
    grade = 'A+'
elif percent_marks >= 80:
    grade = 'A'
elif percent_marks >= 70:
    grade = 'B'
elif percent_marks >= 60:
    grade = 'C'
elif percent_marks >= 50:
    grade = 'D'
else:
    grade = 'F'


print("Total marks: ", total_marks)
print("Average marks: ", avg_marks)
print("Percentage marks: {:.2f}%".format(percent_marks))
print("grade is:",grade)
