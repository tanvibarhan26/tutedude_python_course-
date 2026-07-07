'''Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file. '''

#first input
with open("output.txt", 'w') as fh:
    text1=input("Enter a text to write to the file:")
    fh.write(text1 + "\n")
    fh.close()
print("Data successfully written to the output.txt.")

#append input
with open("output.txt", 'a') as fh:
    text2=input("Enter additional data to append:")
    fh.write(text2)
    fh.close()
print("Data sucessfully append.")

#print the whole output of the file
print("Final content of output.txt:")
with open("output.txt", "r") as fh:
    content = fh.read()
    print(content)


