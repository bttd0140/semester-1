# Worksheet 1.2: Task 1 solution 
import sys

grade_input = input()
if not grade_input.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = int(grade_input)
if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade >= 70:
    result = "Distinction"
elif grade >= 40:
    result = "Pass"
else:
    result = "Fail"

print(f"{grade} is a {result}")