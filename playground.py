
def findOne(strrr):
    return strrr.index('1')



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
    print("Remainder: ", heyhey)
    
    for i in range(0, len(heyhey)):
        if(heyhey[i]=='1'):
            return '1'
    return '0'


def remainder(inputString, divisor):
    crcAdded = list(inputString)
    crcAdded = crcAdded + list('0'*3)
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
    return heyhey



print(remainder("01101000","1011"))
print(checkRemainder("0110100001100101011011000110110001101111011","1011"))


# unstuffedOutput = stuffedOutput.replace('01111110', '')
# unstuffedOutput = stuffedOutput.replace('111110','11111')

# for i in range(0, len(unstuffedOutput), 400)):
#     truth = checkRemainder(unstuffedOutput[i:i+400],crc_32)
#     print(unstuffedOutput[i:i+400])
#     print(truth)


# this is my rough work thing. the crc remainder for this input should have been 100. But i am getting 111. Chec