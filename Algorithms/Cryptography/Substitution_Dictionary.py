with open("usa.txt") as dictFile, open("output.txt") as inputFile:
    text = inputFile.read() #Cipher text from output.txt
    dict = dictFile.read().splitlines() #USA English Dictionary words

#Dictionary Attack
def isValid(message):
    #Check if each decrypted words are available in dictionary
    for item in message: 
        if item.lower() not in dict:
            return False
    return True

def breakCipher():
    for i in range(26): # Brute-force for all possible keys i.e. [0-25]
        message = ""
        #Decode message for each key
        for c in text:
            if ord(c)>64 and ord(c)<91:
                message+= chr((((ord(c)-65)+i)%26)+65)
            else:
                message+=c
        #Check if Decoded Message is valid
        if isValid(message.split()):
            #If Decoded Message is valid, write it into respective files and break loop
            with open("plaintext.txt", "w") as plaintextFile, open("key.txt", "w") as keyFile:
                plaintextFile.write(message)
                keyFile.write(str(i))
            break;

breakCipher()