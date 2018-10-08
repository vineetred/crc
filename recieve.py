crc_32 = "100000100110000010001110110110111"
text = open('f_err.txt')
file_content= text.read()
# output= ' '.join(format(ord(x), '08b') for x in file_content)
count = 0
flag = 0
def recBin(stringToDecode):
    unstuffedOutput = ""
    decodedOutput = ""
 #Counter to check for consecutive 1s
    # print(finalString + "\n")

    for bit in stringToDecode:
        standardOutput = bit
        global count
        if(count == 5):
            if(standardOutput == '0'):
                count = 1
            elif(standardOutput== '1'):
                count = count + 1
                unstuffedOutput = unstuffedOutput + standardOutput

        elif(count >= 6):
            # if(standardOutput == '1'):
            #     print("Transmission Error")
            # elif(standardOutput == '0'):
            unstuffedOutput = unstuffedOutput[:len(unstuffedOutput)-7]
            count = 0
        elif(count<=4):
            if(standardOutput == '1'):
                count = count + 1
                unstuffedOutput = unstuffedOutput + standardOutput
            elif(standardOutput == '0'):
                count = 0
                unstuffedOutput = unstuffedOutput + standardOutput

    for i in range(0,len(unstuffedOutput),8):
        decodedOutput = decodedOutput + chr(int(unstuffedOutput[i:i+8], 2))
    return(unstuffedOutput)


def checkRemainder(inputString, divisor):
    global flag
    crcAdded = list(inputString)
    crcAdded = crcAdded + list('0'*len(crc_32))
    lenInput = len(inputString)
    lenDivisor = len(divisor)
    while '1' in crcAdded[:lenInput]:
        latestOne = findOne(crcAdded)
        for i in range(0, lenDivisor):
            if (divisor[i] == crcAdded[latestOne + i]):
                crcAdded[latestOne + i] = '0'
            else:
                crcAdded[latestOne + i] = '1'

    heyhey = ''.join(crcAdded)[lenInput:]
    # return heyhey
    
    for i in range(0, len(heyhey)):
        if(heyhey[i]=='1'):
            return '1'
    return '0'


def findOne(strrr):
    return strrr.index('1')

returnValUnstuffed = recBin(file_content)
for i in range(0, len(returnValUnstuffed), 400):
    frameString = returnValUnstuffed[i:i+400]
    flagReturn = checkRemainder(frameString, crc_32)
    if(flagReturn == '1'):
        print (frameString)
        print (flagReturn)
    elif(flagReturn == '0'):
        print (frameString)
        print (flagReturn)
# print (file_content)