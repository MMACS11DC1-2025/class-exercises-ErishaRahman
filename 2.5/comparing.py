"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

file = open("2.4/responses.csv")
name = 0
lineinput = input("whats your name?\n").lower()
lineoutput = input("who are you curious about\n").lower()
lineinputsplit = []
lineoutputsplit = []
for line in file:
    if str(lineinput) in line.lower():
        lineinputsplit = line.split(",")
        #identifier = int(lineinput[0]) # grabs id of name entered
        print(lineinputsplit[1])

    if str(lineoutput) in line.lower():
        lineoutputsplit = line.split(",")
        #identifier = int(lineoutput[0]) # grabs id of name entered
        #print(lineoutput[2])
        print(lineoutputsplit[2])

if lineoutputsplit[2] in lineinputsplit[2]:
    print("You both like the number " + lineoutputsplit[2] + "!")
    name = name+1


if lineoutputsplit[3] in lineinputsplit[3]:
    print("You both like " + lineoutputsplit[3] + " as pets!")
    name = name+1

if lineoutputsplit[4] in lineinputsplit[4]:
    print("You both like " + lineoutputsplit[4] + " the best out of all your subjects!")
    name = name+1

if lineoutputsplit[5] in lineinputsplit[5]:
    print("You both like the number " + lineoutputsplit[5] + "!")
    name = name+1

if lineoutputsplit[6] in lineinputsplit[6]:
    print("You both like playing " + lineoutputsplit[6] + "!")
    name = name+1                

if lineoutputsplit[7] in lineinputsplit[7]:
    print("You both like watching " + lineoutputsplit[7] + "!")
    name = name+1

if lineoutputsplit[8] in lineinputsplit[8]:
    print("You both like the music genre " + lineoutputsplit[8] + "!")
    name = name+1

if lineoutputsplit[9] in lineinputsplit[9]:
    print("You both like " + lineoutputsplit[9]+"!")
    name = name+1



if name <= 4:
    print("You two don't have much in common")
elif name > 4 and name <= 6:
    print("You two have some things in common")
elif name > 6 and name <= 8:
    print("You two have a lot in common")
elif name >= 8:
    print("You two are like twins!")
else: 
    print("it seems this didn't work")
    
print(name)
print(lineinputsplit[2] == lineoutputsplit[2])




