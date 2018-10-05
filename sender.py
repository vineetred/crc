crc_32 = "100000100110000010001110110110111"



def remainder(inputString, divisor):
    paddedArray = list(inputString + '0'*3)
    while '1' in paddedArray[:len(inputString)]:
        latestOne = paddedArray.index('1')
        for i in range(0, len(divisor)):
            if divisor[i] == paddedArray[latestOne + i]:
                paddedArray[latestOne + i] = '0'
            else:
                paddedArray[latestOne + i] = '1'

    heyhey = ''.join(paddedArray)[len(inputString):]
    print(heyhey)

remainder("11010011101100","1011")