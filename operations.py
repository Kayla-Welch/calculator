def clear():
    import os

    os.system("clear")

def addition():
    try:
        number1 = int(input("number 1: "))
        number2 = int(input("number 1: "))
    except ValueError:
        print("input a number instead of a letter or symbol")

    additionSum = number1 + number2

    return additionSum

def subtraction():
    try:
        number1 = int(input("number 1: "))
        number2 = int(input("number 1: "))
    except ValueError:
        print("input a number instead of a letter or symbol")

    subtractionDifference = number1 - number2

    return subtractionDifference

def multiplication():
    try:
        number1 = int(input("number 1: "))
        number2 = int(input("number 1: "))
    except ValueError:
        print("input a number instead of a letter or symbol")

    multiplicationProduct = number1 * number2

    return multiplicationProduct

def division():
    try:
        number1 = int(input("number 1: "))
        number2 = int(input("number 1: "))
    except ValueError:
        print("input a number instead of a letter or symbol")

    divisionQuotient = number1 / number2

    return divisionQuotient

