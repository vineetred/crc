
testingString = "0111111011010011101100100"
crc_32= "100000100110000010001110110110111"
text = open('f_send.txt')
file_content= text.read()
print(file_content)

def unstuff(stuffedOutput):
    unstuffedOutput = ""
    count = 0
    for bit in stuffedOutput:
        


        if(count == 6):
            if(bit=='0'):
                print("Inside")
                print(unstuffedOutput)
                unstuffedOutput = unstuffedOutput[:len(unstuffedOutput)-7]
                print(unstuffedOutput)
                count = 0

        elif(count<=4):
            if(bit == '1'):
                
                count = count + 1
                unstuffedOutput = unstuffedOutput + bit
            elif(bit == '0'):
                count = 0
                unstuffedOutput = unstuffedOutput + bit
        elif(count==5):
            if(bit == '1'):
                count = count + 1
                unstuffedOutput = unstuffedOutput + bit
            elif(bit == '0'):
                count = 0

    return unstuffedOutput

def findOne(strrr):
    return strrr.index('1')

def checkRemainder(inputString, divisor):
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
    print("Remainder: ", heyhey)
    
    for i in range(0, len(heyhey)):
        if(heyhey[i]=='1'):
            return '1'
    return '0'
unstuffed = unstuff(testingString)
for i in range(0,len(file_content),400):
    print("Unstuffed: ", unstuffed[i:i+400])
    print("Error: ", checkRemainder(unstuffed[i:i+400], "100000100110000010001110110110111"))