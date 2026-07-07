""" Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist."""

try:
    file_name = open("sample.txt", "rt")
    
    print("Reading file content:")
    
    line_no = 1  #line number will start from 1
    line = file_name.readline()  #1st line gets read
    
    while line:  #loop runs untill the content ends
        print(f"Line {line_no}: {line.strip()}")  #print's line number
        line_no += 1   #increase the number of line
        line = file_name.readline()
    
    file_name.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")




