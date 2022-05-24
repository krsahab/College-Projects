# Python 3.7.8 64-bit
from itertools import chain

def decryption(key):
    with open("output.txt","r") as file_read:
        key = 26 - key # substracting key is equal to adding 26-key
        char_list = list(chain.from_iterable(file_read))
        message = str()
        for item in char_list:
            if ord(item)>96 and ord(item)<123: # check for valid character (if character is lower english alphabet)
                message+=(chr((((ord(item)-97)+key)%26)+97)) # decryption (adding key to every valid characters)
            else:
                message+=item
        return message

def isValid(message):
    # some message validation logic
    if "sample text" in message:
        return True

def bruteforce():
    for key in range(1,27):
        message = decryption(key) # Get decrypted message for every key
        if isValid(message):
            print("Key is :", key)
            print("Message is :")
            print(message)
            break

bruteforce()