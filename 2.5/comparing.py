"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.


1. get names from two people you want to compare 
2. compare them and 
    add a point if they match
    add their choice to the recs list using append
3. print compatibility outcomes
"""
#simple stuff, get their names and assign them to variables
#and split
file = open("2.4/responses.csv")
shared = 0
print("Hello! ill help you compare your interests with another person from the mini school 10 class!")
lineinput = input("whats your name?\n").lower()
lineoutput = input("who are you curious about\n").lower()

lineinputsplit = []
lineoutputsplit = []

recs = []

for line in file:
    if str(lineinput) in line.lower():
        lineinputsplit = line.split(",")
        #identifier = int(lineinput[0])
        #print(lineinputsplit[1])
    else:#enter the name right or else.
        quit("oops, you might have misspelled your name, please try again")

    if str(lineoutput) in line.lower():
        lineoutputsplit = line.split(",")
        #identifier = int(lineoutput[0]) 
        #print(lineoutput[2])
        #print(lineoutputsplit[2])
    else:
        quit("oops, you might have misspelled their name, please try again")


#compares and counts shared interests
#adds to recs if not shared
print("\nAlright, lets see how compatible you two are!\n")
if lineoutputsplit[2] in lineinputsplit[2]:
    print("You both like the number " + lineoutputsplit[2] + "!")
    shared = shared+1
else:
    print("You two don't like the same number")
    

if lineoutputsplit[3] in lineinputsplit[3]:
    print("You both like " + lineoutputsplit[3] + " as pets!")
    shared = shared+1
else:
    print("You two don't like the same pet")
    recs.append(lineoutputsplit[3])

if lineoutputsplit[4] in lineinputsplit[4]:
    print("You both like " + lineoutputsplit[4] + " the best out of all your subjects!")
    shared = shared+1
else:
    print("You two don't like the same subject")
    recs.append(lineoutputsplit[4])

if lineoutputsplit[5] in lineinputsplit[5]:
    print("You both like playing " + lineoutputsplit[5] + "!")
    shared = shared+1  
else:  
    print("You two don't like playing the same sport") 
    recs.append(lineoutputsplit[5])             

if lineoutputsplit[6] in lineinputsplit[6]:
    print("You both like watching " + lineoutputsplit[6] + "!")
    shared = shared+1
else:    
    print("You two don't like watching the same sport.")
    recs.append(lineoutputsplit[6])

if lineoutputsplit[7] in lineinputsplit[7]:
    print("You both like the music genre " + lineoutputsplit[7] + "!")
    shared = shared+1
else:    
    print("You two don't like the same music genre")
    recs.append(lineoutputsplit[7])

if lineoutputsplit[8] in lineinputsplit[8]:
    print("You both like the media genre " + lineoutputsplit[8] + "!")
    shared = shared+1
else:    
    print("You two don't like the same media genre")
    recs.append(lineoutputsplit[8])    

if lineoutputsplit[9] in lineinputsplit[9]:
    print("You both like " + lineoutputsplit[9]+"!\n")
    shared = shared+1
else:    
    print("You two don't like the same food\n")
    recs.append(lineoutputsplit[9])
#get that percent ready OH YEAH
#print(shared)

pervalue = (shared/8) * 100
print("You (" + lineinputsplit[1] +") are compatible with " + lineoutputsplit[1] + " by " + str(pervalue) + "%\n")
#different dialoge omg
if shared <= 2:
    print("You two don't have much in common, so i cannot recommend anything based on their interests, sorry.")
elif shared > 2 and shared <= 4:
    print("You two have some things in common, so you might like, ")
    print(", ".join(recs))
elif shared > 4 and shared <= 7:
    print("You two have a lot in common, so i would definitely recommend,")
    print(", ".join(recs))
elif shared == 8:
    print("You guys are twins, arent you?")
else: 
    print("it seems this didn't work, sorry")

#print(lineinputsplit[2] == lineoutputsplit[2])
#print(recs)



