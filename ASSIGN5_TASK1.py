"""Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""
#Build a dictionary 
student_marks={
            "John":88,
            "Tanvi":100,
            "Max":56,
            "Tom":12,
            "Carol":65
}

#taking input from user
student_name= input("Enter the student's name:").capitalize()
marks = student_marks.get(student_name)
if marks:
    print(f"The marks of {student_name} is: {marks}")

else:
    print(f"Student not found.")
