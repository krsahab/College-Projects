with open("input.txt", "r") as inputFile:
    a, b, c = map(int,inputFile.read().split()) #input file should contain 3 space saperated integers for a, b and c

def computeModulo(a, b, c):
    #c cannot be less then or equal to 0
    if c<=0 or b<0:
        print("Invalid Input")
        return
    #0^b = 0
    if a==0:
        return 0
    #a^0 = 1 (if c!=1)
    if b==0:
        if c==1:
            return 0
        return 1
    temp = 0
    #If c is even
    if b%2 == 0:
        temp = computeModulo(a, b/2, c)%c
        temp = (temp*temp)%c
    #If c is odd
    else:
        temp = a%c
        temp = (temp*(computeModulo(a, b-1, c)%c))%c
    
    #Handle -ve a
    return (temp+c)%c

with open("output.txt","w") as outputFile:
    outputFile.write(str(computeModulo(a, b, c)))