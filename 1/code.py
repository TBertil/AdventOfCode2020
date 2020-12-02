
numbers = []
with open("C:\\Users\\berti\\Documents\\git\\AdventOfCode2020\\1\\input.txt","r") as f:
    for line in f:
        numbers.append(int(line))

def getTwoNrs():
    while(len(numbers)):
        baseNr = numbers.pop()
        for secNr in numbers:
            if(secNr != baseNr):
                if(2020 == (baseNr+secNr)):
                    print("Two numbers:")
                    print(baseNr)
                    print(secNr)
                    print(baseNr * secNr)
                    return


def getThreeNrs():
    while(len(numbers)):
        baseNr = numbers.pop()
        for secNr in numbers:
            for thirdNr in numbers:
                if(secNr != thirdNr):
                    if(2020 == (baseNr+secNr+thirdNr)):
                        print("Three numbers:")
                        print(baseNr)
                        print(secNr)
                        print(thirdNr)
                        print(baseNr * secNr * thirdNr)
                        return
getTwoNrs()
getThreeNrs()