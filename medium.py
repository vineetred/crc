crc_32 = "100000100110000010001110110110111"

text = open('f_err.txt')
file_content= text.read()

count = 0
textOutput = open('f_detect.txt','w')


def checkRemainder(inputString, divisor):
    global flag
    crcAdded = list(inputString)
    # crcAdded = crcAdded + list('0'*(len(crc_32)-1))
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
    
    for i in range(0, len(heyhey)):
        if(heyhey[i]=='1'):
            return '1'
    return '0'



def findOne(strrr):
    return strrr.index('1')

unstuffedOutput1 = file_content.replace('01111110', '')
unstuffedOutput2 = unstuffedOutput1.replace('111110','11111')


for i in range(0, len(unstuffedOutput2), (400+len(crc_32)-1)):
    frameString = unstuffedOutput2[i:i+(400+len(crc_32)-1)]
    try:
        flagReturn = checkRemainder(frameString, crc_32,)
        if(flagReturn == '1'):
            print (frameString)
            print ("Error: ",flagReturn)
            textOutput.write("01111110")
            textOutput.write(frameString)
            textOutput.write("\n")
            textOutput.write(flagReturn)
            textOutput.write("\n")
            

        elif(flagReturn == '0'):
            print (frameString)
            print (flagReturn)
            textOutput.write("01111110")
            textOutput.write(frameString)
            textOutput.write("\n")
            textOutput.write(flagReturn)
            textOutput.write("\n")
    except:
        print (frameString)
        print ('1')
        textOutput.write("01111110")
        textOutput.write(frameString)
        textOutput.write("\n")
        textOutput.write('1')
        textOutput.write("\n")
