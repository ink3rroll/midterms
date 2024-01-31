def mainMenu():
    userInput = ""
    while True:
        if userInput == "1":
            binaryOperations()
            break
        elif userInput == "2":
            numberConversion()
            break
        elif userInput == "3":
            break
        else:
            print("Invalid input.")
        
        print("Main Menu\n[1] Binary Operations\n[2] Number System Conversion\n[3] Exit")
        userInput = input(">> ")

def binaryOperations():
    while True:
        print("Binary Operations\n[1] Division\n[2] Multiplication\n[3] Subtraction\n[4] Addition\n[5] Negative\n[6] Back")
        userInput = input(">> ")
        if userInput == "1":
            x = input("x: ")
            y = input("y: ")
            print(dectobit((bittodec(x))/(bittodec(y))))
            return
        elif userInput == "2":
            x = input("x: ")
            y = input("y: ")
            print(dectobit((bittodec(x))*(bittodec(y))))
            return
        elif userInput == "3":
            x = input("x: ")
            y = input("y: ")
            print(dectobit((bittodec(x))-(bittodec(y))))
            return
        elif userInput == "4":
            x = input("x: ")
            y = input("y: ")
            print(dectobit((bittodec(x))+(bittodec(y))))
            return
        elif userInput == "5":
            value = input("Bit String: ")
            print(negative(value))
            return
        elif userInput == "6":
            mainMenu()
        else:
            print("Invalid input.")
        
        

def numberConversion():
    pass

def bittodec(bitstring):
    bitstring = str(bitstring)
    for i in bitstring:
        if i not in ("1", "0", "."):
            print("Invalid binary string.")
            return "Error"

    reverseBitString = bitstring[::-1]
    exponent = 0
    fracplaceVal = 1
    fractionTotal = 0
    sign = 0
    result = 0

    if "." in bitstring:
        for i in reverseBitString:
            if i != '.':
                fracplaceVal += 1
            else:
                fracExponent = fracplaceVal
                for i in reverseBitString[0:fracplaceVal]:
                    fracExponent -= 1
                    if i == "1":
                        fractionTotal += 1/(2**fracExponent)
                    
                reverseBitString = reverseBitString[fracplaceVal:]
                break
    fractionTotal = round(fractionTotal, 10)

    if reverseBitString[-1] == "1":
        sign = 1
    
    for i in range(0, len(reverseBitString)):
        
        if reverseBitString[i] == "1" and i == len(reverseBitString)-1:
            result += (2**exponent) * (sign*(-1))

        elif reverseBitString[i] == "1":
            result += 2**exponent
        
        exponent += 1
    
    return result + fractionTotal

# Generate a bit string from a decimal value
def dectobit(decimal):
    #Check if the input is 0
    if decimal == 0:
        return "0"
    
    elif decimal == 1:
        return "01"
    
    # Check whether the decimal is positive or negative
    sign = 0
    if decimal < 0:
        sign = 1

    # make a copy of the decimal number into and abs value
    unsignedDec = abs(decimal)
    
    # Separate the whole nnumber from the fraction by converting it into an int 
    wholeNum = int(unsignedDec)
    lenWholenum = len(str(wholeNum))

    
    
    #print(wholeNum, frac, unsignedDec)

    # Find the largest exponent for the whole number
    powersoftwo = 0
    exponent = -1
    while powersoftwo < wholeNum:
        exponent += 1
        powersoftwo = 2**exponent
    
    # Generate the whole number of the binary string
    result = ""
    while exponent > 0.99:
        exponent -= 1
        powersoftwo = 2**exponent
        if powersoftwo <= wholeNum:
            wholeNum -= powersoftwo
            result += "1"
        else:
            result += "0"
    
    if decimal%1 != 0:
        # Separate the fraction from the decimal by removing the whole number
        frac = float(str(unsignedDec)[lenWholenum:])
        # Generate the fraction
        result += "."
        exponent = 1
        while frac > 0:
            powersoftwo = 1/(2**exponent)
            if powersoftwo <= frac:
                frac -= powersoftwo
                result += "1"
            else:
                result += "0"
            
            frac = round(frac, 10)
            exponent += 1
    
    # 2's Complement of the bit string if it is negative
    result = ((result[::-1]) + "0")[::-1]
    if decimal < 0:
        result = negative(result)
    
    return result

def negative(bitstring):
    for i in str(bitstring):
        if i not in ("1", "0", "."):
            print("Invalid binary string.")
            return "Error"
    reverseBitString = str(bitstring)[::-1]
    flip = False
    reverseresult = ""
    for i in reverseBitString:
        if flip:
            if i == "1":
                reverseresult += "0"
                continue
            elif i == "0":
                reverseresult += "1"
            
            else:
                reverseresult += "."
        else:
            reverseresult += i
        
        if i ==  "1":
            flip = True

    return reverseresult[::-1]

if __name__ == "__main__":
    mainMenu()