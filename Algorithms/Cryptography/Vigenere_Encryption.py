from itertools import chain

#Read text and key and convert it into Upper Case
with open("Sample_Vigenere.txt","r") as file_read, open("Vigenere_key.txt","r") as keyFile:
    char_list = list(map(lambda x : x.upper(),chain.from_iterable(file_read)))
    key = keyFile.read().upper()


def Encryption(key, text_chars):
    j=0
    cipher = str()
    #Encrypt each english character in text using key
    for char in text_chars:
        if ord(char)>64 and ord(char)<91:
            cipher += chr((((ord(char)-65)+(ord(key[j])-65))%26)+65)
            j = (j+1)%len(key)
        else:
            cipher += char
    #Write Encrypted Message to output file
    with open("output.txt","w") as fileWrite:
        fileWrite.write(cipher)

Encryption(key, char_list)