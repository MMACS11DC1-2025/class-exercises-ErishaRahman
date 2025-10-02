"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

file = open("2.4/responses.csv")
score = 0
lineinput = input("whats your name?\n").lower()

for line in file:
    if str(lineinput) in line.lower():
        lineinput = line.split(",")
        print("greetings " + str(lineinput[1]) + ".\n")
        identifier = int(lineinput[0]) # grabs id of name entered
        print(lineinput[0])


with open("2.4/responses.csv", "r") as file: #when its open idk what to tell u
    all_lines = file.readlines()

    iteration = -1 # set at -1 to register the first line as line 0 so its like easier to work out
    for line in all_lines:
        iteration = iteration + 1 # amount of times the loop has happened
        if iteration == identifier: # checks if the line # matches the identifier(id) we have (ex line 3= id 3)
            line = line.split(",") # splits the line into a list 
            break # stops when the identifier actually matches

    #PLEASE WORK I WANNA GO TO BED PLEASEEEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASE
print(lineinput[1])
print(lineinput[0])
print(line[2])

for line in all_lines:
    if line[2] == lineinput[2]:
        print("kothar batcha")

'''
for line in all_lines:
+
    if line[2] == lineinput[2]:
            score[iteration] = score[iteration] + 1 # adds new score


    if line[3] == lineinput[3]:
            score[iteration] = score[iteration] + 1 # adds new score

    if line[4] == lineinput[4]:
            score[iteration] = score[iteration] + 1 # adds new score

    if line[5] == lineinput[5]:
            score[iteration] = score[iteration] + 1 # adds new score

    if line[6] == lineinput[6]:
            score[iteration] = score[iteration] + 1 # adds new score

    if line[7] == lineinput[7]:
            score[iteration] = score[iteration] + 1 # adds new score

    if line[8] == lineinput[8]: 
            score[iteration] = score[iteration] + 1 # adds new score

'''


print("hi!")

    # outside for loop
    # loop everything in score[]
    # find highest score
    # print winner 


\
    

        





