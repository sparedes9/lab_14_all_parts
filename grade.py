"""
grade.py
=====
Translate a numeric grade to a letter grade.
1. Ask the user for a numeric grade.
2. Use the table below to calculate the corresponding letter:
    90-100 - A
    80-89  - B
    70-79  - C
    60-69  - D
     0-59  - F
3. Print out both the number and letter grade.
4. If the value is not numeric, allow the error to happen.
5. However, if the number is not within the ranges specified in the table, output:
    "Could not translate %s into a letter grade" where %s is the numeric grade"

Example Output (consider text after the ">" user input):

Run 1:
-----
What grade did you get?
> 59
Number Grade: 59
Letter Grade: F

Run 2:
-----
What grade did you get?
> 89
Number Grade: 89
Letter Grade: B

Run 3:
-----
What grade did you get?
> 90
Number Grade: 90
Letter Grade: A

Run 4:
-----
What grade did you get?
> -12
Couldn't translate -12 into a letter grade
"""

grade = int(raw_input("What is your grade? \n"))

if(grade >=90 and grade <= 100):
	print("Number Grade: " + str(grade))
	print("Letter Grade: A")
elif(grade <=89 and grade >=80):
	print("Number Grade: " + str(grade))
	print("Letter Grade: B")
elif(grade <=79 and grade >=70):
	print("Number Grade: " + str(grade))
	print("Letter Grade: C")
elif(grade <=69 and grade >=60):
	print("Number Grade: " + str(grade))
	print("Letter Grade: D")
else:
	print("GO STUDY!")
	print("Number Grade: " + str(grade))
	print("Letter Grade: F")
