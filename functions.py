def clear():
    import os

    os.system("clear")

def numberInput():
    

    try:
        # allows the numbers that will be formed to be used in other functions
        global number1
        global number2

        # asks the user for the numbers that will be used for operations
        number1 = int(input("number 1: "))
        number2 = int(input("number 1: "))
    
    # checks if the number inputted is actually a number and not some other character
    except ValueError:
        print("input a number instead of a letter or symbol")

class MathOperations:
    def addition():
        numberInput()

        additionSum = number1 + number2

        return additionSum

    def subtraction():
        numberInput()

        subtractionDifference = number1 - number2

        return subtractionDifference

    def multiplication():
        numberInput()

        multiplicationProduct = number1 * number2

        return multiplicationProduct

    def division():
        numberInput()

        divisionQuotient = number1 / number2

        return divisionQuotient

    def exponent():
        numberInput()

        exponentApplication = number1^number2

        return exponentApplication

    def squareRoot():
        import math
        try:
            number1 = int(input("number 1: "))
        except ValueError:
            print("input a number instead of a letter or symbol")
    
        squareRootApplication = math.sqrt(number1)

        return squareRootApplication