dbLines = []
with open("C:\\Users\\berti\\Documents\\git\\AdventOfCode2020\\2\\input.txt","r") as f:
    for line in f:
        limit = line.split(" ")[0].split("-")
        letter = line.split(" ")[1][0]
        pw = line.split(" ")[2].replace("\n","")
        dbLines.append([limit,letter,pw])


def pwCheckPartOne():
    pwValid = 0    
    pwErrors = 0 
    for dbLine in dbLines:
        count = dbLine[2].count(dbLine[1])
        lowerLim = int(dbLine[0][0])
        highlim = int(dbLine[0][1])
        if(lowerLim <= count <= highlim):
            pwValid +=1 
        else:
            pwErrors +=1
    print("Part one:")
    print("Valid: " + str(pwValid))
    print("pwErrors: " + str(pwErrors))

def pwCheckPartTwo():
    pwValid = 0    
    pwErrors = 0 
    for dbLine in dbLines:
        indexOne = int(dbLine[0][0]) - 1 # index 1 => index 0
        indexTwo = int(dbLine[0][1]) - 1 
        if((dbLine[2][indexOne] == dbLine[1]) !=
            (dbLine[2][indexTwo] == dbLine[1])):
            pwValid +=1 
        else:
            pwErrors +=1 
    print("Part two:")
    print("Valid: " + str(pwValid))
    print("pwErrors: " + str(pwErrors))
    

pwCheckPartOne()
pwCheckPartTwo()
