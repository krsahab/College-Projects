from itertools import chain

file_read = open("message.txt","r")
char_list = list(filter(lambda x: ord(x)>64 and ord(x)<91, list(chain.from_iterable(file_read)))) #Read all characters from file
letter_freq = {'A':8.2, 'B':1.5, 'C':2.8, 'D':4.3, 'E':13, 'F':2.2, 'G':2, 'H':6.1, 'I':7, 'J':0.15, 'K':0.77, 'L':4, 'M':2.4, 'N':6.7, 'O':7.5, 'P':1.9, 'Q':0.095, 'R':6, 'S':6.3, 'T':9.1, 'U':2.8, 'V':0.98, 'W':2.4, 'X':0.15, 'Y':2, 'Z':0.074} #English letter frequencies

#Calculate frequency of each character in a text
def cal_char_freq(text):
    charfreq = {}
    for item in text:
        if ord(item)>64 and ord(item)<91: #[A-Z]
            if item in charfreq:
                charfreq[item]+=1
            else:
                charfreq[item] = 1
    return charfreq

#Calculate IOC
def IOC(text_group):
    charfreq = cal_char_freq(text_group)
    ioc_cal = 0
    for item in charfreq.values():
        ioc_cal+=(item*(item-1)) # sum(k(k-1))
    ioc_cal = ioc_cal/(len(text_group)*(len(text_group)-1)) #sum/N(N-1)
    return ioc_cal

#make groups of letters at distane of given key length
def make_group(text, key_length):
    text_group = []
    for i in range(key_length):
        temp_text = str()
        j = i;
        while j<len(text):
            temp_text += text[j]
            j+=key_length
        text_group.append(temp_text)
    return text_group

#Calculate Key Length
def cal_key_len():
    possible_length = []
    for length in range(1,int(len(char_list)/10)+1): #Assuming, at least 10 letters are required in each text to analyze efficiently/precisely
        txt_gp = make_group(char_list,length)
        total_IOC = 0
        for item in txt_gp:
            total_IOC += IOC(item)
        IOC_avg = total_IOC/len(txt_gp)
        if IOC_avg > 0.06 and IOC_avg < 0.076: # Average IOC in English = 0.068
            if all(length%it != 0 for it in possible_length): #Key length which is multiple of existing/smaller length is discarded
                possible_length.append(length)
    return possible_length

#Calculate optimum shift to match with actual English letter frequencies
def cal_shift(txt_freq):
    max_freq = 0
    probable_shift = 0
    for i in range(26):
        freq_sum = 0
        for txt, val in txt_freq.items():
            freq_sum += val*letter_freq[chr((((ord(txt)-65)+i)%26)+65)]
        if freq_sum > max_freq:
            max_freq = freq_sum
            probable_shift = i
    return 26-probable_shift #Shift by k in actual text is shift by 26-k in encrypted text

#find Key with each predicted key lengths
def possible_text():
    key_lengths = cal_key_len()
    for length in key_lengths:
        result_key = str()
        texts = make_group(char_list, length)
        for text in texts:
            max_chars = []
            txt_freq = cal_char_freq(text)
            result_key += chr((cal_shift(txt_freq)%26)+65)
        return result_key, length

#Decrypt message with key
def decrypt(key):
    key = key*(int(len(char_list)/len(key))+1)
    message = str()
    for i in range(len(char_list)):
        message += chr((((ord(char_list[i])-65)+26-(ord(key[i])-65))%26)+65)
    return message

key, length = possible_text()
print("Key :", key, "Length :", length)
print("Message :",decrypt(key))

''' Output: Key : AMBROISETHOMAS Length : 14
Message : 
DOYOUKNOWTHELANDWHERETHEORANGETREEBLOSSOMSTHECOUNTRYOFGOLDENFRUITSANDMARVELOUSROSESWHERETHEBREEZEISSOFTERANDBIRDSLIGHTERWHEREBEESGATHERPOLLENINEVERYSEASONANDWHERESHINESANDSMILESLIKEAGIFTFROMGODANETERNALSPRINGTIMEUNDERANEVERBLUESKYALASBUTICANNOTFOLLOWYOUTOTHATHAPPYSHOREFROMWHICHFATEHASEXILEDMETHEREITISTHERETHATISHOULDLIKETOLIVETOLOVETOLOVEANDTODIEITISTHERETHATISHOULDLIKETOLIVEITISTHEREYESTHERE
'''