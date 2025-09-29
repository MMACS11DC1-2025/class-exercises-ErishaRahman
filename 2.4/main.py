file = open("2.4/responses.csv")
lineinput = input("whats your name?").lower().strip()
for line in file:
    if lineinput in line.lower():
        print(line)
        myline = line

lineinput2 = input("who are you comparing yourself to?").lower().strip()
for line in file:
    if lineinput2 in line.lower():
        print(line)
        myline = line

