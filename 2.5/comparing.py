"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

file = open("2.4/responses.csv")
lineinput = input("whats your name?").lower()
lineinput2 = input("who are you comparing yourself to?").lower().strip()
"""
##fileList = file.read().strip().split("\n")
line = fileList[22].split(',')
col1 = line[1]
print(col1 == line[6])
"""
for line in file:
    if lineinput in line.lower():
        lineinput = line.split(",")
        print("greetings" + lineinput[1] + ".\n")
       

        """
    if lineinput2 in line.lower():
        print(line)
        myline = line
"""





