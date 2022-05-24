# Python 3.7.8 64-bit
from itertools import chain

# open input.txt to read message, output.txt to write encrypted message and key.txt to get key
def encryption():
    with open("input.txt","r") as file_read, open("output.txt","w") as file_write, open("key.txt","r") as key:
        key = int(key.read())
        char_list = list(chain.from_iterable(file_read))
        for item in char_list:
            if ord(item)>96 and ord(item)<123: # check for valid character (if character is lower english alphabet)
                file_write.write(chr((((ord(item)-97)+key)%26)+97)) # encryption (adding key to every valid characters)
            else:
                file_write.write(item)

def decryption():
    with open("output.txt","r") as file_read, open("key.txt","r") as key:
        key = int(key.read())
        key = 26 - key # substracting key is equal to adding 26-key
        char_list = list(chain.from_iterable(file_read))
        for item in char_list:
            if ord(item)>96 and ord(item)<123: # check for valid character (if character is lower english alphabet)
                print(chr((((ord(item)-97)+key)%26)+97), end='') # decryption (adding key to every valid characters)
            else:
                print(item, end='')

encryption()
decryption()