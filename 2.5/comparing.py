#Hello! This program will help you compare your interests with another person from the mini school 10 class!
#It will also recommend things based on their interests if you two dont have much in common
#I used a csv file to store the data, so make sure its in the same folder


#simple stuff, get their names and assign them to variables
#and split
file = open("2.4/responses.csv")

shared = 0
errorone = 0
errortwo = 0

print("Hello! ill help you compare your interests with another person from the mini school 10 class!")

lineinput = input("whats your name?\n").strip().lower()
lineoutput = input("who are you curious about\n").strip().lower()

lineinputsplit = []
lineoutputsplit = []

recs = []


for line in file:
    if str(lineinput) in line.lower():
        lineinputsplit = line.split(",")

        #testing stuff
        #identifier = int(lineinput[0])
        #print(lineinputsplit[1])
        
    else: #incase of misspelling
        errorone = errorone + 1
        

    if str(lineoutput) in line.lower():
        lineoutputsplit = line.split(",")

        #testing
        #identifier = int(lineoutput[0]) 
        #print(lineoutput[2])
        #print(lineoutputsplit[2])

    else:  
        errortwo = errortwo + 1

#when mispell
if errorone >= 28:
    quit("oops, you might have misspelled a name, please try again") 

if errortwo >= 28:
    quit("oops, you might have misspelled a names, please try again")

# code testing booooo
#if str(lineinput) not in file.read().lower():
    #quit("oops, you might have misspelled one of the names, please try again")

#compares and counts shared interests
#adds to recs if not shared
print("\nAlright, lets see how compatible you two are!\n")

#i separated the number part because that rec doent make sense
if lineoutputsplit[2] in lineinputsplit[2]:
    print("You both like the number " + lineoutputsplit[2] + "!")
    shared = shared+1
#loop to make it less repetitive
for i in range(3,8):
    if lineoutputsplit[i] in lineinputsplit[i]:
        print("You both like the number " + lineoutputsplit[i] + "!")
        shared = shared+1
    else:
        recs.append(lineoutputsplit[i])

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
















#old ugly codeeeeee
"""
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
"""
