"""Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly."""

a=int(input("enter a number:"))
if(a%2==0):
    print(a,"is number is even.")
else:
    print(a,"is number is odd.")