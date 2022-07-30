# This is the code for finding CGPA of a student.

NS = str(input("Enter your name please: "))
Class = int(input("Enter your Grade/Standard/Class: "))
percentage = float(input("Enter your percentage: "))
cgpa = percentage / 9.5
print(cgpa)
if cgpa >= 9:
    print("Congratulations! Here's your cgpa :)")
elif cgpa <= 8:
    print("Good job! This is your cgpa :)")
elif cgpa <= 7:
    print("This is your cgpa")
