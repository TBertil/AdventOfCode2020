
numbers = []
with open("C:\\Users\\berti\\Documents\\git\\AdventOfCode2020\\1\\input.txt","r") as f:
    for line in f:
        numbers.append(int(line))

savedNr = []
multiplied = 0

def getNrs():
    while(len(numbers)):
        baseNr = numbers.pop()
        for secNr in numbers:
            for thirdNr in numbers:
                if(secNr != thirdNr):
                    if(2020 == (baseNr+secNr+thirdNr)):
                        print(baseNr)
                        print(secNr)
                        print(thirdNr)
                        print(baseNr * secNr * thirdNr)
                        return
getNrs()