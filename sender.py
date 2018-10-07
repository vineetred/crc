crc_32 = "100000100110000010001110110110111"

#Opening the file
text = open('input.txt')
file_content= text.read()

#Converting to binary
output= ' '.join(format(ord(x), '08b') for x in file_content) #This converts the
myfileStringBinary = output.replace(" ", "")

#Polynomial division
def remainder(inputString, divisor):
    crcAdded = list(inputString + '0'*len(crc_32))
    while '1' in crcAdded[:len(inputString)]:
        latestOne = findOne(crcAdded)
        for i in range(0, len(divisor)):
            if (divisor[i] == crcAdded[latestOne + i]):
                crcAdded[latestOne + i] = '0'
            else:
                crcAdded[latestOne + i] = '1'

    heyhey = ''.join(crcAdded)[len(inputString):]
    return heyhey

def findOne(strrr):
    return strrr.index('1')

def assignment1(crcPadded):
    finalString = crcPadded

    standardOutput = ""
    stuffedOutput = ""
    decodedOutput = ""
    count = 0 #Counter to check for consecutive 1s
    seperate = '01111110' #Frame separatorprint(finalString + "\n")
    for bit in finalString: 
        standardOutput = bit #loading each bit into the the var
        
        if(count == 5):
            count = 1
            stuffedOutput = stuffedOutput + '0' + standardOutput #Putting an end to consecutive 1s

        elif(count<=4):
            if(standardOutput == '1'):
                count = count + 1
                stuffedOutput = stuffedOutput + standardOutput

            elif(standardOutput == '0'):
                count = 0
                stuffedOutput = stuffedOutput + standardOutput

        if(len(stuffedOutput)%400==0):
            stuffedOutput = stuffedOutput + seperate

    stuffedOutput = seperate + stuffedOutput #Adding the flag to the first frame
    return stuffedOutput

#Opening the file
text = open('input.txt')
file_content= text.read()

#Converting to binary
output= ' '.join(format(ord(x), '08b') for x in file_content) #This converts the
myfileStringBinary = output.replace(" ", "")


hello = ""

for i in range(0,len(myfileStringBinary),400):
    frameString = myfileStringBinary[i:i+400]
    finalFrameString = frameString + remainder(frameString, crc_32)
    hello = hello + assignment1(finalFrameString)
print (hello)

out = open('f_send.txt', 'w')
out.write(hello)